import flet as ft
from paginas.menu_principal import main_page
from paginas.perfil import perfil_page
from paginas.enfoques import enfoques_page

# --- Datos globales del usuario ---
user_data = {
    "nombre": "",
    "apellido": "",
    "edad": "",
    "peso": "",
    "altura": "",
}

# --- Mapa de rutas ---
routes = {
    "/": lambda page: main_page(page, user_data),
    "/perfil": lambda page: perfil_page(page, user_data),
    "/tren_inferior": lambda page: enfoques_page(page, "TREN_INFERIOR"),
    "/tren_medio": lambda page: enfoques_page(page, "TREN_MEDIO"),
    "/tren_superior": lambda page: enfoques_page(page, "TREN_SUPERIOR"),
}

# --- Controlador de cambio de ruta ---
def route_change(route_event: ft.RouteChangeEvent):
    page = route_event.page
    page.clean()
    current_page = routes.get(page.route, lambda p: main_page(p, user_data))
    current_page(page)
    page.update()

# --- Función principal ---
def main(page: ft.Page):
    page.window_resizable = True
    page.bgcolor = ft.Colors.BLACK
    page.on_route_change = route_change
    page.on_view_pop = route_change
    page.go("/")  # siempre inicia en el menú principal

# --- Ejecuta la app ---
ft.app(target=main)
