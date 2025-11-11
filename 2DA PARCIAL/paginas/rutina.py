import flet as ft
from ejercicios import EJERCICIOS_REALIZADOS

def rutina_page(page: ft.Page):
    page.title = "MiRutina - Rutina en progreso"
    page.bgcolor = ft.Colors.BLACK

    rutina = page.session.get("rutina_actual") or []
    index = 0  # posición actual
    color_activo = "#2563EB"
    color_inactivo = "#1E293B"

    # Inputs
    series_input = ft.TextField(label="Series realizadas", width=150, text_align=ft.TextAlign.CENTER)
    repeticiones_input = ft.TextField(label="Repeticiones por serie", width=150, text_align=ft.TextAlign.CENTER)
    peso_input = ft.TextField(label="Peso utilizado (kg)", width=150, text_align=ft.TextAlign.CENTER)

    # Texto del ejercicio
    titulo = ft.Text(rutina[index], size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    # Contenedor clickeable
    ejercicio_container = ft.Container(
        bgcolor=color_activo,
        border_radius=20,
        padding=15,
        content=titulo,
        alignment=ft.alignment.center,
        width=250,
        ink=True,  # permite clic con efecto visual
    )

    seleccionado = False

    def seleccionar_ejercicio(e):
        nonlocal seleccionado
        seleccionado = not seleccionado
        ejercicio_container.bgcolor = "#2563EB" if seleccionado else "#1E293B"
        page.update()

    ejercicio_container.on_click = seleccionar_ejercicio


    # Botones
    boton_siguiente = ft.ElevatedButton(
        text="Siguiente ejercicio",
        bgcolor="#3B82F6",
        color=ft.Colors.WHITE,
        width=200,
    )
    boton_finalizar = ft.ElevatedButton(
        text="Finalizar rutina",
        bgcolor="#22C55E",
        color=ft.Colors.WHITE,
        width=200,
        visible=False
    )

    def actualizar_boton():
        boton_siguiente.visible = index < len(rutina) - 1
        boton_finalizar.visible = index == len(rutina) - 1
        page.update()

    def guardar_y_avanzar(e):
        nonlocal index
        EJERCICIOS_REALIZADOS.append({
            "titulo": rutina[index],
            "series": series_input.value,
            "repeticiones": repeticiones_input.value,
            "peso": peso_input.value,
        })
        series_input.value = ""
        repeticiones_input.value = ""
        peso_input.value = ""

        if index < len(rutina) - 1:
            index += 1
            titulo.value = rutina[index]
            ejercicio_container.bgcolor = color_activo  # reset color al siguiente
            actualizar_boton()
            page.update()

    def finalizar_rutina(e):
        EJERCICIOS_REALIZADOS.append({
            "titulo": rutina[index],
            "series": series_input.value,
            "repeticiones": repeticiones_input.value,
            "peso": peso_input.value,
        })
        page.snack_bar = ft.SnackBar(ft.Text("Rutina finalizada ✅"))
        page.snack_bar.open = True
        page.update()
        page.go("/")

    boton_siguiente.on_click = guardar_y_avanzar
    boton_finalizar.on_click = finalizar_rutina

    phone_frame = ft.Container(
        width=320,
        height=600,
        bgcolor="#0F172A",
        border_radius=40,
        border=ft.border.all(1, ft.Colors.WHITE24),
        padding=20,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ejercicio_container,
                series_input,
                repeticiones_input,
                peso_input,
                boton_siguiente,
                boton_finalizar,
            ],
        ),
    )

    actualizar_boton()
    page.clean()
    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=phone_frame, bgcolor=ft.Colors.BLACK))
