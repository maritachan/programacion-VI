import flet as ft

def perfil_page(page: ft.Page, user_data):
    page.title = "MiRutina - Perfil de Usuario"
    page.bgcolor = ft.Colors.BLACK

    nombre = ft.TextField(label="Nombre", value=user_data["nombre"], width=250)
    apellido = ft.TextField(label="Apellido", value=user_data["apellido"], width=250)
    edad = ft.TextField(label="Edad", value=str(user_data["edad"]), width=250, keyboard_type=ft.KeyboardType.NUMBER)
    peso = ft.TextField(label="Peso (kg)", value=str(user_data["peso"]), width=250, keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="Altura (cm)", value=str(user_data["altura"]), width=250, keyboard_type=ft.KeyboardType.NUMBER)

    def guardar_datos(e):
        user_data["nombre"] = nombre.value
        user_data["apellido"] = apellido.value
        user_data["edad"] = edad.value
        user_data["peso"] = peso.value
        user_data["altura"] = altura.value

        page.snack_bar = ft.SnackBar(ft.Text("Datos actualizados correctamente ✅"))
        page.snack_bar.open = True
        page.update()

        # Redirige de nuevo al menú principal
        page.go("/")

    form = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("Editar Perfil de Usuario", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Divider(height=10, color=ft.Colors.WHITE10),
            nombre,
            apellido,
            edad,
            peso,
            altura,
            ft.ElevatedButton("Guardar Cambios", on_click=guardar_datos, bgcolor="#22C55E"),
            ft.TextButton("Volver al Menú", on_click=lambda e: page.go("/")),
        ],
    )

    container = ft.Container(
        width=320,
        height=600,
        padding=20,
        bgcolor="#0F172A",
        border_radius=40,
        alignment=ft.alignment.center,
        content=form,
    )

    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=container))