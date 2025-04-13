import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Gestión"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f1f5f9"

    articulos = []
    clientes = []
    proveedores = []
    empleados = []

    def crear_tabla(datos, columnas):
        return ft.DataTable(
            columns=[ft.DataColumn(label=ft.Text(col, weight="bold")) for col in columnas],
            rows=[
                ft.DataRow(
                    cells=[ft.DataCell(ft.Text(str(item[col]))) for col in columnas]
                ) for item in datos
            ],
            border_radius=10,
            heading_row_color="#1e293b",
            heading_text_style=ft.TextStyle(color="white", weight="bold"),
        )

    def generar_formulario(nombre_tabla, campos, dataset):
        inputs = [ft.TextField(label=campo, border_radius=10, bgcolor="#e0f2fe") for campo in campos]

        output = ft.Column()

        def actualizar_tabla():
            output.controls.clear()
            output.controls.append(crear_tabla(dataset, campos))
            page.update()

        def agregar(e):
            nuevo = {campos[i]: inputs[i].value for i in range(len(campos))}
            dataset.append(nuevo)
            actualizar_tabla()

        def eliminar(e):
            if dataset:
                dataset.pop()
                actualizar_tabla()

        def actualizar(e):
            if dataset:
                for i in range(len(campos)):
                    dataset[-1][campos[i]] = inputs[i].value
                actualizar_tabla()

        return ft.Container(
            padding=20,
            bgcolor="#ffffff",
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, color="#94a3b8", offset=ft.Offset(2, 2)),
            content=ft.Column([
                ft.Text(f"{nombre_tabla}", size=20, weight="bold"),
                ft.Row(inputs, wrap=True),
                ft.Row([
                    ft.ElevatedButton("Agregar", bgcolor="#22c55e", color="white", on_click=agregar),
                    ft.ElevatedButton("Eliminar último", bgcolor="#ef4444", color="white", on_click=eliminar),
                    ft.ElevatedButton("Actualizar último", bgcolor="#3b82f6", color="white", on_click=actualizar)
                ], spacing=10),
                output
            ])
        )
    
    articulos_tab = ft.Tab(
        text="Artículos",
        content=generar_formulario("Artículos", ["idArticulo", "Nombre", "Precio", "stock"], articulos)
    )

    clientes_tab = ft.Tab(
        text="Clientes",
        content=generar_formulario("Clientes", ["idCliente", "Nombre", "Telefono", "Tarjeta_puntos_idTarjeta_puntos"], clientes)
    )

    proveedores_tab = ft.Tab(
        text="Proveedores",
        content=generar_formulario("Proveedores", ["idProveedor", "Nombre", "Telefono", "Direccion"], proveedores)
    )

    empleados_tab = ft.Tab(
        text="Empleados",
        content=generar_formulario("Empleados", ["idEmpleado", "Nombre", "Sueldo", "Telefono", "Puesto"], empleados)
    )

    page.add(
        ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[articulos_tab, clientes_tab, proveedores_tab, empleados_tab],
            expand=1
        )
    )

ft.app(target=main)
import mysql.connector
from mysql.connector import Error 

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ortizzambrano13",
            database="tienda"
        )

        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error en la conexión: {e}")
        return None

def ver_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM articulo")
    registros = cursor.fetchall()
    for row in registros:
        print(row)
    cursor.close()

def insertar_usuario(conexion):
    nombre = input("Ingrese el nombre del usuario: ")
    edad = input("Ingrese la edad del usuario: ")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    conexion.commit()
    print("Usuario insertado correctamente")
    cursor.close()

def actualizar_usuario(conexion):
    id_usuario = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nuevo_nombre, id_usuario))
    conexion.commit()
    print("Usuario actualizado correctamente")
    cursor.close()

def eliminar_usuario(conexion):
    codigo = input("Ingrese el ID del usuario a eliminar: ")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM articulo WHERE codigo = %s", (codigo,))
    conexion.commit()
    print("Usuario eliminado correctamente")
    cursor.close()

def menu():
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos")
        return
    
    while True:
        print("\nMenú")
        print("1. Ver usuarios")
        print("2. Insertar usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ver_usuarios(conexion)
        elif opcion == "2":
            insertar_usuario(conexion)
        elif opcion == "3":
            actualizar_usuario(conexion)
        elif opcion == "4":
            eliminar_usuario(conexion)
        elif opcion == "5":
            conexion.close()
            print("Conexión cerrada. Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")
            
menu()