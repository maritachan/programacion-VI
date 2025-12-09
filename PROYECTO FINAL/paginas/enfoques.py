import flet as ft
from ejercicios import EJERCICIOS


def enfoques_page(page: ft.Page, tipo_tren):
    page.title = f"MiRutina - {tipo_tren.replace('_', ' ').title()}"
    page.bgcolor = ft.Colors.BLACK

    ejercicios = EJERCICIOS.get(tipo_tren, [])
    seleccionados = set()

    def toggle_selection(titulo, checkbox=None):
        if titulo in seleccionados:
            seleccionados.remove(titulo)
            if checkbox:
                checkbox.value = False
        else:
            seleccionados.add(titulo)
            if checkbox:
                checkbox.value = True
        page.update()

    # Tarjetas seleccionables
    cards = []

    for ej in ejercicios:

        # Checkbox sincronizado
        checkbox = ft.Checkbox(
            value=False,
            fill_color=ft.Colors.WHITE,
            check_color=ft.Colors.BLACK,
        )

        # Función para construir cada card con su checkbox
        def make_card(ejercicio, cb):
            def click_action(e):
                toggle_selection(ejercicio["titulo"], cb)

            return ft.Container(
                bgcolor="#9333EA" if ejercicio["titulo"] not in seleccionados else "#2563EB",
                border_radius=18,
                padding=10,
                margin=ft.margin.symmetric(vertical=4, horizontal=4),
                ink=True,
                on_click=click_action,
                shadow=ft.BoxShadow(blur_radius=8, color=ft.Colors.BLACK12),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=6,
                    controls=[
                        cb,
                        ft.Text(
                            ejercicio["titulo"],
                            size=13,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                            color=ft.Colors.WHITE,
                        ),
                    ],
                ),
            )

        checkbox.on_change = lambda e, t=ej["titulo"], c=checkbox: toggle_selection(t, c)

        cards.append(make_card(ej, checkbox))

    # GRID
    grid = ft.GridView(
        expand=True,
        runs_count=2,
        max_extent=150,
        spacing=8,
        run_spacing=8,
        controls=cards,
    )

    # Botón "Empezar"
    def empezar_rutina(e):
        if not seleccionados:
            page.snack_bar = ft.SnackBar(ft.Text("Selecciona al menos un ejercicio"))
            page.snack_bar.open = True
            page.update()
            return

        page.session.set("rutina_actual", list(seleccionados))
        from paginas.rutina import rutina_page
        rutina_page(page)

    # Marco estilo teléfono
    phone_frame = ft.Container(
        width=320,
        height=600,
        bgcolor="#0F172A",
        border_radius=40,
        border=ft.border.all(1, ft.Colors.WHITE24),
        padding=15,
        content=ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.START,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                            icon_color=ft.Colors.WHITE,
                            on_click=lambda e: page.go("/"),
                        ),
                        ft.Text(
                            tipo_tren.replace("_", " ").title(),
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                    ],
                ),
                ft.Divider(height=10, color=ft.Colors.WHITE24),
                ft.Container(expand=True, content=grid),
                ft.ElevatedButton(
                    text="Empezar",
                    bgcolor="#22C55E",
                    color=ft.Colors.WHITE,
                    height=45,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                    on_click=empezar_rutina,
                ),
            ],
        ),
    )

    page.clean()
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=phone_frame,
            bgcolor=ft.Colors.BLACK,
        )
    )
