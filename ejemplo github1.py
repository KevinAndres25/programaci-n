from datetime import datetime

# Solicitar la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingresa tu fecha de nacimiento (en formato DD/MM/AAAA): ")

# Convertir la cadena de texto a un objeto datetime
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")

# Obtener la fecha actual
fecha_actual = datetime.now()

# Calcular la edad
edad = fecha_actual.year - fecha_nacimiento.year

# Ajustar la edad si no ha cumplido años este año
if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
    edad -= 1

# Mostrar la edad
print(f"Tienes {edad} años.")


