class Producto:
    def __init__(self, nombre, precio, cantidad):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(precio, (int, float)) or isinstance(precio, bool):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")

        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or isinstance(nuevo_precio, bool):
            raise TypeError("El precio debe ser un número.")
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual a cero.")
        self.precio = float(nuevo_precio)

    def actualizar_cantidad(self, nueva_cantidad):
        if not isinstance(nueva_cantidad, int) or isinstance(nueva_cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual a cero.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return (
            f"Producto: {self.nombre} | "
            f"Precio: {self.precio:.2f} € | "
            f"Cantidad: {self.cantidad} | "
            f"Valor total: {self.calcular_valor_total():.2f} €"
        )


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser un texto.")

        nombre_buscado = nombre.strip().lower()

        if not nombre_buscado:
            raise ValueError("El nombre no puede estar vacío.")

        for producto in self.productos:
            if producto.nombre.lower() == nombre_buscado:
                return producto

        return None

    def calcular_valor_inventario(self):
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self):
        if not self.productos:
            print("\nEl inventario está vacío.")
            return

        print("\n=== LISTADO DE PRODUCTOS ===")
        for producto in self.productos:
            print(producto)


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje).strip())
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError as error:
            print(f"Error: {error}. Introduce un número válido.")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError as error:
            print(f"Error: {error}. Introduce un número entero válido.")


def menu_principal(inventario):
    while True:
        print("\n" + "=" * 45)
        print("SISTEMA DE INVENTARIO")
        print("=" * 45)
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = pedir_float("Precio: ")
                cantidad = pedir_entero("Cantidad: ")

                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)

                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Nombre del producto a buscar: ").strip()
                producto = inventario.buscar_producto(nombre)

                if producto is None:
                    raise LookupError(f"No se encontró el producto '{nombre}'.")

                print("\nProducto encontrado:")
                print(producto)

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                valor_total = inventario.calcular_valor_inventario()
                print(
                    f"\nValor total del inventario: "
                    f"{valor_total:.2f} €"
                )

            elif opcion == "5":
                print("\nGracias por utilizar el sistema de inventario.")
                print("¡Hasta luego!")
                break

            else:
                print("Error: selecciona una opción entre 1 y 5.")

        except (TypeError, ValueError, LookupError) as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    inventario = Inventario()
    menu_principal(inventario)
