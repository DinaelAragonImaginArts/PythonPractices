#function = def

def estudiantes():
    print("Estudiantes aprendiendo Python")

estudiantes() 


def tabla_del_7():
    for x in range(10):
        print("7*{}={}".format(x,x*7))

tabla_del_7()


def advierto():
    global variable
    variable = 'Jose'
    print(variable)
    variable = 'Dinael'

advierto()

print (variable)