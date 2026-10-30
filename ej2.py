from ej1 import crear_grafo_vacio, agregar_vertice, agregar_arista, vecinos
def crear_cola_vacia():
    return []

def cola_vacia(c):
    return len(c) == 0

def encolar(c, elem):
    c.append(elem)

def desencolar(c):
    if cola_vacia(c):
        raise IndexError("La cola está vacía")
    return c.pop(0)

def distancias_desde(g, origen):
    c = crear_cola_vacia()
    distancias = {}
    distancias[origen] = 0
    encolar(c, origen)
    while not cola_vacia(c):
        actual = desencolar(c)
        for v in vecinos(g, actual):
            if v not in distancias:
                distancias[v] = distancias[actual] + 1
                encolar(c, v)
    return distancias

def alcanzables_en_k_saltos(g, origen, k):
    distancias = distancias_desde(g, origen)
    return [vertice for vertice, dist in distancias.items() if dist == k]

R = crear_grafo_vacio()
for s in ["S1", "S2", "S3", "S4"]:
    agregar_vertice(R, s)

agregar_arista(R, "S1", "S2")
agregar_arista(R, "S1", "S3")
agregar_arista(R, "S2", "S3")
agregar_arista(R, "S3", "S1")
agregar_arista(R, "S4", "S3")

if __name__ == "__main__":
    print("Distancias desde S4:", distancias_desde(R, "S4"))
    print("Distancias desde S1:", distancias_desde(R, "S1"))

    print("A 1 salto desde S4:", alcanzables_en_k_saltos(R, "S4", 1))
    print("A 2 saltos desde S4:", alcanzables_en_k_saltos(R, "S4", 2))
    print("A 3 saltos desde S4:", alcanzables_en_k_saltos(R, "S4", 3))