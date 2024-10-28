class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar2(valor, self.raiz)

    def insertar2(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.insertar2(valor, nodo.izquierda)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.insertar2(valor, nodo.derecha)

    def mostrar_arbol(self, nodo):
        niveles = self.altura(nodo)
        ancho_max = 2 ** niveles - 1
        matriz = [[" " for _ in range(ancho_max)] for _ in range(niveles)]

        def rellenar(nodo, nivel, pos):
            if nodo is not None:
                matriz[nivel][pos] = str(nodo.valor)
                offset = 2 ** (niveles - nivel - 2)
                rellenar(nodo.izquierda, nivel + 1, pos - offset)
                rellenar(nodo.derecha, nivel + 1, pos + offset)

        rellenar(nodo, 0, ancho_max // 2)
        for fila in matriz:
            print("".join(fila))

    def preOrden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.preOrden(nodo.izquierda)
            self.preOrden(nodo.derecha)

    def inOrden(self, nodo):
        if nodo:
            self.inOrden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.inOrden(nodo.derecha)

    def postOrden(self, nodo):
        if nodo:
            self.postOrden(nodo.izquierda)
            self.postOrden(nodo.derecha)
            print(nodo.valor, end=' ')

    def buscar(self, valor):
        return self.buscar2(self.raiz, valor)

    def buscar2(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        if valor < nodo.valor:
            return self.buscar2(nodo.izquierda, valor)
        return self.buscar2(nodo.derecha, valor)

    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

    def cantidad_hojas(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self.cantidad_hojas(nodo.izquierda) + self.cantidad_hojas(nodo.derecha)

    def cantidad_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.cantidad_nodos(nodo.izquierda) + self.cantidad_nodos(nodo.derecha)

    def completo(self, nodo):
        if nodo is None:
            return True
        queue = [nodo]
        flag = False
        while queue:
            temp = queue.pop(0)
            if temp.izquierda:
                if flag:
                    return False
                queue.append(temp.izquierda)
            else:
                flag = True
            if temp.derecha:
                if flag:
                    return False
                queue.append(temp.derecha)
            else:
                flag = True
        return True

    def lleno(self, nodo):
        if nodo is None:
            return True
        if nodo.izquierda is None and nodo.derecha is None:
            return True
        if nodo.izquierda is not None and nodo.derecha is not None:
            return self.lleno(nodo.izquierda) and self.lleno(nodo.derecha)
        return False

    def eliminar_arbol(self, nodo):
        if nodo:
            self.eliminar_arbol(nodo.izquierda)
            self.eliminar_arbol(nodo.derecha)
            print(f"Eliminando nodo: {nodo.valor}")
            nodo = None  

    def elim_arbol(self):
        self.eliminar_arbol(self.raiz)
        self.raiz = None  

    def amplitud(self):
        if self.raiz is None:
            return
        queue = [self.raiz]
        while queue:
            nodo = queue.pop(0)
            print(nodo.valor, end=' ')
            if nodo.izquierda:
                queue.append(nodo.izquierda)
            if nodo.derecha:
                queue.append(nodo.derecha)
    
    def mostrar_arbol_acostado(self, nodo, nivel=0):
        if nodo is not None:
            self.mostrar_arbol_acostado(nodo.derecha, nivel + 1)
            print("    " * nivel + str(nodo.valor))
            self.mostrar_arbol_acostado(nodo.izquierda, nivel + 1)

def menu():
    arbol = Arbol()
    while True:
        print("\n--- Menú de opciones disponibles del Árbol Binario ---")
        print("[1] Insertar elemento")
        print("[2] Mostrar árbol completo")
        print("[3] Mostrar árbol acostado (raíz a la izquierda)")
        print("[4] Buscar un elemento")
        print("[5] Recorrer el árbol en PreOrden")
        print("[6] Recorrer el árbol en InOrden")
        print("[7] Recorrer el árbol en PostOrden")
        print("[8] Recorrer el árbol por niveles (Amplitud)")
        print("[9] Altura del árbol")
        print("[10] Cantidad de hojas")
        print("[11] Cantidad de nodos")
        print("[12] Verificar si es un árbol completo")
        print("[13] Verificar si es un árbol lleno")
        print("[14] Eliminar el árbol")
        print("[15] Salir")

        opcion = int(input("Elija una opción: "))

        if opcion == 14:
            print("\nSaliendo...\n")
            break
        elif opcion == 1:
            valor = int(input("Ingrese el valor a insertar: "))
            arbol.insertar(valor)
        elif opcion == 2:
            print("Árbol binario:")
            arbol.mostrar_arbol(arbol.raiz)
        elif opcion == 3:
            print("Árbol mostrado acostado:")
            arbol.mostrar_arbol_acostado(arbol.raiz)
        elif opcion == 4:
            valor = int(input("Ingrese el valor a buscar: "))
            nodo = arbol.buscar(valor)
            print(f"Elemento {'encontrado' if nodo else 'no encontrado'}")
        elif opcion == 5:
            print("Recorrido PreOrden:")
            arbol.preOrden(arbol.raiz)
            print()
        elif opcion == 6:
            print("Recorrido InOrden:")
            arbol.inOrden(arbol.raiz)
            print()
        elif opcion == 7:
            print("Recorrido PostOrden:")
            arbol.postOrden(arbol.raiz)
            print()
        elif opcion == 8:
            print("Recorrido por niveles (Amplitud):")
            arbol.amplitud()
            print()
        elif opcion == 9:
            print(f"Altura del árbol: {arbol.altura(arbol.raiz)}")
        elif opcion == 10:
            print(f"Cantidad de hojas: {arbol.cantidad_hojas(arbol.raiz)}")
        elif opcion == 11:
            print(f"Cantidad de nodos: {arbol.cantidad_nodos(arbol.raiz)}")
        elif opcion == 12:
            print(f"Es un árbol binario completo: {arbol.completo(arbol.raiz)}")
        elif opcion == 13:
            print(f"Es un árbol binario lleno: {arbol.lleno(arbol.raiz)}")
        elif opcion == 14:
            arbol.elim_arbol()
            print("Árbol eliminado.")
        else:
            print("Opción no válida. Intente de nuevo.")

menu()
