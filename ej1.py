def crear_grafo_vacio():
    return {}


def agregar_vertice(g, v):
    if v not in g:
        g[v] = []


def agregar_arista(g, u, v):
    agregar_vertice(g, u)
    agregar_vertice(g, v)
    
    if v not in g[u]:
        g[u].append(v)


def vertices(g):
    return list(g.keys())


def vecinos(g, u):
    return list(g.get(u, []))


def existe_arista(g, u, v):
    return u in g and v in g[u]

def grado_salida(g, u):
    return len(vecinos(g, u))

def grado_entrada(g, u):
    contador = 0
    for v in vertices(g):
        if existe_arista(g, v, u):
            contador = contador + 1
    return contador

def servidores_pozo(g):
    pozos = []
    for s in vertices(g):
        if grado_salida(g, s) == 0 and grado_entrada(g, s) > 0:
            pozos.append(s)
    return pozos


R = crear_grafo_vacio()
for s in ["S1", "S2", "S3", "S4"]:
    agregar_vertice(R, s)
agregar_arista(R, "S1", "S2")
agregar_arista(R, "S1", "S3")
agregar_arista(R, "S2", "S3")
agregar_arista(R, "S3", "S1")
agregar_arista(R, "S4", "S3")

if __name__ == "__main__":
    print(R)
    print(grado_salida(R, "S1"))
    print(grado_entrada(R, "S3"))
    print(servidores_pozo(R))
