import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener


class SizeOffsets():
    def __init__(self):
        self.int = 4
        self.bool = 1
        self.char = 1
        self.void = 0

    def getSize(self, type):
        if type == 'int':
            return self.int
        elif type == 'char':
            return self.char
        elif type == 'boolean':
            return self.bool
        elif type == 'void':
            return self.void
    
    def sizeArray(self, size, type):
        if type == 'int':
            return self.int * size
        elif type == 'char':
            return self.char * size
        elif type == 'boolean':
            return self.bool * size
        elif type == 'void':
            return self.void * size
 
class TableItem():
    def __init__(self, id, type, offset, size, params=False, scope="global", value=None,  array=False):
        self.id = id
        self.type = type
        self.offset = offset
        self.size = size
        self.params = params
        self.scope = scope
        self.value = value
        self.array = array

class DecafPrueba(DecafListener):

    def __init__(self):
        self.table = {'global':[None,None,{}]}
        self.scopeTemporal = []
        self.nodeTypes = {}
        self.nodeCodes = {}
        self.subScopes = 0
        self.contTemp = 0
        self.errors = []
        self.offsets = {'global':[]}
        self.sizes = {
            "int": 4,
            "bool": 1,
            "char": 1,
            "void": 0
        }

    

    def crearTemporal(self):
        # Crea nueva variable temporal para codigo intermedio t0, t1, t2, etc...
        temporal = 't'+ str(self.contTemp)
        self.contTemp += 1
        return temporal

    def TopeGet(self, id):
        # Para este metodo
        # Se le aplica a una variable
        # Con esta variable, voy a mi tabla de simbolos a sacar s
            #  Su scope
            #  Su offset
        # Si es variable global creo la direccion G[offset]
        # Si es variable local creo la direccion L[Offset]
        # Regreso la address G[0], G[4], L[8].... ETC
        info = self.getTableInfo(id)
        #print(info.id, info.offset, info.scope) 
        if(info.scope == "global"):
            dir = 'G['+str(info.offset)+']'
            return dir
        else:
            dir = 'L['+str(info.offset)+']'
            return dir
            
    def getTableInfo(self, id):
        encontrado = False
        for k in reversed(list(self.table.keys())):
            if((encontrado == False) and (k in self.scopeTemporal)):
                for key, value in self.table[k][2].items():
                    if (id == value.id):
                        encontrado = True
                        return value

    
    # LISTENER ENTRAR AL PROGRAMA
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        
        print("Entro al programa\n")
        self.scopeTemporal.append("global")
        self.offsets[self.scopeTemporal[-1]].append(0)

    # LISTENER DEL FIN DEL PROGRAMA  
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        
        # PRINT DE TABLA DE SIMBOLOS
        print("Tabla de variables final")
        for k,v in self.nodeTypes.items():
            print(k,",",v)

        print("-"*15)
        for key,value in self.table.items():
            
            print("Scope:", key)
            print("Padre:",value[0])
            print("Tipo:",value[1])

            for k,v in value[2].items():
                print("     Variable:", v.id,"Tipo:",  v.type,"Offset:", v.offset,"Tamanio:", v.size,"Es parametro?:", v.params,"Es array?", v.array)
            print("-"*15)
        print("Salgo del programa\n")

    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        # Para manejo de Scopes
        tipo = ctx.getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        self.scopeTemporal.append(nombre)
        self.table[self.scopeTemporal[-1]] = [self.scopeTemporal[-2],tipo,{}]
        self.offsets[self.scopeTemporal[-1]] = [0]
        self.nodeTypes[ctx] = tipo
        print("El ctx del metodo",nombre,"es:",ctx,"\n")

    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        self.scopeTemporal.pop()

    def enterParameter(self, ctx:DecafParser.ParameterContext):
        #AUN NO SE REVISA ESTO
        print("*"*100)
        tipo = ctx.getChild(0).getChild(0).getText()
        variable = ctx.getChild(1).getText()
        self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, 0, 0, params=True, scope=self.scopeTemporal[-1])

        

        self.nodeTypes[ctx] = tipo

    def enterVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        # El hijo 0 de un varDeclaration es un varType y el hijo 0 de ese varType es el mero tipo
        # El hijo 1 de un varDeclaration es el nombre de la variable
        # El hijo 2 de un varDeclaration es el fin ;
        variable = ctx.getChild(1).getText()
        tipo = ctx.getChild(0).getText()
        
        if(ctx.NUM()!=None):
            size = self.sizes[tipo]
            cantidad = int(ctx.getChild(3).getText())
            offsetAct = self.offsets[self.scopeTemporal[-1]][-1]
            newSize = size*cantidad
            offset = self.offsets[self.scopeTemporal[-1]][-1]+(size*cantidad)

            #print("El offset actual", offsetAct)
            #print("El size de la variable", newSize)
            #print("El offset luego de la variable", offset)
            self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, offsetAct, newSize, array=True, scope=self.scopeTemporal[-1])
            self.offsets[self.scopeTemporal[-1]].append(offset)

        else:
            size = self.sizes[tipo]
            

            offsetAct = self.offsets[self.scopeTemporal[-1]][-1]
            offset = self.offsets[self.scopeTemporal[-1]][-1]+size
            #print("El offset actual", self.offsets[self.scopeTemporal[-1]][-1])
            #print("El size de la variable", size)
            #print("El offset luego de la variable", offset)

            self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, offsetAct, size, scope=self.scopeTemporal[-1])
            self.offsets[self.scopeTemporal[-1]].append(offset)


        
        self.nodeTypes[ctx] = 'void'
        print("El ctx de la declaracion de la variable",variable,"es:",ctx,"\n")
        


    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        
        print("El ctx de un INT literal es:", ctx.getText(), ctx)
        #print("El valor del INT literal es:",ctx.NUM())
        self.nodeTypes[ctx] = 'int'
        self.nodeCodes[ctx] = {
            'codigo': [],
            'dir': ctx.getText()
        }
        #print("METIENDO A",ctx,"EL VALOR",{
        #    'codigo': [],
        #    'dir': ctx.getText()
        #})
        print("Saliendo del Int Literal\n")




    def exitStatementLOCATION(self, ctx:DecafParser.StatementLOCATIONContext):
        print("El ctx de un statement location (asignacion) es:", ctx)
        #print("Tiene una cantidad de hijos", ctx.getChildCount())

        left = ctx.location()               # Seria como variable a
        right = ctx.expression()            # Seria como numero 3
        self.nodeTypes[ctx] = 'void'

        print("El right es", right)
        print("El left es",left)
        print("Esto es un",left.getText(),"=",right.getText())
        
        #Trabajando con el valor asignado a la variable
        print("*"*20)
        print("BUSCANDO",right)
        print("*"*20)

        E = self.nodeCodes[right]

        if("[" not in left.getText()):
            id = left.getText()
            # hacer top get
            # E['code'] + [topget + ' = ' + E['addr']] 
            top = self.TopeGet(id)
            code = E['codigo'] + [top+' = '+E['dir']]
            print("*"*20)
            print("CODIGO INTERMEDIO")
            for i in code:
                print(i)
            print("*"*20)
        else:
            print("Es array")
        
        print("Saliendo de un statement \n")


    def exitLiteral(self, ctx:DecafParser.LiteralContext):
        child = ctx.getChild(0)
        #print("METIENDO A",ctx,"EL VALOR",child,self.nodeCodes[child])
        self.nodeTypes[ctx] = self.nodeTypes[child]
        self.nodeCodes[ctx] = self.nodeCodes[child]
        print()

    def exitExpr_literal(self, ctx:DecafParser.Expr_literalContext):
        
        literal = ctx.getChild(0)


        integers = literal.getChild(0)
        characters = literal.getChild(1)
        booleans = literal.getChild(2)
        
        if(integers):
            print("ESTAMOS SALIENDO DE UN EXPR DE INTS\n")
            #print("METIENDO A",ctx,"EL VALOR",literal,self.nodeCodes[literal])
            self.nodeTypes[ctx] = self.nodeTypes[literal]
            self.nodeCodes[ctx] = self.nodeCodes[literal]
            print()

        if(characters):
            print("ESTAMOS SALIENDO DE UN EXPR DE CHARACTERS\n")
        if(booleans):
            print("ESTAMOS SALIENDO DE UN EXPR DE BOOLEANS\n")

    def exitExpr_loc(self, ctx:DecafParser.Expr_locContext):
        yo = ctx
        child = ctx.location()
        print("exitExpr_loc")
        print("*"*20)
        print("yo",yo)
        print("BUSCANDO",child)
        print("*"*20)
        self.nodeCodes[ctx] = self.nodeCodes[child]

    def exitLocation(self, ctx:DecafParser.LocationContext):
        #AQUI OBTENGO EL CTX DE LA VARIABLEEE
        #print("-"*20)
        #print("En el exitLocation")
        #print("Yo",ctx)
        #print("Yo",ctx.getText())
        #print(ctx.getChild(0))
        variable = ctx.getText()
        #print("Encontro el var_id",variable)

        addr = self.TopeGet(variable)
        #print("Lo que devuelve el topeget es",addr)
        #print("-"*20)

        
        self.nodeCodes[ctx] = {
            'codigo': [],
            'dir': addr
        }
        
        
    def exitExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        print("SALIENDO DE exitExpr_arith4,",ctx)
        
        left = ctx.getChild(0)
        sign = ctx.getChild(1).getText()
        right = ctx.getChild(2)
        addr = self.crearTemporal()

        code = self.nodeCodes[left]['codigo']+self.nodeCodes[right]['codigo']+[addr+' = '+self.nodeCodes[left]['dir'] + ' '+sign+' '+self.nodeCodes[right]['dir']]
        
        self.nodeCodes[ctx] = {
            'codigo': code,
            'dir': addr
        }
        #print("Object",self.code_nodes[ctx])
    def exitExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        print("SALIENDO DE exitExpr_arith5,",ctx)
        
        left = ctx.getChild(0)
        sign = ctx.getChild(1).getText()
        right = ctx.getChild(2)
        addr = self.crearTemporal()

        code = self.nodeCodes[left]['codigo']+self.nodeCodes[right]['codigo']+[addr+' = '+self.nodeCodes[left]['dir'] + ' '+sign+' '+self.nodeCodes[right]['dir']]
        
        self.nodeCodes[ctx] = {
            'codigo': code,
            'dir': addr
        }
        
    def exitExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        left = ctx.getChild(1)
        addr = self.crearTemporal()
        code = self.nodeCodes[left]['codigo']+[addr+' = '+'menos '+self.nodeCodes[left]['dir']]
        
        self.nodeCodes[ctx] = {
            'codigo': code,
            'dir': addr
        }

    def exitExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        print("EN exitExpr_parenthesis", ctx)
        right = ctx.getChild(1)
        
        E = self.nodeCodes[right]

  
        self.nodeCodes[ctx] = {
            'codigo': E['codigo'],
            'dir': E['dir']
        }
        
        
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()
    prueba = DecafPrueba()
    walker = ParseTreeWalker()
    walker.walk(prueba, tree)
 
if __name__ == '__main__':
    main(sys.argv)

'''
EL NODE_CODE[CTX] TIENE DE FORMA = {
    'code':[],
    'addr':ctx.getText()
}
'''

'''
PARA OBTENER LA LINEA DONDE SE ESTA PASANDO - SE USA EN ERRORES
ctx.start.line

PARA OBTENER EL PRIMER HIJO - SE USA EN TODO
ctx.getChild(0)

PARA SABER CUANTOS HIJOS TIENE - SE USA EN TODO
ctx.getChildCount()

PARA SABER SI TIENE UNA EXPRESSION - SE USA EN LOCATIONS
ctx.expression()

PARA SABER TODO EL TEXTO QUE TIENE - SE USA EN TODO
ctx.getText()

PARA SABER EL CTX PADRE - SE USA EN BLOCKS
ctx.parentCtx
'''


'''
------------------------
int a;           //L[0]
int b;           //L[4]
int c;           //L[8]
c = 5;           //L[8] = 5 
=======================
L[8] = 5
-----------------------


'''