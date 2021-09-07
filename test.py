import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from DecafListener import DecafListener
from antlr4.tree.Trees import Trees


# CLASE CON LA TABLA DE SIMBOLOS PARA SACAR INFORMACION
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


# CLASE CON OVERRIDE DE LOS LISTENERS DE DECAF
# INIT CUENTA CON UN DICCIONARIO DONDE SE MANEJAN: 
    # LOS SCOPES Y LAS TABLAS DE SIMBOLOS
# DICCIONARIO CON LOS NODOS DEL ARBOL
# CONTADOR PARA MANEJAR LOS SCOPES INTERNOS COMO LOS IFS
# ARRAY CON LOS ERRORES DEL PROGRAMA
class DecafPrueba(DecafListener):
    def __init__(self):
        self.table = {'global':[None,None,{}]}
        self.scopeTemporal = []
        self.nodeTypes = {}
        self.subScopes = 0
        self.errors = []


    # LISTENER CON LA INICIALIZACION DEL PROGRAMA
    # SE AGREGA EL SCOPE GLOBAL
    def enterProgram(self, ctx:DecafParser.ProgramContext):
        self.scopeTemporal.append("global")

    # LISTENER DEL FIN DEL PROGRAMA  
    def exitProgram(self, ctx:DecafParser.ProgramContext):
        
        # NOS AYUDA A IDENTIFICAR SI SE CUMPLIO LA PROPIEDAD DE TENER UN MAIN
        mainExists = False
        mainParameters = False
        for key,value in self.table.items():
            if(key == 'main'):
                mainExists = True
                for k,v in value[2].items():
                    print(v.params)
                    if (v.params):
                        mainParameters = True
      
        # PRINT DE TABLA DE SIMBOLOS
        print("Tabla de variables final")
        print("-"*15)
        for key,value in self.table.items():
            
            print("Scope:", key)
            print("Padre:",value[0])
            print("Tipo:",value[1])

            for k,v in value[2].items():
                print("     Variable", v.id, v.type, v.offset, v.size, v.params, v.array)
            print("-"*15)
        
        
        # CHEQUEO DE MAIN
        if(mainExists):
            pass
        else:
            print("Error Main no declarado")
            self.errors.append("Error Main no declarado")
        
        if(mainParameters):
            print("Error Main tiene parametros")
            self.errors.append("Error Main tiene parametros")
        else:
            pass

        # EDITA EL TXT CON LOS ERRRORES ENCONTRADOS EN TODO EL ARCHIVO  
        textfile = open("Output.txt","w")
        if(len(self.errors) > 0):
            for element in self.errors:
                textfile.write(str(element)+"\n")
        else:
            textfile.write("Archivo sin problemas detectados de momento")
        textfile.close()

        # TODOS LOS NODOS

        #for k,v in self.nodeTypes.items():
        #    print(k,v)
            

    # LISTENER PARA CUANDO SE ENTRA A UNA DECLARACION DE METODOS
    # INGRESAMOS EN NUESTRA TABLA DE SIMBOLOS NUEVOS SCOPES
    # MANEJAMOS NUESTROS SCOPES EN UN STACK POR LO QUE HACEMOS PUSH
    def enterMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        tipo = ctx.getChild(0).getChild(0).getText()
        nombre = ctx.getChild(1).getText()
        self.scopeTemporal.append(nombre)
        self.table[self.scopeTemporal[-1]] = [self.scopeTemporal[-2],tipo,{}]
        self.nodeTypes[ctx] = tipo

    
    # LISTENER PARA CUANDO SE SALE DE UNA DECLARACION DE METODOS
    # CUANDO SALIMOS DE UN METODO SIGNIFICA QUE SALIMOS DE SU SCOPE POR LO QUE HACEMOS POP DE NUESTRO STACK
    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        nombre = ctx.getChild(1).getText()
        self.scopeTemporal.pop()
        

    # LISTENER PARA CUANDO SE INGRESA A UN PARAMETRO
    # AGREGA LOS PARAMETROS A LA TABLA DE SIMBOLOS
    # NO PERMITE QUE SE TENGAN DOS PARAMETROS IGUALES
    def enterParameter(self, ctx:DecafParser.ParameterContext):
        tipo = ctx.getChild(0).getChild(0).getText()
        variable = ctx.getChild(1).getText()

        if (variable not in self.table[self.scopeTemporal[-1]][2]):
            self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, 0, 0, params=True)
            self.nodeTypes[ctx] = tipo
        else:
            print("-"*25)
            print("Error en la linea:",ctx.start.line,"Variable declarada 2 veces en el mismo ambito")
            errorArray = "Error en la linea:",ctx.start.line,"Variable declarada 2 veces en el mismo ambito"
            self.errors.append(errorArray)
            self.nodeTypes[ctx] = 'error'
            print("-"*25)

    # LISTENER PARA CUANDO SE SALE DE UNA DECLARACION DE VARIABLE
    # UNA VEZ FUERA DE LA DECLARACION SE MODIFICA EL VALOR DEL NODO ASIGNANDO SU TIPO
    def exitVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        varType = ctx.getChild(0).getText()
        self.nodeTypes[ctx] = varType


    # LISTENER PARA CUANDO SE ENTRA A UNA DELCARACION DE VARIABLE
    # NOS SIRVE PARA IR AGREGANDO VARIABLES A NUESTRA TABLA DE SIMBOLOS
    # NO PERMMITE QUE SE DECLAREN 2 VARIABLES LLAMADAS IGUAL EN EL MISMO SCOPE
    def enterVarDeclaration(self, ctx:DecafParser.VarDeclarationContext):
        # El hijo 0 de un varDeclaration es un varType y el hijo 0 de ese varType es el mero tipo
        # El hijo 1 de un varDeclaration es el nombre de la variable
        # El hijo 2 de un varDeclaration es el fin ;
   
        variable = ctx.getChild(1).getText()
        tipo = ctx.getChild(0).getChild(0).getText()

        if(self.scopeTemporal[-1] == 'global'):
            pass
        
        if (variable not in self.table[self.scopeTemporal[-1]][2]):
            if(ctx.NUM()!=None):
                if(str(ctx.NUM()) == '0'):
                    self.nodeTypes[ctx] = 'error'
                    print("-"*25)
                    print("Error en la linea:",ctx.start.line,"Declaracion de array con posicion incorrecta")
                    errorArray = "Error en la linea:",ctx.start.line,"Declaracion de array con posicion incorrecta"
                    self.errors.append(errorArray)
                    print("Variable", '"'+variable+'"',"no guardada")
                    print("-"*25)
                else:
                    self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, 0, 0, array=True)
                    self.nodeTypes[ctx] = 'void'
            else:
                self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, 0, 0)
                self.nodeTypes[ctx] = 'void'
        else:
            print("-"*20)
            print("Error en la linea:",ctx.start.line,"Variable declarada 2 veces en el mismo ambito")
            errorArray = "Error en la linea:",ctx.start.line,"Variable declarada 2 veces en el mismo ambito"
            self.errors.append(errorArray)
            self.nodeTypes[ctx] = 'error'

 
    # LISTENER PARA CUANDO SE ENTRA A UNA LOCATION
    # QUE NOS AYUDA A ENCONTRAR VARIABLES EN NUESTRO SCOPE
    # SI NO SE LLEGARA A ENCONTRAR EN NUESTRO SCOPE VA CON EL PADRE, Y EL PADRE DEL PADRE Y ASI... HASTA LLEGAR A GLOBAL
    # SI NO ESTA EN GLOBAL DETERMINAMOS QUE NO NUNCA DUE DECLARADA POR LO QUE NO SE PUEDE UTILIZAR
    def enterLocation(self, ctx:DecafParser.LocationContext):
        encontrado = False
        # Diccionario revisado de forma inversa y solamente en el camnio de los padres de mi scope, no va a revisar a otros scopes que no tienen nada que ver
        for k in reversed(list(self.table.keys())):
            if((encontrado == False) and (k in self.scopeTemporal)):
                for key, value in self.table[k][2].items():
                    if (ctx.getChild(0).getText() == value.id):
                        self.nodeTypes[ctx] = value.type
                        encontrado = True
                        break
        if(encontrado):
            #print("VARIABLE ENCONTRADA")
            pass
        else:
            print("Error en la linea:",ctx.start.line, 'varible "'+ctx.getChild(0).getText()+'"', "no encontrada en scope",self.scopeTemporal[-1],"ni como variable global")
            errorArray = "Error en la linea:",ctx.start.line, 'varible "'+ctx.getChild(0).getText()+'"', "no encontrada en scope",self.scopeTemporal[-1],"ni como variable global"
            self.errors.append(errorArray)
            self.nodeTypes[ctx] = 'error'
            print("-"*20)

    # LISTENER PARA CUANDO SE ENTRA A UNA LLAMADA DE UN METODO
    # NOS AYUDA A DETERMINAR SI HAY ANOMALIAS EN SU LLAMADA
    # MANEJAMOS EL USO DE PARAMETRO ACA
    def enterMethodCall(self, ctx:DecafParser.MethodCallContext):
        
        metodo =  ctx.getChild(0)
        parametros = []
        _param = ctx.getChildCount()
        for x in range(_param):

            try:
                miScope = self.scopeTemporal[-1]
                param = ctx.getChild(x).getChild(0).getText()
                paramTipo = self.table[miScope][2][param].type
                #print("En el scope",miScope,"del metodo", metodo,"tengo el parametro",param,"de tipo",paramTipo)
                
                parametros.append(ctx.getChild(0).getChild(x).getChild(0).getText())
                parametros.append(paramTipo)
            except:
                pass
        if len(parametros) > 0:
  
            scopeParams = self.scopeTemporal[-1]
            #print("En el scope:",scopeParams,"Del metodo:", metodo,"Tengo los siguientes parametros",parametros)
            if(str(metodo) in self.table):  
                resp = self.checkParams(str(metodo),parametros)
            else:
               print("Error en la linea:",ctx.start.line,"Error en declaracion de metodo")
               errorArray = "Error en la linea:",ctx.start.line,"Error en declaracion de metodo"
               self.errors.append(errorArray)

            if(resp):
                print("Todo bien con",metodo)
                pass
            else:
                print("-"*25)
                print("Error en la linea:",ctx.start.line,"Problema con los parametros")
                errorArray = "Error en la linea:",ctx.start.line,"Problema con los parametros"
                self.errors.append(errorArray)
                print("-"*25)

    # LISTENER PARA CUANDO SE SALE DE UNA LLAMADA DE UN METODO
    # NOS AYUDA A AGREGAR EL VALOR DEL METODO A NUESTRO DICCIONARIO DE NODOS
    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        metodo = ctx.getChild(0)

        for k,v in self.table.items():
            if(k == str(metodo)):
                self.nodeTypes[ctx] = v[1]

                    
    # LISTENER PARA LA SALIDA DE UN METHOD CALL DE UNA EXPRESSION
    # NOS AYUDA A AGREGAR EL VALOR DE ESTE A NUESTRO DICCIONARIO DE TIPOS
    def exitExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]


    # LISTENER PARA CUANDO SALIMOS DE UN RETURN 
    # NOS AYUDA VERIFICAR SI LO QUE SE ESTA RETORNANDO ES DEL MISMO TIPO QUE QUE NUESTRA FUNCION
    def exitStatementRETURN(self, ctx:DecafParser.StatementRETURNContext):
        #print("DENTRO DE exitStatementRETURN")
        metodo = self.scopeTemporal[-1]
        #print("EL Scrope ES",metodo)
        tipoMethod = self.table[str(metodo)][1]
        #print("EL TIPO DE METODO ES", tipoMethod)
 
        #print("El valor del return",ctx.getChild(1).getText())
        if (ctx.getChild(1).getText() == ""):

            if(str(tipoMethod) != 'void'):
                print("-"*25)
                print("Error en la linea:",ctx.start.line,"Metodo:",metodo,"No tiene return y espera un return tipo",str(tipoMethod))
                errorArray = "Error en la linea:",ctx.start.line,"Metodo:",metodo,"No tiene return y espera un return tipo",str(tipoMethod)
                self.errors.append(errorArray)
                print("-"*25)
            else:
                self.nodeTypes[ctx] = 'void'
                pass
        else:
            # SI TIENE RETURN NORMAL DEBE DE CONCORDAR CON EL 
            accepted = ('int', 'char', 'boolean')

            if(str(tipoMethod) == 'subScope'):
                scopePadre = self.scopeRaiz(metodo)
                tipoScopePadre = self.table[str(scopePadre)][1]
                #print("El padre tiene tipo", tipoScopePadre)
                ctxReturn = ctx.getChild(1).getChild(0)

                exprType = self.nodeTypes[ctxReturn]
                if (exprType == tipoScopePadre):
                    self.nodeTypes[ctx] = 'void'
                    #print("RETURN CORRECTO AHUEVO")
                else:
                    self.nodeTypes[ctx] = 'error'
                    print("-"*25)
                    print("Error en la linea:",ctx.start.line,"Metodo:",scopePadre,"Tiene un tipo de return diferente")
                    errorArray = "Error en la linea:",ctx.start.line,"Metodo:",scopePadre,"Tiene un tipo de return diferente"
                    self.errors.append(errorArray)
                    print("-"*25)
            elif(str(tipoMethod) in accepted):
                ctxReturn = ctx.getChild(1).getChild(0)
                exprType = self.nodeTypes[ctxReturn]
                exprType = self.nodeTypes[ctxReturn]
                if (exprType == str(tipoMethod)):
                    self.nodeTypes[ctx] = 'void'
                    #print("RETURN CORRECTO AHUEVO")
                else:
                    self.nodeTypes[ctx] = 'error'
                    print("-"*25)
                    print("Error en la linea:",ctx.start.line,"Metodo:",metodo,"Tiene un tipo de return diferente")
                    errorArray = "Error en la linea:",ctx.start.line,"Metodo:",metodo,"Tiene un tipo de return diferente"
                    self.errors.append(errorArray)
                    print("-"*25)
            else:
                print("-"*25)
                print("Error en la linea:",ctx.start.line,"Metodo:",metodo,"No Es tipo void y tiene un return")
                errorArray = "Error en la linea:",ctx.start.line,"Metodo:",metodo,"No Es tipo void y tiene un return"
                self.errors.append(errorArray)
                print("-"*25)
        
    # METODO QUE NOS SIRVE PARA SABER QUIEN ES EL MERO PADRE DE NUESTRO SCOPE ACTUAL POR SI ESTAMOS MUY ANIDADOS Y TENEMOS UN RETURN QUE VERIFICAR
    # SE USA EN EL EXIT STAT RETURN
    def scopeRaiz(self, scopeActual):
        raiz = None
        for i in reversed(self.scopeTemporal):
            if self.table[str(i)][0] == 'global':
                raiz = i
                break
        return raiz

    # METODO QUE NOS SIRVE PARA VERIDICAR QUE LOS PARAMETROS QUE ESTAMOS INGRESANDO SON DEL MISMO TIPO DE LOS QUE FUERON DECLARADOS
    def checkParams(self, scope, params):
        acepted = True
        total = 0 
        for key,value in self.table.items():
            if(key == scope):
                #print("Scope:", key)
                #print("Padre:",value[0])
                #print("Tipo:",value[1])
                cont = 0
                for k,v in value[2].items():
                    if(v.params):
                        #print("COMPARAR", v.type,"CON", params[cont])
                        try:
                            if(str(v.type) != str(params[cont])):
                                acepted = False
                        except:
                            acepted = False
                        cont+=1
                if(cont != len(params)):
                    acepted = False
        if(acepted):
            return True
        else:
            return False

    # LISTENER DE PRIMITIVOS PARA IDENTIFICAR INTS
    def exitInt_literal(self, ctx:DecafParser.Int_literalContext):
        self.nodeTypes[ctx] = 'int'
        
    # LISTENER DE PRIMITIVOS PARA IDENTIFICAR CHARS
    def exitChar_literal(self, ctx:DecafParser.Char_literalContext):
        self.nodeTypes[ctx] = 'char'
        
    # LISTENER DE PRIMITIVOS PARA IDENTIFICAR BOOLEANS
    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        self.nodeTypes[ctx] = 'boolean'
        

    # LISTENER PARA CUANDO SALIMOS DE UN LOCATION
    # NOS AYUDA A SABER SI ES UN ARRAY O UN STRUCT
    # ES ARRAY SI TIENE EXPRESSION
    # ES STRUCT SI TIENE LOCATION (EN PROCESO....)
    # CON LO DEL ARRAY PODEMOS IDENTIFICAR SI LO QUE SE INGRESÓ ENTRE LOS CORCHETES SI ES UN NÚMERO
    def exitLocation(self, ctx:DecafParser.LocationContext):
        if (ctx.expression()):
            #print("TIENE EXPRESSION")
            if (self.nodeTypes[ctx.expression()] != 'int'):
                self.nodeTypes[ctx] = 'error'
                print("-"*25)
                print("error <expr> en ID[<expr>] debe ser un int")
                errorArray = "Error en la linea:",ctx.start.line,"error <expr> en ID[<expr>] debe ser un int"
                self.errors.append(errorArray)
                print("-"*25)
            else:
                self.nodeTypes[ctx] = self.nodeTypes[ctx.expression()] 
                #print("aGREGADO",ctx,"con valor int")

    # LISTENER PARA CUANDO SALIMOS DE UN LOCATION DE UNA EXPRESSION
    # NOS AYUDA A AGREGARLO A NUESTRO DICCIONARIO DE NODOS
    def exitExpr_loc(self, ctx:DecafParser.Expr_locContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]

    # LISTENER PARA CUANDO SALIMOS DE UN LITERAL
    # NOS AYUDA A AGREGARLO A NUESTRO DICCIONARIO DE NODOS
    def exitLiteral(self, ctx: DecafParser.LiteralContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]


    # LISTENER PARA CUANDO SALIMOS DE UN LITERAL DE UNA EXPRESION
    # NOS AYUDA A AGREGARLO A NUESTRO DICCIONARIO DE NODOS
    def exitExpr_literal(self, ctx: DecafParser.Expr_literalContext):
        self.nodeTypes[ctx] = self.nodeTypes[ctx.getChild(0)]
    
    # LISTENER PARA LAS EXPRESSIONES DE COMPARACION
    # NOS SIRVE PARA IDENTIFICAR QUE SI EST ESTÉ HACIENDO BIEN LA COMPARACION
    def exitExpr_arith3(self, ctx: DecafParser.Expr_arith3Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)
        operador = ctx.getChild(1).getText()
        operadores = ('<','<=','>','>=')

        if (operador in operadores):
            if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
                self.nodeTypes[ctx] = 'boolean'

            else:
                self.nodeTypes[ctx] = 'error'
                print("Error en la linea:",ctx.start.line)
                errorArray = "Error en la linea:",ctx.start.line
                self.errors.append(errorArray)
                print("-"*25)

        elif (operador == "==" or operador == "!="):
            tipos = ('int', 'char', 'boolean')
            type1 = self.nodeTypes[op1] 
            type2 = self.nodeTypes[op2]

            if (type1 in tipos and type2 in tipos):
                if(self.nodeTypes[op1] == self.nodeTypes[op2]):
                    self.nodeTypes[ctx] = 'boolean'

                else:
                    self.nodeTypes[ctx] = 'error'
                    print("Error")
                    print("Error en la linea:",ctx.start.line)
                    errorArray = "Error en la linea:",ctx.start.line
                    self.errors.append(errorArray)
                    print("-"*25)
            else:
                self.nodeTypes[ctx] = 'error'
                print("Error en la linea:",ctx.start.line, "Problemas en la expresion del if")
                errorArray = "Error en la linea:",ctx.start.line, "Problemas en la expresion del if"
                self.errors.append(errorArray)
                print("-"*25)
                 


    # LISTENER PARA OPERACIONES DE MULTIPLICACION Y DIVISION
    # NOS SIRVE PARA VER QUE CUANDO SE HAGAN ESTAS OPERACIONES SI SEAN CON LOS TIPOS ADECUADOS LOS OPERANDOS
    def exitExpr_arith5(self, ctx:DecafParser.Expr_arith5Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            self.nodeTypes[ctx] = 'int'
        else:
            self.nodeTypes[ctx] = 'error'
            print("Error en la linea:",ctx.start.line,"Error en la multiplicacion")
            errorArray = "Error en la linea:",ctx.start.line,"Error en la multiplicacion"
            self.errors.append(errorArray)
            

    # LISTENER PARA OPERACIONES DE SUMA Y RESTA
    # NOS SIRVE PARA VER QUE CUANDO SE HAGAN ESTAS OPERACIONES SI SEAN CON LOS TIPOS ADECUADOS LOS OPERANDOS
    def exitExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        op1 = ctx.getChild(0)
        op2 = ctx.getChild(2)

        if(self.nodeTypes[op1] == 'int' and self.nodeTypes[op2] == 'int'):
            self.nodeTypes[ctx] = 'int'
        else:
            self.nodeTypes[ctx] = 'error' 
            print("Error en la linea:",ctx.start.line,"Error en la suma")
            errorArray = "Error en la linea:",ctx.start.line,"Error en la suma"
            self.errors.append(errorArray)
            print("-"*25)
 

    # LISTENER PARA CUANDO ENTRO EN UN BLOCK
    # NOS AYUDA A SABER CUANDO ESTAMOS ENTRANDO A UN SUB SCOPE
    #LO DETERMINAMOS CUANDO EL HERMANO NO ES UN PRIMITIVO
    def enterBlock(self, ctx:DecafParser.BlockContext):
        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()
        
        if firstChild not in ('int', 'char', 'boolean', 'struct', 'void'):
            #print("PUEDE SER UN IF O UN ELSE MAYBE")
            #print("Estoy en ", self.scopeTemporal )
            inicioNombre = self.scopeTemporal[-1]
            nombre = inicioNombre + str(self.subScopes)
            self.subScopes+=1
            #print("NUEVO SCOPE",nombre)
            self.scopeTemporal.append(nombre)
            self.table[self.scopeTemporal[-1]] = [self.scopeTemporal[-2],'subScope',{}]
        
        self.nodeTypes[ctx] = 'void'
    
    # LISTENER PARA CUANDO SALGO EN UN BLOCK
    # NOS SIRVE PARA SACAR DEL STACK DE SCOPES NUESTRA SUBSCOPE
    def exitBlock(self, ctx:DecafParser.BlockContext):
        
        parentCtx = ctx.parentCtx
        firstChild = parentCtx.getChild(0).getText()
        #print(firstChild)
        if firstChild not in ('int', 'char', 'boolean', 'struct', 'void'):
            #print("Estoy en ", self.scopeTemporal )

            self.scopeTemporal.pop()
    
    # LISTENER CUANDO SE SALE DE UN IF
    # NOS SIRVE PARA DETERMINAR CUANDO LA EXPRESION EN UN IF NO ES BOOLEANO
    def exitStatementIF(self, ctx:DecafParser.StatementIFContext):
        expression = ctx.getChild(2)

        if(self.nodeTypes[expression] == 'boolean'):
            self.nodeTypes[ctx] = 'boolean'
        else:
            self.nodeTypes[ctx] = 'error'
            print("Error en la linea:",ctx.start.line, "Statement en el if no es booleano") 
            errorArray = "Error en la linea:",ctx.start.line, "Statement en el if no es booleano"
            self.errors.append(errorArray)
            print("-"*25)
        
        
        
 
def main(path):
    input_stream = FileStream(path)
    lexer = DecafLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()
    prueba = DecafPrueba()
    walker = ParseTreeWalker()
    walker.walk(prueba, tree)

    
 
if __name__ == '__main__':
    #tabla = SymbolTable()
    #main(sys.argv)
    main('C:/Users/Gustavo/Desktop/DECIMO/COMPIS/lab0-Compis/compisPython/test.decaf')

