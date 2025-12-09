import flet as ft
from ejercicios import EJERCICIOS_REALIZADOS

def rutina_page(page: ft.Page):
    page.title = "MiRutina - Rutina en progreso"
    page.bgcolor = ft.Colors.BLACK

    rutina = page.session.get("rutina_actual") or []
    if not rutina:
        page.snack_bar = ft.SnackBar(
            ft.Text("No hay ejercicios seleccionados.", color=ft.Colors.WHITE),
            bgcolor="#DC2626",
            open=True
        )
        page.update()
        page.go("/")
        return

    index = 0
    color_activo = "#2563EB"
    color_inactivo = "#1E293B"

    # Inputs numéricos
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
        ink=True,
    )

    seleccionado = False
    def seleccionar_ejercicio(e):
        nonlocal seleccionado
        seleccionado = not seleccionado
        ejercicio_container.bgcolor = color_activo if seleccionado else color_inactivo
        page.update()
    ejercicio_container.on_click = seleccionar_ejercicio

    # Botones
    boton_siguiente = ft.ElevatedButton(text="Siguiente ejercicio", bgcolor="#3B82F6", color=ft.Colors.WHITE, width=200)
    boton_finalizar = ft.ElevatedButton(text="Finalizar rutina", bgcolor="#22C55E", color=ft.Colors.WHITE, width=200, visible=False)

    def actualizar_boton():
        boton_siguiente.visible = index < len(rutina) - 1
        boton_finalizar.visible = index == len(rutina) - 1
        page.update()

    # Validación
    def validar_campos():
        if not series_input.value:
            return "Ingresa la cantidad de series."
        if not repeticiones_input.value:
            return "Ingresa las repeticiones."
        if not peso_input.value:
            return "Ingresa el peso utilizado."
        if not series_input.value.isdigit():
            return "Las series deben ser un número."
        if not repeticiones_input.value.isdigit():
            return "Las repeticiones deben ser un número."
        if not peso_input.value.isdigit():
            return "El peso debe ser un número."
        if int(series_input.value) == 0:
            return "Las series no pueden ser 0."
        if int(repeticiones_input.value) == 0:
            return "Las repeticiones no pueden ser 0."
        if int(peso_input.value) == 0:
            return "El peso no puede ser 0."
        return None

    # Guardar y pasar al siguiente
    def guardar_y_avanzar(e):
        nonlocal index
        error = validar_campos()
        if error:
            page.snack_bar = ft.SnackBar(ft.Text(error, color=ft.Colors.WHITE), bgcolor="#DC2626", open=True)
            page.update()
            return

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
            ejercicio_container.bgcolor = color_activo
            actualizar_boton()
            page.update()

    # Finalizar rutina
    def finalizar_rutina(e):
        nonlocal index
        error = validar_campos()
        if error:
            page.snack_bar = ft.SnackBar(ft.Text(error, color=ft.Colors.WHITE), bgcolor="#DC2626", open=True)
            page.update()
            return

        EJERCICIOS_REALIZADOS.append({
            "titulo": rutina[index],
            "series": series_input.value,
            "repeticiones": repeticiones_input.value,
            "peso": peso_input.value,
        })

        page.snack_bar = ft.SnackBar(ft.Text("Rutina finalizada ✅", color=ft.Colors.WHITE), bgcolor="#16A34A", open=True)
        page.update()
        page.go("/resumen")

    boton_siguiente.on_click = guardar_y_avanzar
    boton_finalizar.on_click = finalizar_rutina

    # Marco tipo teléfono
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
            controls=[ejercicio_container, series_input, repeticiones_input, peso_input, boton_siguiente, boton_finalizar],
        ),
    )

    actualizar_boton()
    page.clean()
    page.add(ft.Container(expand=True, alignment=ft.alignment.center, content=phone_frame, bgcolor=ft.Colors.BLACK))
