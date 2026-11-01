from ej1 import *
def explorar_ciclo(g, u, estado, orden_instalacion):
    estado[u] = "GRIS"
    for v in vecinos(g, u):
        if estado[v] == "GRIS":
            return True
        if estado[v] == "BLANCO":
            if explorar_ciclo(g, v, estado, orden_instalacion):
                return True
    estado[u] = "NEGRO"
    orden_instalacion.append(u)
    return False

def tiene_dependencia_circular(g):
    estado = {}
    for v in vertices(g):
        estado[v] = "BLANCO"
    
    for v in vertices(g):
        if estado[v] == "BLANCO":
            if explorar_ciclo(g, v, estado, []):
                return True
                
    return False

def obtener_orden_instalacion(g):
    estado = {v: "BLANCO" for v in vertices(g)}
    orden_instalacion = []
    
    for v in vertices(g):
        if estado[v] == "BLANCO":
            if explorar_ciclo(g, v, estado, orden_instalacion):
                print("Se detectó una dependencia circular")
                return None
                
    return orden_instalacion

R = crear_grafo_vacio()
agregar_arista(R, 1, 2)
agregar_arista(R, 1, 3)
agregar_arista(R, 2, 1)

orden = obtener_orden_instalacion(R)
print("Orden de instalación:", orden)
print(tiene_dependencia_circular(R))