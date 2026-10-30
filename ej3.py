from ej1 import vecinos
def explorar_ciclo(g, u, estado):
    estado[u] = "GRIS"
    for v in vecinos(g, u):
        if estado[v] == "GRIS":
            return True
        if estado[v] == "BLANCO":
            if explorar_ciclo(g, v, estado):
                return True
    estado[u] = "NEGRO"
    return False

