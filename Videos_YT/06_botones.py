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
    # page.theme = ft.Theme(
    #     color_scheme_seed='#247F4C',
    # )

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    #----------------------------------------------------

    def fun_ejemplo(e):
        print("works")
 
    page.add(
        ft.ElevatedButton("Button N1",on_click=fun_ejemplo),
        ft.Button("Button N11",bgcolor='red'),

        ft.FilledButton("Button N2"),
        ft.FilledTonalButton("Button N3"),
        ft.OutlinedButton("Button N4"),
        ft.TextButton("Button N5"),

        ft.FloatingActionButton("Button N6",icon=ft.Icons.ADD),
        ft.IconButton(icon=ft.Icons.HOME),

        ft.PopupMenuButton(
            icon=ft.Icons.DO_NOT_TOUCH,
            items=[
                ft.PopupMenuItem("Button M1"),
                ft.PopupMenuItem("Button M2"),
            ]
        )

    )

ft.app(main)