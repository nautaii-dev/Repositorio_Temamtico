import os

def mostrar_capacidad_sistema():

    statvfs = os.statvfs("/")

    capacidad_total = statvfs.f_frsize * statvfs.f_blocks

    capacidad_libre = statvfs.f_frsize * statvfs.f_bfree

    capacidad_usada = capacidad_total - capacidad_libre

    print("Capacidad total del sistema:", capacidad_total)

    print("Capacidad libre del sistema:", capacidad_libre)

    print("Capacidad usada del sistema:", capacidad_usada)

mostrar_capacidad_sistema()

