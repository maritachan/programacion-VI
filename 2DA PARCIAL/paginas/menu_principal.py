import locale
import flet as ft
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'es_PY.UTF-8')


# ================================
# FUNCIÓN PARA SUGERENCIA DEL DÍA
# ================================
def sugerencia_del_dia_container():
    dia_semana = datetime.today().weekday()
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Patrón de entrenamientos
    tipos = ["TREN INFERIOR", "TREN SUPERIOR", "CORE / TREN MEDIO"]

    tipo_hoy = tipos[dia_semana % 3]
    tipo_manana = tipos[(dia_semana + 1) % 3]

    texto_hoy = f"{dias[dia_semana]} – Empieza la semana fuerte con {tipo_hoy.lower()} 💪"
    texto_manana = f"Mañana {dias[(dia_semana + 1) % 7]}: sugerimos {tipo_manana} para equilibrar tu rutina."

    return ft.Container(
        padding=ft.padding.all(12),
        border_radius=15,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#5B21B6", "#3B82F6"],
        ),
        content=ft.Column(
            spacing=5,
            controls=[
                ft.Text("💡 Sugerencia del Día", size=13, weight=ft.FontWeight.BOLD),
                ft.Text(texto_hoy, size=12, color=ft.Colors.WHITE),
                ft.Text(texto_manana, size=10, color=ft.Colors.WHITE70),
            ],
        ),
    )


# ================================
# PÁGINA PRINCIPAL
# ================================
def main_page(page: ft.Page, user_data):
    page.title = "MiRutina - Menú Principal"
    page.bgcolor = ft.Colors.BLACK

    # Callback: cuando cambia el nombre en el perfil
    def update_ui():
        name_display.value = f"Hola, {user_data['nombre']}" if user_data["nombre"] else "Hola, Usuario"
        page.update()

    # ======== TARJETA PRINCIPAL ========
    phone_frame = ft.Container(
        width=320,
        height=600,
        bgcolor="#0F172A",
        border_radius=ft.border_radius.all(40),
        border=ft.border.all(1, ft.Colors.WHITE24),
        padding=ft.padding.all(15),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                # PERFIL SUPERIOR
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ACCOUNT_CIRCLE_ROUNDED,
                            icon_color=ft.Colors.BLUE_400,
                            icon_size=45,
                            on_click=lambda e: page.go("/perfil"),
                        ),
                        ft.Column(
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                (name_display := ft.Text(
                                    f"Hola, {user_data['nombre']}" if user_data["nombre"] else "Hola, Usuario",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                )),
                                ft.Text(
                                    datetime.now().strftime("%A, %d de %B de %Y"),
                                    size=10,
                                    color=ft.Colors.WHITE60,
                                ),
                            ],
                        ),
                        ft.Icon(ft.Icons.NOTIFICATIONS_ROUNDED, color=ft.Colors.WHITE70),
                    ],
                ),
                ft.Divider(height=15, color=ft.Colors.WHITE12),

                # ======== SUGERENCIA DEL DÍA DINÁMICA ========
                sugerencia_del_dia_container(),

                ft.Divider(height=20, color=ft.Colors.WHITE10),
                ft.Text("¿Qué quieres enfocar hoy?", size=13, color=ft.Colors.WHITE70),

                # BOTONES DE TRENES
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    controls=[
                        ft.ElevatedButton(
                            width=80,
                            height=100,
                            bgcolor="#9333EA",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                            content=ft.Text(
                                "TREN\nINFERIOR", size=11, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD
                            ),
                            on_click=lambda e: page.go("/tren_inferior"),
                        ),
                        ft.ElevatedButton(
                            width=80,
                            height=100,
                            bgcolor="#22C55E",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                            content=ft.Text(
                                "TREN\nMEDIO", size=11, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD
                            ),
                            on_click=lambda e: page.go("/tren_medio"),
                        ),
                        ft.ElevatedButton(
                            width=80,
                            height=100,
                            bgcolor="#3B82F6",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=15)),
                            content=ft.Text(
                                "TREN\nSUPERIOR", size=11, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD
                            ),
                            on_click=lambda e: page.go("/tren_superior"),
                        ),
                    ],
                ),
                ft.Divider(height=20, color=ft.Colors.WHITE10),

                # PIE
                ft.Text(
                    "Versión 1.0 - MiRutina",
                    size=9,
                    color=ft.Colors.WHITE38,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
        ),
    )

    phone_wrapper = ft.Container(expand=True, alignment=ft.alignment.center, content=phone_frame, bgcolor=ft.Colors.BLACK)
    page.add(phone_wrapper)
    update_ui()
