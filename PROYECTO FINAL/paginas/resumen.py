import flet as ft
from datetime import datetime
from ejercicios import EJERCICIOS_REALIZADOS

def resumen_page(page: ft.Page):
    page.title = "MiRutina - Resumen de la rutina"
    page.bgcolor = ft.Colors.BLACK

    if not EJERCICIOS_REALIZADOS:
        page.snack_bar = ft.SnackBar(
            ft.Text("No hay ejercicios realizados.", color=ft.Colors.WHITE),
            bgcolor="#DC2626",
            open=True
        )
        page.update()
        return

    # Fecha de realización
    fecha_actual = datetime.now().strftime("%d/%m/%Y - %H:%M")

    # Encabezado del resumen
    titulo_resumen = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=3,
        controls=[
            ft.Text(
                "Resumen de la Rutina",
                size=22,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE
            ),
            ft.Text(
                f"Fecha: {fecha_actual}",
                size=14,
                color=ft.Colors.WHITE70
            ),
        ]
    )

    # Crear tarjetas con datos de ejercicios
    ejercicios_controls = []
    for i, ex in enumerate(EJERCICIOS_REALIZADOS, start=1):
        ejercicios_controls.append(
            ft.Container(
                bgcolor="#1E293B",
                padding=15,
                border_radius=15,
                width=280,
                border=ft.border.all(1, ft.Colors.WHITE12),
                shadow=ft.BoxShadow(color=ft.Colors.WHITE12, blur_radius=10, offset=ft.Offset(2, 2)),
                content=ft.Column(
                    spacing=5,
                    controls=[
                        ft.Text(f"{i}. {ex['titulo']}", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(f"Series: {ex['series']}", color=ft.Colors.WHITE70),
                        ft.Text(f"Repeticiones: {ex['repeticiones']}", color=ft.Colors.WHITE70),
                        ft.Text(f"Peso: {ex['peso']} kg", color=ft.Colors.WHITE70),
                    ]
                )
            )
        )

    # Botón de regreso al menú
    boton_volver = ft.ElevatedButton(
        text="Volver al menú principal",
        bgcolor="#3B82F6",
        color=ft.Colors.WHITE,
        width=250,
        height=50,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            elevation=5,
            overlay_color={"hovered": ft.Colors.BLUE_ACCENT},  # compatible
        ),
        on_click=lambda e: page.go("/menu")
    )

    # Frame tipo teléfono
    phone_frame = ft.Container(
        width=320,
        height=600,
        bgcolor="#0F172A",
        border_radius=40,
        border=ft.border.all(1, ft.Colors.WHITE24),
        padding=20,
        content=ft.Column(
            scroll="auto",
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[titulo_resumen] + ejercicios_controls + [boton_volver]
        )
    )

    page.clean()
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,
            content=phone_frame,
            bgcolor=ft.Colors.BLACK
        )
    )
