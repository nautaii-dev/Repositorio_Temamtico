import socket

def escanear_puertos(ip, inicio, fin):
    print("Escaneando puertos de la IP:", ip)
    for puerto in range(inicio, fin + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print("Puerto {} está abierto".format(puerto))
        sock.close()
        print("Escaneando puerto", puerto, "de", fin)

ip = input("Introduce la dirección IP a escanear: ")
inicio = int(input("Introduce el puerto inicial del rango a escanear: "))
fin = int(input("Introduce el puerto final del rango a escanear: "))
escanear_puertos(ip, inicio, fin)

