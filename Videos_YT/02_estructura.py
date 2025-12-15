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
       ...
    )

ft.app(main)




# def main(page:ft.Page):
#     #------Configuraciones Ventana-----------------------
#     page.title = "Ventana"
#     page.window.height = 500
#     page.window.width = 500

#     page.window.resizable = False

#     page.bgcolor = "white"

#     page.horizontal_alignment = 'center'
#     page.vertical_alignment = 'center'
#     #----------------------------------------------------

#     page.add(
#         ft.Text("Ejemplo",color='black')
#     )

# ft.app(main)

