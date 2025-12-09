import flet as ft

def registro_page(page: ft.Page, user_data):
    page.title = "MiRutina - Registro"
    page.bgcolor = ft.Colors.BLACK

    nombre = ft.TextField(label="Nombre", width=250)
    apellido = ft.TextField(label="Apellido", width=250)

    def continuar(e):
        if not nombre.value.strip() or not apellido.value.strip():
            page.snack_bar = ft.SnackBar(ft.Text("Completa todos los campos ⚠️"))
            page.snack_bar.open = True
            page.update()
            return

        # Guardamos los datos
        user_data["nombre"] = nombre.value.strip()
        user_data["apellido"] = apellido.value.strip()

        # Edad, peso y altura se llenan después en perfil
        user_data["edad"] = ""
        user_data["peso"] = ""
        user_data["altura"] = ""

        page.go("/menu")  # Ir al menú principal

    form = ft.Column(
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                "Registro de Usuario",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            ft.Divider(height=10, color=ft.Colors.WHITE10),
            nombre,
            apellido,
            ft.ElevatedButton(
                "Continuar",
                bgcolor="#3B82F6",
                width=200,
                on_click=continuar,
            ),
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
