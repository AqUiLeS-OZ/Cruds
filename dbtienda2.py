import flet as ft

def main(page: ft.Page):
    page.title = "Gestor Tienda - Sin Conexión"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#f1f5f9"

    mensaje = ft.Text(color="red")

    # Campos y entradas por tabla
    tablas = {
        "articulo": ["idArticulo", "Nombre", "Precio", "stock"],
        "cliente": ["idCliente", "Nombre", "Telefono", "Tarjeta_puntos_idTarjeta_puntos"],
        "proveedor": ["idProveedor", "Nombre", "Telefono", "Direccion"],
        "empleados": ["idEmpleado", "Nombre", "Sueldo", "Telefono", "Puesto"]
    }

    entradas = {}
    tablas_output = {}

    def agregar(tabla):
        mensaje.value = f"Simulación de agregar en {tabla} (sin conexión)"
        mensaje.color = "green"
        page.update()

    def eliminar_ultimo(tabla):
        mensaje.value = f"Simulación de eliminar el último de {tabla} (sin conexión)"
        mensaje.color = "green"
        page.update()

    def actualizar_ultimo(tabla):
        mensaje.value = f"Simulación de actualizar el último de {tabla} (sin conexión)"
        mensaje.color = "green"
        page.update()

    # Construir pestañas
    tabs = []
    for nombre_tabla, columnas in tablas.items():
        entradas[nombre_tabla] = {col: ft.TextField(label=col, bgcolor="#f0f9ff", border_radius=10) for col in columnas}
        tablas_output[nombre_tabla] = ft.Column()
        tabs.append(
            ft.Tab(
                text=nombre_tabla.capitalize(),
                content=ft.Column([  
                    ft.Row(list(entradas[nombre_tabla].values()), wrap=True, scroll=ft.ScrollMode.ALWAYS),
                    ft.Row([ 
                        ft.ElevatedButton("Agregar", bgcolor="#22c55e", color="white", on_click=lambda e, t=nombre_tabla: agregar(t)),
                        ft.ElevatedButton("Eliminar último", bgcolor="#ef4444", color="white", on_click=lambda e, t=nombre_tabla: eliminar_ultimo(t)),
                        ft.ElevatedButton("Actualizar último", bgcolor="#3b82f6", color="white", on_click=lambda e, t=nombre_tabla: actualizar_ultimo(t)),
                    ], spacing=10),
                    tablas_output[nombre_tabla]
                ], scroll=ft.ScrollMode.ADAPTIVE, spacing=10, height=550)
            )
        )

    page.add(
        ft.Container(
            padding=20,
            bgcolor="white",
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=8, color="#94a3b8", offset=ft.Offset(2, 2)),
            content=ft.Column([ 
                ft.Text("Gestión de Base de Datos - Tienda", size=24, weight="bold"),
                mensaje,
                ft.Text("Conexión no realizada. Funciones simuladas."),
                ft.Tabs(tabs=tabs, expand=1)
            ], expand=True)
        )
    )


ft.app(target=main)
