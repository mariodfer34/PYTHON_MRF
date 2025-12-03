"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto"""

usuario = "admin"
contraseña = "1234"
usuario = input("Ingresa su nombre de usuario: ")
contraseña = input("Ingresa su contraseña: ")
if usuario == usuario and contraseña == contraseña:
    print("Inicio de sesión correcto")
else:
    print("Nombre de usuario incorrecto")