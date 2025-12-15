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
    ts = ft.TextStyle(
        color='black',
        size=24,
        font_family='Times New Roman',
        bgcolor='red',
        italic=False,
        weight=ft.FontWeight.BOLD
    )

    page.add(
        ft.Text(
            "IEEE :)",
            color='black',
            size=24,
            font_family='Times New Roman',
            bgcolor='red',
            italic=False,
            weight=ft.FontWeight.BOLD

        ),
        ft.Text("IEEE",color='black',italic=True,size=40),
        ft.Text("IEEE hola mundo!!",size=40,selectable=True,color='blue'),
        ft.Text("IEEE",color='black',size=40),
        ft.Text("IEEE",color='black',size=40,style=ts),
        ft.Text("IEEE",color='black',size=40),
        ft.Text("IEEE",size=40),
    )

ft.app(main)