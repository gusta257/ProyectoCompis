#Proyecto 3
'''

    Descriptor de Registros contiene
    todos los registros disponibles a utilizar
    y lo que tienen dentro 
    registros = {
        r0: ['L[0]'],
        r1: ['t0'],
        r2: [],
        r3: [],
        r4: [],
        r5: [],
        r6: [],
        r7: [],
        r8: [],
        r9: [],
        r10: []
    }

    Descriptor de direcciones contiente
    direcciones = {
        t0: ['t0', 'r1']
        L[0]: ['L[0]', 'r0']
    }

'''

class CodigoTarget():
    def __init__(self, size):
        self.registros = {
            'r0': [],
            'r1': [],
            'r2': [],
            'r3': [],
            'r4': [],
            'r5': [],
            'r6': [],
            'r7': [],
            'r8': [],
            'r9': [],
            'r10': []
        }
        self.funcionSize = size
        print(self.funcionSize)
        self.addr = {}
        self.code = []
        self.arm = []
        self.main()
        
    
    def main(self):

        file1 = open('Output.txt', 'r')
        Lines = file1.readlines()
        call = 0
        param = 0
        count = 0
        codeTemp = []
        # Strips the newline character
        for line in Lines:
            # PARA EVITAR LINEAS EN BLANCO
            if len(line.replace(" ", "")) > 1:

                # LINEA DE INICIO DE UN METODO
                if "DEF" in line and "EXIT" not in line:
                    print()
                    print()
                    print()
                    self.registros = {
                        'r0': [],
                        'r1': [],
                        'r2': [],
                        'r3': [],
                        'r4': [],
                        'r5': [],
                        'r6': [],
                        'r7': [],
                        'r8': [],
                        'r9': [],
                        'r10': []
                    }
                    self.code = []
                    codeTemp = []
                    self.addr = {}
                    # NOMBRE DE LA FUNCION
                    funcion = line[4:-1]
                    # CONTADOR DE HOJA O RAMA
                    call = 0
                    # TAMANIO DE LA FUNCION COMPLETA
                    funcionS = self.funcionSize[line[4:-2]]
                    # AGREGANDO TAG
                    # main:
                    self.code.append(funcion)


                # LINEA DE SALIDA DE UN METODO
                elif "EXIT" in line:
                    print("SALIENDO")
                    # VERIFICADOR DE HOJA O RAMA
                    if(call > 0):
                        print("No es hoja")
                        # PROLOGO DE STACK CUANDO NO ES HOJA
                        self.code.append("\tpush {r11, lr}")
                        self.code.append("\tadd r11, sp, #0")
                        self.code.append("\tsub sp, sp, #"+str(funcionS))
                        
                        # BODY DE CODIGO
                        for i in codeTemp:
                            self.code.append(i)
    
                        # EPILOGO DE STACK
                        self.code.append("\tsub sp, r11, #0")
                        self.code.append("\tpop {r11,pc}")

                         

                    else:
                        print("Es hoja")
                        # PROLOGO DE STACK CUANDO ES HOJA
                        self.code.append("\tpush {r11}")
                        self.code.append("\tadd r11, sp, #0")
                        self.code.append("\tsub sp, sp, #"+str(funcionS))

                        # BODY DE CODIGO
                        for i in codeTemp:
                            self.code.append(i)

                        # EPILOGO DE STACK
                        self.code.append("\tadd sp, r11, #0")
                        self.code.append("\tpop {r11}")
                        self.code.append("\tbx lr")
                    param = 0
                    for i in self.code:
                        self.arm.append(i) 
        
                elif "PARAM" in line:
                    line = line.strip()
                    print("-"*20)
                    print("PARAMETROS",line)

                    registerP = "r"+str(param)
                    param+=1
                    print("Este param va en",registerP)
                    variable = line.find("M")
                    valor = line[variable+2:]
                    print(valor)
                    
                    if "L" in line:
                        val = str(valor[2:-1])
                        if val.isnumeric():
                            valor = "[sp, #"+str(val)+"]"
                        else:
                            
                            abrir = valor.find("[")+1
                            cerrar = valor.find("]")
                            temporal = valor[abrir:cerrar]
                            for k,v in self.registros.items():
                                if temporal in v:
                                    valor = "[sp, "+str(k)+"]"
                                    break
                        texto = "\tldr "+registerP+", "+valor
                        codeTemp.append(texto)
                        print("Codigo generado",texto)
                    else:
                        print("Es global")

                elif "CALL" in line:
                    # HAY QUE HACER IF SI LA FUNCION ES UN METODO VOID O NO
                    call += 1
                    line = line.strip()
                    param = 0 
                    posFun =  line.find(",")
                    funcion  = line[5:posFun]
                    texto = "\tbl "+ funcion
                    codeTemp.append(texto)
                    print("La funcion es",funcion)
                    print("registros",self.registros)
                    print("addr",self.addr)
                    self.registros['r0'] = ['R']
                    self.addr['R'] = ['R','r0']

                else:
                    # BODY DE CODIGO
                    # GET REG DE INSTRUCCION
                    codeReg, getRegistros, elements = self.getReg(line)
                    print("Saliendo del getReg de",line)
                    #print("Asi va addr",self.addr)
                    #print("Asi va reg",self.registros)
                    #print("registros",getRegistros)
                    #print("elements",elements)

                    # BODY DE CODIGO
                    for i in codeReg:
                        codeTemp.append(i)
 
                    # GENERACION INSTRUCCIONES PARA OPERACIONES 
                    # DE LA FORMA: OP dst, orig1, orig2 -> 
                    # ADD R0, R1, R2 --> R0 = R1 + R2
                    # SUB R0, R1, R2 --> R0 = R1 - R2
                    # MUL R0, R1, R2 --> R0 = R1 * R2
                    # x = y + z
                    if '+' in line or '-' in line or '*' in line:
                        if '+' in line:
                            codeTemp.append("\tadd "+getRegistros['x'] +", "+getRegistros['y'] +", "+getRegistros['z'])
                        if '-' in line:
                            codeTemp.append("\tsub "+getRegistros['x'] +", "+getRegistros['y'] +", "+getRegistros['z'])
                        if '*' in line:
                            codeTemp.append("\tmul "+getRegistros['x'] +", "+getRegistros['y'] +", "+getRegistros['z'])
                        
                        # SE ACTUALIZA EL DESCRIPTOR DE REGISTROS
                        # EL REGISTRO DE LA IZQUIERDA EN ESTE CASO 'x'
                        self.registros[getRegistros['x']] = [elements[0]]
                        #print("Buscando",getRegistros['x'],"en",self.registros)
                        #print("Asignando",[elements[0]])
                        
                        # SE ACTUALIZA EL DESCRIPTOR DE DIRECCIONES
                        # EL REGISTRO DE LA IZQUIERDA EN ESTE CASO 'x'
                        #print("ADDR ANTES",self.addr)
                        #print("Elements",elements)
                        #print("Registros",getRegistros)
                        #self.addr[elements[0]] = [getRegistros['x']] 
                        #print("Buscando",elements[0],"en",self.addr)
                        #print("Asignando",[getRegistros['x']])
                        #print("ADDR DESPUES",self.addr)

                    # LIMPIANDO LA DIRECCION SI ESTA NO ES 'x'
                    for k, v in self.addr.items():
                        #print("En el for",k,",",v,elements[0])
                        if getRegistros['x'] in v and k != elements[0]:  
                            #print(getRegistros['x'], elements[0])  
                            index = v.index(getRegistros['x'])
                            #print(self.addr[k],index)
                            #print("BORRANDO",self.addr[k][index])
                            self.addr[k].pop(index)
                            #print(self.addr[k],"ahora")

                    for k,v in self.registros.items():
                        if(len(v) > 0 and v[0].isnumeric()):
                            #print("Elregistro",k,"tiene un numero hay que borrar")
                            self.registros[k] = []
                            self.addr[v[0]] = [self.addr[v[0]][0]]  
                                

                    print("Asi queda addr",self.addr)
                    print("Asi queda reg",self.registros)

        print("Asi queda addr",self.addr)
        print("Asi queda reg",self.registros)
        # CODIGO FINAL
        for i in self.arm:
            print(i)


    # METODO GETREG PARA OBTENER:
    # REGISTROS INVOLUCRADOS
    # CODIGO DE CARGA DE ESOS REGISTROS
    # Y EL VALOR DESDE EL CODIGO INTERMEDIO DE REFERENCIA 
    def getReg(self,line):
        a_list = line.split()
        line = " ".join(a_list)
        line = line.replace(" ", "")
        print("-"*20)
        print("INSTRUCCION PARA EL GET REG",line)
        print(self.addr)
        ops = ['+','-','*']
        check =  any(item in a_list for item in ops)
        registers = {
                    'x':'',
                    'y':'',
                    'z':''
                    }
        codeReg = []
        reg =  self.addr.keys()
        
        # SI LA INSTRUCCION ES UNA OPERACION
        if check:
            # OBTEN REG DE LA FORMA x = y + z
            for item in ops: 
                if item in a_list:
                    op = item
            
            # DATOS DEL CODIGO INTERMEDIO
            igual = line.find("=")
            operacion = line.find(op)
            x = line[:igual]
            y = line[igual+1:operacion]
            z = line[operacion+1:]
            elements = [x,y,z]
            
            # ACTUALIZACION DEL REGISTRO DE DIRECCIONES SI ES UNA TEMPORAL
            if x not in reg:
                self.addr[x] = self.esTemporal(x)
            if y not in reg:
                self.addr[y] = self.esTemporal(y)
            if z not in reg:
                self.addr[z] = self.esTemporal(z)

            #print("Antes de revisar casos",self.addr)
            # PARA Y
            for k,v in self.registros.items():
                # CASO 1 Y
                # SI y SE ENCUENTRA EN UN REGISTRO SE SELECCIONA ESE REGISTRO
                if y in v:
                    #print("Entre aca?")
                    #print("K es",k,"Y v es",v)
                    #print("Registros",self.registros)
                    #print("Addres",self.addr)
                    registers['y'] = k
                    break
                 
                # CASO 2 Y
                # SI y NO SE ENCUENTRA EN UN REGISTRO Y HAY UN REGISTRO VACIO SE ELIGE ESE REGISTRO Y SE CARGA
                if y not in v:
                    if len(v) == 0:
                        if(y.isnumeric() ==False):
                            #print("Reg ",k)
                            self.registros[k] = [y] 
                            #print("Y Agregando a registros",k,[y])
                            self.addr[y].append(k)
                            text = "        ldr "+k+", "+self.valor(y)
                            print("Genere Y",text)
                            codeReg.append(text)
                            registers['y'] = k      
                            break
                        else:
                            #print("Reg ",k)
                            #print("QUE ES K",k)
                            #print("QUE ES REGISTROS",self.registros)
                            #print("QUE ES y",y)
                            print("Guardando en el registro",k,"el valor",y)
                            self.registros[k] = [y] 
                            #print("Y Agregando a registros",k,[y])
                            self.addr[y].append(k)
                            text = "        mov "+k+", "+self.valor(y)
                            print("Genere Y",text)
                            codeReg.append(text)
                            registers['y'] = k      
                            break

            # PARA Z
            for k,v in self.registros.items():
                # CASO 1 Z
                # SI z SE ENCUENTRA EN UN REGISTRO SE SELECCIONA ESE REGISTRO
                if z in v:
                    registers['z'] = k
                    break

                # CASO 2 Z
                # SI z NO SE ENCUENTRA EN UN REGISTRO Y HAY UN REGISTRO VACIO SE ELIGE ESE REGISTRO Y SE CARGA
                if z not in v:
                    if len(v) == 0:
                        if(z.isnumeric() ==False):
                            #print("Reg ",k)
                            self.registros[k] = [z] 
                            #print(" Z Agregando a registros",k,[z])
                            self.addr[z].append(k)
                            #print("Aqui esta el problema del ldr 3 verdad",z)
                            text = "        ldr "+ k +", "+ self.valor(z) 
                            print("Genere Z",text)
                            codeReg.append(text)
                            registers['z'] = k

                            break
                        else:
                            #print("Reg ",k)
                            self.registros[k] = [z] 
                            #print(" Z Agregando a registros",k,[z])
                            self.addr[z].append(k)
                            #print("Aqui esta el problema del ldr 3 verdad",z)
                            text = "        mov "+ k +", "+ self.valor(z) 
                            print("Genere Z",text)
                            codeReg.append(text)
                            registers['z'] = k

                            break

            
            # PARA X
            # CASO 1 X
            # SI x SE ENCUENTRA EN UN REGISTRO SE SELECCIONA ESE REGISTRO
            for k,v in self.registros.items():
                if x in v:
                    registers['x'] = k
                    break
            
            # CASO 2 X
            # REUTILIZAMOS EL REGISTRO DE y en X
            if registers['x'] == '': 
                registers['x'] = registers['y']
            
            # SE ACTUALIZA EL DESCRIPTOR DE DIRECCIONES CON LO DEL LADO IZQUIERDO "x"
            self.addr[x].append(registers['x'])

            # SE ACTUALIZA EL DECRIPTOR DE REGISTROS CON EL CONTENIDO DE X
            self.registros[registers['x']] = [x]
            #print("X Agregando a registros",registers['x'],[x])
            
        # SI LA INSTRUCCION ES UNA ASIGNACION
        # DE LA FORMA: x = y
        else:
            print("Es una asignacion",line)

            # DATOS DEL CODIGO INTERMEDIO
            igual = line.find("=")
            x = line[:igual]
            y = line[igual+1:]
            esNum= y.isnumeric()
            #print("x es",x,"y es",y)
            elements = [x,y]
            llavesD = self.addr.keys()
            #print("add es",self.addr)
            #print("LAS LLAVES DE ADDRES SON",llavesD)
            if x not in llavesD:
                self.addr[x] = self.esTemporal(x)
            if y not in llavesD:
                self.addr[y] = self.esTemporal(y)
            #print("add es",self.addr)
            #print("reg es",self.registros)
            tempReg = self.addr[y]
            registroY = ""

            # SELECCIONAMOS EL REGISTRO A UTILIZAR
            for registroN in tempReg:
                #print(tempReg)
                if "r" == registroN[0]:
                    registroY = registroN
            
            if(registroY == ""):
                for k,v in self.registros.items():
                    if len(v) == 0 and esNum == False:
                        self.registros[k] = [y]
                        self.addr[y].append(k)
                        print("Ahora",y,"esta en el registro",k)
                        print("Y addr es",self.addr)
                        text = "        ldr "+k+", "+self.valor(y)
                        print("Y EL CODE GENERADO ES",text)
                        codeReg.append(text)
                        tempReg = self.addr[y]
                        for registroN in tempReg:
                            #print(tempReg)
                            if "r" == registroN[0]:
                                registroY = registroN
                        break
                    elif len(v) == 0 and esNum:
                        self.registros[k] = [y]
                        self.addr[y].append(k)
                        print("Ahora",y,"esta en el registro",k)
                        print("Y addr es",self.addr)
                        text = "        mov "+k+", "+self.valor(y)
                        print("Y EL CODE GENERADO ES",text)
                        codeReg.append(text)
                        tempReg = self.addr[y]
                        for registroN in tempReg:
                            #print(tempReg)
                            if "r" == registroN[0]:
                                registroY = registroN
                        break
            

            # ACTUALIZAMOS EL DECRIPTOR DE REGISTROS Y DIRECCIONES CON EL VALOR DE LA IZQUIERDA
            self.registros[registroY] = [x] 
            #print("Agregando a registros",registroY,x)
            #print("Antesito",self.addr,x)
            self.addr[x].append(registroY)
            #print("Luego",self.addr)
            # ASIGNAMOS NUEVO REGISTRO PARA x Y y
            registers['x'] = registroY
            registers['y'] = registroY

            print(registers)

            # GENERACION DE CODIGO
            text = "\tstr "+registroY+", "+self.valor(x)
            codeReg.append(text)

        #print("AL TERMINAR TENGO ADDR",self.addr)
        #print("AL TERMINAR TENGO REGISTROS",self.registros)
            


        return codeReg, registers, elements

    def esTemporal(self, valor):
        return [valor]
        '''
        if 't' in valor:
            return []
        else:
  
            return [valor]
        
        '''
        
    
    def valor(self, valor):
        if valor[0] == 'L':
            
            val = str(valor[2:-1])
            if val.isnumeric():
                valor = "[sp, #"+str(val)+"]"
                return valor
            else:
                print("°"*40)
                abrir = valor.find("[")+1
                cerrar = valor.find("]")
                temporal = valor[abrir:cerrar]
                for k,v in self.registros.items():
                    if temporal in v:
                        #print("Entre aca?")
                        #print("K es",k,"Y v es",v)
                        #print("Registros",self.registros)
                        #print("Addres",self.addr)
                        #registers['y'] = k
                        valor = "[sp, "+str(k)+"]"
                        break
                return valor
        else:
            return "#"+str(valor)
