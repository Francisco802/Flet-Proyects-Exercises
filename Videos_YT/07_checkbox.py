#flet --version: 0.28.2
#python --version: 3.10.6

import flet as ft

def main(page:ft.Page):
    #------Configuraciones Ventana-----------------------
    page.title = "Ventana"
    page.window.height = 500
    page.window.width = 500

    page.window.resizable = False

    page.theme_mode = "light"

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    #----------------------------------------------------
    def check_test(e):
        t1.value = f"El valor del checkbox es: {c1.value}"
        page.update()

    c1 = ft.Checkbox(
           label="Motor",
           value=False,
           tristate=True,
           on_change=check_test
       )
    
    t1 = ft.Text(f"El valor del checkbox es: {c1.value}")

    page.add(
       ft.Row(
           alignment=ft.MainAxisAlignment.CENTER,
           controls=[c1]
       ),
       t1
    )

ft.app(main)