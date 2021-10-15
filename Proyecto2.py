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
        self.ifCont = -1
        self.contLbl = -1
        self.errors = []
        self.offsets = {'global':[]}
        self.sizes = {
            "int": 4,
            "boolean": 1,
            "char": 1,
            "void": 0
        }

    

    def crearTemporal(self):
        # Crea nueva variable temporal para codego intermedio t0, t1, t2, etc...
        temporal = 't'+ str(self.contTemp)
        self.contTemp += 1
        return temporal

    
    def crearEtiqueta(self, tipo, boolean=''):
        # Crea nueva etiqueta para codego intermedio IF_TRUE_0, IF_FALSE_0, WHILE_TRUE_0, WHILE_FALSE_0,  etc...
        if(boolean == 'TRUE' or boolean == 'FALSE'):
            f = tipo+'_'+boolean+'_'+str(self.ifCont)
            return f
        else:
            f = tipo+'_'+str(self.ifCont)
            return f


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
        #print("Tabla de variables final")
        #for k,v in self.nodeTypes.items():
        #    print(k,",",v)

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
        print("El parameter tiene estos hijos",ctx.getChildCount())
        print("Hijo 0",ctx.getChild(0),ctx.getChild(0).getText())
        print("Hijo 1",ctx.getChild(1),ctx.getChild(1).getText())


        if (ctx.getChildCount() == 2):
            print("Param normal")
            tipo = ctx.getChild(0).getChild(0).getText()
            variable = ctx.getChild(1).getText()
            size = self.sizes[tipo]
            offsetAct = self.offsets[self.scopeTemporal[-1]][-1]
            offset = self.offsets[self.scopeTemporal[-1]][-1]+size

            self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, offsetAct, size, params=True, scope=self.scopeTemporal[-1])
            self.nodeTypes[ctx] = tipo
            self.offsets[self.scopeTemporal[-1]].append(offset)
        else:
            # PARA PARAMETROS QUE SON ARRAY PERO LUEGO SE VERA ESO XD
            tipo = ctx.getChild(0).getChild(0).getText()
            variable = ctx.getChild(1).getText()
            self.table[self.scopeTemporal[-1]][2][variable] = TableItem(variable, tipo, 0, 0, params=True, scope=self.scopeTemporal[-1])
            self.nodeTypes[ctx] = tipo

        print()

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
        print("Saliendo del Int Literal\n")

    def exitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        
        print("El ctx de un bool literal es:", ctx.getText(), ctx)
        #print("El valor del INT literal es:",ctx.NUM())
        self.nodeTypes[ctx] = 'boolean'
        self.nodeCodes[ctx] = {
            'codigo': [],
            'dir': ctx.getText()
        }
        print("Saliendo del BOOL Literal\n")

    def exitChar_literal(self, ctx:DecafParser.Char_literalContext):
        
        print("El ctx de un char literal es:", ctx.getText(), ctx)
        #print("El valor del INT literal es:",ctx.NUM())
        self.nodeTypes[ctx] = 'char'
        self.nodeCodes[ctx] = {
            'codigo': [],
            'dir': ctx.getText()
        }
        print("Saliendo del CHAR Literal\n")


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
        #print("*"*20)
        #print("BUSCANDO",right)
        #print("*"*20)

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
            ##print("AGREGANDO A",ctx,"EL CODIGO",code)
            self.nodeCodes[ctx] = {
                'dir': E['dir'],
                'codigo': code
            }

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
        print("TIENE ESTOS HIJOS",ctx.getChildCount())
        print(type(literal))
    

        integers = literal.getChild(0)
        characters = literal.getChild(0)
        booleans = literal.getChild(0)
        print(integers.getText())
        print(characters.getText())
        print(booleans.getText())
        
        if(integers):
            print("ESTAMOS SALIENDO DE UN EXPR DE INTS\n")
            #print("METIENDO A",ctx,"EL VALOR",literal,self.nodeCodes[literal])
            self.nodeTypes[ctx] = self.nodeTypes[literal]
            self.nodeCodes[ctx] = self.nodeCodes[literal]
        '''
        if(characters):
            print("ESTAMOS SALIENDO DE UN EXPR DE CHARACTERS\n")
            self.nodeTypes[ctx] = self.nodeTypes[literal]
            self.nodeCodes[ctx] = self.nodeCodes[literal]
        if(booleans):
            print("ESTAMOS SALIENDO DE UN EXPR DE BOOLEANS\n")
            self.nodeTypes[ctx] = self.nodeTypes[literal]
            self.nodeCodes[ctx] = self.nodeCodes[literal]
        '''
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
        
    def enterExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        # GENERAR ETIQUETAS Y ASIGNARLAS AL HIJO
        print("*"*100)
        print("Entrando  DE enterExpr_arith2,",ctx)
        print(ctx.getChildCount())
        print(ctx.getChild(0),ctx.getChild(0).getText())
        print(ctx.getChild(1),ctx.getChild(1).getText())
        print(ctx.getChild(2),ctx.getChild(2).getText())
        #ANTES DE TODO
        
        for expr in ctx.expression():
            # PASANDOLE AL HIJO LAS PROPIEDADES DEL PADRE
            # PASANDOLE A EXPR1 Y EXPR 2 LOS DATOS DE expr mayor
            self.nodeCodes[expr] = self.nodeCodes[ctx]
            print("PASANDOLE A", expr.getText(),self.nodeCodes[expr])

        b_true = self.crearEtiqueta('EXPR')
        print("--------------------")
        cont = 0
        for expr in ctx.expression():
            if cont == 0:
                self.nodeCodes[expr] = {
                    'true': b_true,
                    'false': self.nodeCodes[expr]['false']
                }
                print("PASANDOLE A",expr.getText(),self.nodeCodes[expr])
            cont += 1
            
        print("*"*100)

    def enterExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        # GENERAR ETIQUETAS Y ASIGNARLAS AL HIJO
        print("*"*100)
        print("Entrando  DE enterExpr_arith1,",ctx)
        print(ctx.getChildCount())
        print(ctx.getChild(0),ctx.getChild(0).getText())
        print(ctx.getChild(1),ctx.getChild(1).getText())
        print(ctx.getChild(2),ctx.getChild(2).getText())
        #ANTES DE TODO
        
        for expr in ctx.expression():
            # PASANDOLE AL HIJO LAS PROPIEDADES DEL PADRE
            # PASANDOLE A EXPR1 Y EXPR 2 LOS DATOS DE expr mayor
            self.nodeCodes[expr] = self.nodeCodes[ctx]
            print("PASANDOLE A", expr.getText(),self.nodeCodes[expr])

        b_false = self.crearEtiqueta('EXPR')
        print("--------------------")
        cont = 0
        for expr in ctx.expression():
            if cont == 0:
                self.nodeCodes[expr] = {
                    'true': self.nodeCodes[expr]['true'],
                    'false': b_false
                }
                print("PASANDOLE A",expr.getText(),self.nodeCodes[expr])
            cont += 1
            
        print("*"*100)

    # Exit a parse tree produced by DecafParser#expr_arith2.
    def exitExpr_arith2(self, ctx:DecafParser.Expr_arith2Context):
        expr1 = ctx.getChild(0)
        expr2 = ctx.getChild(2)
        print("CUANDO METO ESTA COSA",expr2)
        B = self.nodeCodes[ctx]
        B1 = self.nodeCodes[expr1]
        B2 = self.nodeCodes[expr2]
        B1_true = B1['true'] 
        # print("ESTOY GENERANDO ESTO ",B1_true)
        B1_false = B['false']
        B2_true = B['true']
        B2_false = B['false']
        self.nodeCodes[expr1] = {
            'true': B1_true,
            'false': B1_false,
            'codigo': B1['codigo']
        }
        self.nodeCodes[expr2] = {
            'true': B2_true,
            'false': B2_false,
            'codigo': B2['codigo']
        }
        code = self.nodeCodes[expr1]['codigo']+[B1_true]+self.nodeCodes[expr2]['codigo']
        print("***************")
        print("CODIGO GENERADO",code)
        print("***************")
        self.nodeCodes[ctx] = {
            'codigo' : code,
            'true' : self.nodeCodes[ctx]['true'],
            'false': self.nodeCodes[ctx]['false']
        }
        print("*"*100)

    # Exit a parse tree produced by DecafParser#expr_arith1.
    def exitExpr_arith1(self, ctx:DecafParser.Expr_arith1Context):
        expr1 = ctx.getChild(0)
        expr2 = ctx.getChild(2)
        print("CUANDO METO ESTA COSA",expr2)
        B = self.nodeCodes[ctx]
        B1 = self.nodeCodes[expr1]
        B2 = self.nodeCodes[expr2]

        B1_true = B['true'] 
        B1_false = B1['false']
        B2_true = B['true']
        B2_false = B['false']
        self.nodeCodes[expr1] = {
            'true': B1_true,
            'false': B1_false,
            'codigo': B1['codigo']
        }
        self.nodeCodes[expr2] = {
            'true': B2_true,
            'false': B2_false,
            'codigo': B2['codigo']
        }
        code = self.nodeCodes[expr1]['codigo']+[B1_false]+self.nodeCodes[expr2]['codigo']
        print("***************")
        print("CODIGO GENERADO",code)
        print("***************")
        self.nodeCodes[ctx] = {
            'codigo' : code,
            'true' : self.nodeCodes[ctx]['true'],
            'false': self.nodeCodes[ctx]['false']
        }
        print("*"*100)

    def exitExpr_arith4(self, ctx:DecafParser.Expr_arith4Context):
        print("SALIENDO DE exitExpr_arith4,",ctx)
        
        left = ctx.getChild(0)
        sign = ctx.getChild(1).getText()
        right = ctx.getChild(2)
        addr = self.crearTemporal()

        code = self.nodeCodes[left]['codigo']+self.nodeCodes[right]['codigo']+[addr+' = '+self.nodeCodes[left]['dir'] + ' '+sign+' '+self.nodeCodes[right]['dir']]
        #print("AGREGANDO A",ctx,"EL CODIGO",code)
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
        #print("AGREGANDO A",ctx,"EL CODIGO",code)
        self.nodeCodes[ctx] = {
            'codigo': code,
            'dir': addr
        }

    def exitExpr_minus(self, ctx:DecafParser.Expr_minusContext):
        left = ctx.getChild(1)
        addr = self.crearTemporal()
        code = self.nodeCodes[left]['codigo']+[addr+' = '+'menos '+self.nodeCodes[left]['dir']]
        #print("AGREGANDO A",ctx,"EL CODIGO",code)
        self.nodeCodes[ctx] = {
            'codigo': code,
            'dir': addr
        }


    def enterExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        print()
        print("EN enterExpr_parenthesis",ctx.getText(),ctx)
        print("HIJO 2",ctx.getChild(1).getText(),ctx.getChild(1))

        self.nodeCodes[ctx.expression()] = self.nodeCodes[ctx]
        print("PANSANDOLE A",ctx.expression().getText(), self.nodeCodes[ctx.expression()])
        print()



    def exitExpr_parenthesis(self, ctx:DecafParser.Expr_parenthesisContext):
        print("AQUI QUE PASA",ctx)
        child = ctx.expression()
        print("EXTRAYENGO EL HIJO",child)
        E = self.nodeCodes[child]
        print("QUE TIENE E",E)
        self.nodeCodes[ctx] = E
    
    def enterStatementWHILE(self, ctx:DecafParser.StatementWHILEContext):
        print("ENTRAMOS AL WHILE",ctx)
        self.ifCont+=1
        #Aqui debo de crear los labels, 
        # si es un if normal tengo que crear un True y un next
        # Si es un if else tengo que crear un True y un False
        print("TIENE ESTOS HIJOS",ctx.getChildCount())
        inicio = self.crearEtiqueta('BEGIN_WHILE')
        b_true = self.crearEtiqueta('WHILE','TRUE')
        b_next = self.crearEtiqueta('END_WHILE')
        b_false = b_next
        expr = ctx.getChild(2)
        block = ctx.getChild(4)
        self.nodeCodes[expr] = {
            'true':b_true,
            'false':b_false
            }
        self.nodeCodes[block] = {
                'next': inicio
            }

    def exitStatementWHILE(self, ctx:DecafParser.StatementWHILEContext):
        print("Saliendo del WHILE",ctx)
        expr = ctx.expression()
        block = ctx.getChild(4)
        B = self.nodeCodes[expr]
        S = self.nodeCodes[block]
        '''
        S.codigo = 
        etiqueta (inicio) 
        || B.codigo
        || etiqueta (B.true) 
        || S 1.codigo
        || gen ( goto inicio)
        '''
        code = [S['next']]+B['codigo']+[B['true']]+S['codigo']+['GOTO '+S['next']]+[B['false']] #+ [B['true']] + S['codigo'] + [B['false']]
        print("*"*20)
        
        print("CODIGO INTERMEDIO")
        for i in code:
            print(i)
     
        #self.nodeCodes[ctx] = {
        #    'codigo': code
        #}
        print("*"*20)


    def exitStatementIF(self, ctx:DecafParser.StatementIFContext):
    
        print("#"*20)
        print("SALIENDO DE UN IF")
        if(len(ctx.children) > 5):
            #ELSE
            #   B.codigo
            #|| etiqueta (B.true) 
            #|| S 1.codigo
            #|| gen ( goto S.siguiente)
            #|| etiqueta (B.false) 
            # || S 2.codigo
            expr = ctx.expression()
            block1 = ctx.getChild(4)
            block2 = ctx.getChild(6)
            B = self.nodeCodes[expr]
            print("Esto es B",B)
            S1 = self.nodeCodes[block1]
            S2 = self.nodeCodes[block2]
            code = B['codigo']+[B['true']]+S1['codigo']+['GOTO '+ S1['next']]+[B['false']] +S2['codigo']+[S1['next']]
            print("*"*20)
            #print(code)
            print("CODIGO INTERMEDIO")
            for i in code:
                print(i)
            #print("AGREGANDO A",ctx,"EL CODIGO",code)
            self.nodeCodes[ctx] = {
                'codigo': code
            }
            print("*"*20)
            
        else:
            expr = ctx.expression()
            block = ctx.getChild(4)
            B = self.nodeCodes[expr]
            print("Esto es B",B)
            S = self.nodeCodes[block]
            code = B['codigo'] + [B['true']] + S['codigo'] + [B['false']]
            print("*"*20)
            print("CODIGO INTERMEDIO")
            for i in code:
                print(i)
            #print("AGREGANDO A",ctx,"EL CODIGO",code)
            self.nodeCodes[ctx] = {
                'codigo': code
            }
            print("*"*20)

        print("#"*20,"\n")


    def enterStatementIF(self, ctx:DecafParser.StatementIFContext):
        self.ifCont+=1
        #Aqui debo de crear los labels, 
        # si es un if normal tengo que crear un True y un next
        # Si es un if else tengo que crear un True y un False
        print("ENTRANDO AL IF",ctx)
        #print("TIENE ESTOS HIJOS",ctx.getChildCount())
        #print("HIJO 0",ctx.getChild(0))
        #print("HIJO 1",ctx.getChild(1))
        #print("HIJO 2",ctx.getChild(2),ctx.getChild(2).getText(),type(ctx.getChild(2)))
        #print("HIJO 3",ctx.getChild(3))
        #print("HIJO 4",ctx.getChild(4),ctx.getChild(4).getText(),type(ctx.getChild(4)))
        #print("HIJO 5",ctx.getChild(5))
        #print("HIJO 6",ctx.getChild(6),ctx.getChild(6).getText(),type(ctx.getChild(6)))
        b_true = self.crearEtiqueta('IF','TRUE')
        b_next = self.crearEtiqueta('END_IF')
        
        
        # Hijo 2 es expression
        
        # Hijo 4 es block

        if(len(ctx.children) > 5):
            expr = ctx.getChild(2)
            print("LA EXPRESION QUE DA PROBLEMA",expr,expr.getChildCount(),expr.getText(),type(expr))
            blockIF = ctx.getChild(4)
            blockELSE = ctx.getChild(6)
            print("Es un IF else")
            b_false = self.crearEtiqueta('IF','FALSE')
            self.nodeCodes[expr] = {
            'true':b_true,
            'false':b_false
            }
            self.nodeCodes[blockIF] = {
                'next': b_next
            }
            self.nodeCodes[blockELSE] = {
                'next': b_next
            }
            # aqui el b_flase se convierte en algo mas
        else:
            expr = ctx.getChild(2)
            block = ctx.getChild(4)
            b_false = b_next
            
            self.nodeCodes[expr] = {
            'true':b_true,
            'false':b_false
            }
        
            self.nodeCodes[block] = {
                'next': b_next
            }

            print("PASANDOLE A",expr.getText(),self.nodeCodes[expr])
            
            print("PASANDOLE A",block.getText(),self.nodeCodes[block])
            
        print()

    

    def enterBlock(self, ctx:DecafParser.BlockContext):
        
        if (type(ctx.parentCtx) == DecafParser.StatementIFContext):
        
            print("Entro al block",ctx)
            print("Y TIENE ESTA CANTIDAD DE HIJOS",ctx.getChildCount())
            print("HIJO 0",ctx.getChild(0))
            print("HIJO 1",ctx.getChild(1),type(ctx.getChild(1)),ctx.getChild(1).getText())
            print("HIJO 2",ctx.getChild(2))
            print("HAY ESTA CANTIDAD DE VARIABLES DELCARADAS EN EL BLOCK",len(ctx.varDeclaration()))
            print("HAY ESTA CANTIDAD DE STATEMENTS EN EL BLOCK",len(ctx.statement())) 
            
            # TODO:
            # LUEGO HACER UN FI PARA CUADNO SEA MAS DE UN BLOCK
            # HACER FOR PARA PARA RECOLECTAR TODOS LOS (varDeclaration)* Y (statement)*
            # EN EL CICLO ESE HAY QUE HACER PRUEBAS CON TODOS LOS STATEMENTS PARA VER QUE TODO SE GUARDE
            

            expression = ctx.parentCtx.getChild(2)
            print("Expression en el block es..",expression)
            exprAddr = self.nodeCodes[expression]
            print("Y tiene dentro",exprAddr)
            print("Dentro de un block dentro de un if")
            

        print()

    def exitBlock(self, ctx:DecafParser.BlockContext):
        print("salgo al block",ctx)
        if (type(ctx.parentCtx) == DecafParser.StatementIFContext):
            
            
            print("Y TIENE ESTA CANTIDAD DE HIJOS",ctx.getChildCount())
            print("HIJO 0",ctx.getChild(0))
            print("HIJO 1",ctx.getChild(1),type(ctx.getChild(1)),ctx.getChild(1).getText())
            print("HIJO 2",ctx.getChild(2))
            #assignacion = ctx.getChild(1)
            #print("Entonces no tengo un",assignacion)
            #B = self.nodeCodes[assignacion]
            #print("ESTO ES B",B)
            #print("ESTOY EN",ctx)
            #print("NO TENGO ESTO",self.nodeCodes[ctx])
            #self.nodeCodes[ctx]['codigo'] = B['codigo']
            print("HAY ESTA CANTIDAD DE VARIABLES DELCARADAS EN EL BLOCK",len(ctx.varDeclaration()))
            print("HAY ESTA CANTIDAD DE STATEMENTS EN EL BLOCK",len(ctx.statement())) 
            statements = ctx.statement()
            code = []
            for i in statements:
                #print("Los statements ->>:",i,i.getText())
                #print(self.nodeCodes[i])
                code.extend(self.nodeCodes[i]['codigo'])
            print("EL CODE GENERADO",code)
            self.nodeCodes[ctx]['codigo'] = code

        elif(type(ctx.parentCtx) == DecafParser.StatementWHILEContext):
            print("Es un while")
            statements = ctx.statement()
            code = []
            for i in statements:
                print("Los statements ->>:",i,i.getText())
                print(self.nodeCodes[i])
                code.extend(self.nodeCodes[i]['codigo'])
            print("EL CODE GENERADO",code)
            self.nodeCodes[ctx]['codigo'] = code
        else:
            print("No es if ni while")
            statements = ctx.statement()
            code = []
            for st in statements:
                code.extend(self.nodeCodes[st]['codigo'])
            print(code)
        
            self.nodeCodes[ctx] = {
                'dir': [],
                'codigo': code
            }

        print()

    def enterExpr_not(self, ctx:DecafParser.Expr_notContext):
        print("ESTOY ENTRANDO AL NOT",ctx)
        print("HIJO 0",ctx.getChild(0))
        print("HIJO 1",ctx.getChild(1).getText())
    
    def exitExpr_not(self, ctx:DecafParser.Expr_notContext):
        print("ESTOY SALIENDO AL NOT",ctx)

    def exitExpr_arith3(self, ctx:DecafParser.Expr_arith3Context):
        
        print("Y BUSCANDO SALIENDO CTX exitExpr_arith3",ctx)
        print("CANTIDAD HIJOS",ctx.getChildCount())
        print("HIJO 0",ctx.getChild(0),ctx.getChild(0).getText())
        print("HIJO 1",ctx.getChild(1),ctx.getChild(1).getText())
        print("HIJO 2",ctx.getChild(2),ctx.getChild(2).getText())
        print("BUSCANDO DONDE ENTRA",ctx)
        print("Datos",self.nodeCodes[ctx])
        # AHORITA TENGO Datos {'true': 'IF_TRUE_0', 'false': 'NEXT_S_0'}
        child = ctx.arith_op_third()
        B = self.nodeCodes[ctx]
        if(child.rel_op() or child.eq_op() ):
            expr = ctx.expression()
            for i in expr:
                print("BUSCANDO XD",i)
                
            E1 = self.nodeCodes[expr[0]] # PARA LA VARIABLE A
            E2 = self.nodeCodes[expr[1]] # PARA EL NUM 5
            #print("ESTOS ES E1",E1)
            #print("ESTOS ES E2",E2)
            if(child.rel_op()):
                op = child.rel_op().getText()
            elif(child.eq_op()):
                op = child.eq_op().getText()

            code = E1['codigo']+E2['codigo']+['IF '+E1['dir']+' '+op+' '+E2['dir']+' GOTO '+B['true']]+['GOTO '+B['false']]
            print("CODIGO GENERADO")
            print(code)
            B['codigo'] = code

        print("-"*20)
        print()

    def exitMethodDeclaration(self, ctx:DecafParser.MethodDeclarationContext):
        print("Saliendo de un method decl",ctx)
        nombre = ctx.ID().getText()
        codigo = self.nodeCodes[ctx.block()] 
        code = ['DEF '+nombre+":"]+codigo['codigo']+['EXIT DEF '+nombre]
        print("*"*20)
        
        print("CODIGO INTERMEDIO")
        for i in code:
            print(i)
     
        print("*"*20)
        self.nodeCodes[ctx] = {
            'codigo' : code
        }
    
    def exitStatementRETURN(self, ctx:DecafParser.StatementRETURNContext):
        expr = ctx.expression()
        code = ['RETURN ' + self.nodeCodes[expr]['dir']]
        print("EL CODE RETURN",code)

        self.nodeCodes[ctx] = {
            'codigo':code
        }

    def exitExpr_mcall(self, ctx:DecafParser.Expr_mcallContext):
        expr = ctx.methodCall()
        print(expr.getText())
        self.nodeCodes[ctx] = self.nodeCodes[expr]
        print()

    def exitMethodCall(self, ctx:DecafParser.MethodCallContext):
        expr = ctx.expression()
        nombre = ctx.ID().getText()
        hijos = len(expr)
        code = []
        for exp in expr:
            code.extend(['PARAM '+self.nodeCodes[exp]['dir']])

        call = 'CALL ' + nombre + str(hijos)
        code.append(call)
        print("EL CODE EXIRT MEHTOD CALL", code)
        self.nodeCodes[ctx] = {
            'codigo' : code,
            'dir': 'R'
        }
    def exitStatementMETHODCALL(self, ctx:DecafParser.StatementMETHODCALLContext):
        child = ctx.methodCall()
        self.nodeCodes[ctx] = self.nodeCodes[child]
    

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