listaRegistro = []
clientes = 0
costoTotal = 0
respuesta = input("Desea ingresar un cliente?")
while respuesta == "si":
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = float(input("Costo($0.00): "))
    registro = {"cliente": cliente, "producto": producto, "costo": costo}
    listaRegistro.append(registro)
    costoTotal += costo
    respuesta = input("Desea seguir ingresando clientes?")

for registro in listaRegistro:
    print(registro)

print("El costo total es: " + str(costoTotal))
