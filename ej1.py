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


R = crear_grafo_vacio()
for s in ["S1", "S2", "S3", "S4"]:
    agregar_vertice(R, s)
agregar_arista(R, "S1", "S2")
agregar_arista(R, "S1", "S3")
agregar_arista(R, "S2", "S3")
agregar_arista(R, "S3", "S1")
agregar_arista(R, "S4", "S3")

print(R)
