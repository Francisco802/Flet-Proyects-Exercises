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

    page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Row(
                    expand=True,
                    controls=[
                        ft.Container(
                        expand=True,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.RED,
                        content=ft.Text("Etiqueta 1",color='black')
                        ),
                        ft.Container(
                        #expand=True,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.RED,
                        content=ft.Text("Etiqueta 1",color='black')
                        )
                    ]
                ),
                ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                content=ft.Text("Etiqueta 1",color='black')
                ),
                ft.Container(
                #expand=True,
                alignment=ft.alignment.center,
                bgcolor=ft.Colors.AMBER,
                content=ft.Text("Etiqueta 1",color='black')
                )
            ]
        )
    )

ft.app(main)