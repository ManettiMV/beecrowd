class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def acha_pai(r, v):
    if r is None:
        return None
    if v <= r.valor:
        if r.esq is None:
            return r
        return acha_pai(r.esq, v)
    else:
        if r.dir is None:
            return r
        return acha_pai(r.dir, v)

def imprime_arvore(r, tipo):
    if r is not None:
        if tipo == 1:
            resultado.append(str(r.valor))
            imprime_arvore(r.esq, tipo)
            imprime_arvore(r.dir, tipo)
        elif tipo == 2:
            imprime_arvore(r.esq, tipo)
            resultado.append(str(r.valor))
            imprime_arvore(r.dir, tipo)
        elif tipo == 3:
            imprime_arvore(r.esq, tipo)
            imprime_arvore(r.dir, tipo)
            resultado.append(str(r.valor))

c = int(input())
for caso in range(1, c + 1):
    raiz = None
    n = int(input())
    valores = map(int, input().split())
    for noh in valores:
        aux = Node(noh)
        pai = acha_pai(raiz, noh)
        if pai is None:
            raiz = aux
        elif noh <= pai.valor:
            pai.esq = aux
        else:
            pai.dir = aux

    print(f"Case {caso}:")
    resultado = []
    imprime_arvore(raiz, 1)
    print("Pre.:", " ".join(resultado))
    resultado = []
    imprime_arvore(raiz, 2)
    print("In..:", " ".join(resultado))
    resultado = []
    imprime_arvore(raiz, 3)
    print("Post:", " ".join(resultado))
    print()
