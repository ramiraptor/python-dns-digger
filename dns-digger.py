import dns.resolver

import dns.resolver

# Dominio para el que deseas obtener los registros DNS
dominio = "rowfitness.cl"

# Nombre del archivo de salida para almacenar los registros DNS
archivo_salida = "registros_dns_cloudflare.txt"

try:
    # Resolver registros A (IPv4) para el dominio
    respuesta_A = dns.resolver.resolve(dominio, 'A')

    # Resolver registros AAAA (IPv6) para el dominio
    respuesta_AAAA = dns.resolver.resolve(dominio, 'A')
    respuesta_MX= dns.resolver.resolve(dominio, 'MX')

    # Abrir el archivo de salida en modo escritura
    with open(archivo_salida, 'w') as archivo:
        archivo.write(f"Registros A (IPv4) para el dominio '{dominio}':\n")
        for registro in respuesta_A:
            archivo.write(str(registro) + "\n")

        archivo.write(f"\nRegistros AAAA (IPv6) para el dominio '{dominio}':\n")
        for registro in respuesta_AAAA:
            archivo.write(str(registro) + "\n")


        archivo.write(f"\nRegistros AAAA (IPv6) para el dominio '{dominio}':\n")
        for registro in respuesta_MX:
            archivo.write(str(registro) + "\n")


    print(f"Registros DNS (A, MX y AAAA) del dominio '{dominio}' almacenados en '{archivo_salida}'")
except dns.resolver.NXDOMAIN:
    print(f"El dominio '{dominio}' no existe.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
