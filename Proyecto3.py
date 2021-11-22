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
        self.main()
        
    
    def main(self):

        file1 = open('Output.txt', 'r')
        Lines = file1.readlines()
        call = 0
        count = 0
        codeTemp = []
        # Strips the newline character
        for line in Lines:
            # PARA EVITAR LINEAS EN BLANCO
            if len(line.replace(" ", "")) > 1:

                # LINEA DE INICIO DE UN METODO
                if "DEF" in line and "EXIT" not in line:
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
        
                elif "CALL" in line:
                    # LLAMADA A OTRA TAG
                    call += 1
                
                else:
                    # BODY DE CODIGO
                    # GET REG DE INSTRUCCION
                    codeReg, getRegistros, elements = self.getReg(line)

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
                        
                        # SE ACTUALIZA EL DESCRIPTOR DE DIRECCIONES
                        # EL REGISTRO DE LA IZQUIERDA EN ESTE CASO 'x'
                        self.addr[elements[0]] = [getRegistros['x']] 


                        for k, v in self.addr.items():
                            if getRegistros['x'] in v and k != elements[0]:
                                print(getRegistros['x'],"esta en",v,"Y",k )
                                index = v.index(getRegistros['x'])
                                self.addr[k].pop(index)


        for i in self.code:
            print(i)

    def getReg(self,line):
        a_list = line.split()
        line = " ".join(a_list)
        line = line.replace(" ", "")
        print("-"*20)
        print("INSTRUCCION PARA EL GET REG",line)
        ops = ['+','-','*']
        check =  any(item in a_list for item in ops)
        registers = {
                    'x':'',
                    'y':'',
                    'z':''
                    }
        codeReg = []
        reg =  self.registros.keys()
        if check:
            print("Es una operacion",line)

            for item in ops: 
                if item in a_list:
                    op = item
            
            igual = line.find("=")
            operacion = line.find(op)
            x = line[:igual]
            y = line[igual+1:operacion]
            z = line[operacion+1:]
            elements = [x,y,z]
            if x not in reg:
                self.addr[x] = self.esTemporal(x)
            if y not in reg:
                self.addr[y] = self.esTemporal(y)
            if z not in reg:
                self.addr[z] = self.esTemporal(z)


    
            for k,v in self.registros.items():
                print("LLAVE",k,"VALOR",v)
                if y in v:
                    #print("Entro al caso 1, no se hace nada")
                    #print("Reg ",k)
                    registers['y'] = k
                    case3 = False
                    break
                if y not in v:
                    if len(v) == 0:
                        #print("Reg ",k)
                        self.registros[k] = [y] #se ingresa al registro
                        self.addr[y].append(k)
                        text = "        ldr "+k+", "+self.valor(y)
                        codeReg.append(text)
                        registers['y'] = k
                        print("*"*10)
                        print(codeReg)
                        print("*"*10)        
                        break

            for k,v in self.registros.items():
                if z in v:
                    #print("Entro al caso 1, no se hace nada")
                    #print("Reg ",k)
                    registers['z'] = k
                    break
                if z not in v:
                    if len(v) == 0:
                        #print("Reg ",k)
                        self.registros[k] = [z] #se ingresa al registro
                        self.addr[z].append(k)
                        text = "        ldr "+ k +", "+ self.valor(z) 
                        codeReg.append(text)
                        registers['z'] = k

                        break
            
          
            for k,v in self.registros.items(): #Caso 1
                if x in v:
                    registers['x'] = k
                    break

            if registers['x'] == '': #No se cumple el caso 1
                registers['x'] =registers['y']
            
            #print("LOS REGISTROS VAN ASI",self.registros)
            #print("LOS ADDR VAN ASI",self.addr)
            #print("X ES",x)
            self.addr[x].append(registers['x'])
            self.registros[registers['x']] = [x]
            
            
        else:
            print("es una asignacion",line)
            pos_eq = line.find("=")
            x = line[:pos_eq]
            y = line[pos_eq+1:]
            elements = [x,y]
            keysDir = self.addr.keys()

            if x not in keysDir:
                self.addr[x] = self.esTemporal(x)
            if y not in keysDir:
                self.addr[y] = self.esTemporal(y)

            #print("Val1 ", x)
            #print("Val2 ", y)
            tempReg = self.addr[y]
            regy = ""
            #Encontrar registro de Y
            #print("QUE MADRES ES",tempReg)
            for ele in tempReg:
                if "r" == ele[0]:
                    regy = ele
            
            self.registros[regy].append(x) #Agregar x al descriptor de registro Ry
            self.addr[x] = [x]
            registers['x'] = regy
            registers['y'] = regy
            text = "\tstr "+regy+", "+self.valor(x)
            codeReg.append(text)


        return codeReg, registers, elements

    def esTemporal(self, valor):
        if 't' in valor:
            return []
        else:
  
            return [valor]
    
    def valor(self, valor):
        #print("QUE ES VALOR",valor)
        if valor[0] == 'L':
            val = str(valor[2:-1])
            if val.isnumeric():
                valor = "[sp, #"+str(val)+"]"
                return valor
            else:
                return valor



'''
Primero, el DEF método jaja para poner el tag de cada método, y 
agregar lo del prólogo y epílogo que nos explicó turiman
Operaciones (todo lo relacionado a register y address descriptor), aquí se generan los ldr y str necesarios
Asignaciones, aquí serían los mov y str también
'''