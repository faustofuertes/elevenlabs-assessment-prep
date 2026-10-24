# Dictionaries
# sirve para guardar colecciones con clave-valor key-value
# basicamente objetos
# formato JSON

persona = {
    "nombre":"fufulame31",
    "edad":22,
    "sexo":"masculino",
    "socials":{
        "instagram":"fausto_fuertes",
        "x":"fausto_fuertes_onX"
    }
}

# para acceder a valores
print(persona["socials"]["x"])

# cambiar valores al accedor
persona["edad"] = 23
print(persona["edad"])

# eliminar completamente una propiedad
#del persona["edad"]
#print(persona)

edad = persona.pop("edad") # elimina y retorna esa clave-valor
print(f'Edad: {edad}')
print(persona)

# sobreescribir un diccionario con otro diccionarios
a = {"name":"fufulame", "edad":22 }
b = {"name":"fufulame", "es_gay":False}

a.update(b)
print(a)

# comprobar si un diccionario tiene un propiedad
print("nombre" in persona) 
print("pito" in persona) 

# obtener todas las key
print(f'\nKeys: {persona.keys()}') 

# obtener todas los values
print(f'\nValues: {persona.values()}') 

# obtener todas las items
print(f'\nItems: {persona.items()}') 

for key, value in persona.items():
    print(f'\nKey: {key} - Value: {value}')