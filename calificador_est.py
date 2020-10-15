from clave_X.clave_x import suma, multiplicacion, sumarLista, getGithubUrl

result = suma(3, 3)
if result == 6:
    print("ejercicio01: pass")
else:
    print("ejercicio01: fail")

result = multiplicacion(2, 4, 5)
if result == 40:
    print("ejercicio02: pass")
else:
    print("ejercicio02: fail")

numerosLista = []
result = sumarLista()
if result == 38:
    print("ejercicio03: pass")
else:
    print("ejercicio03: fail")

result = getGithubUrl()
if not result == "":
    print("ejercicio04: pass")
else:
    print("ejercicio04: fail")
