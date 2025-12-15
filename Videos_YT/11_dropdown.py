#flet --version: 0.28.2
#python --version: 3.10.6

import flet as ft

def main(page:ft.Page):
    #------Configuraciones Ventana-----------------------
    page.title = "Dropdown"
    page.window.height = 500
    page.window.width = 500

    page.window.resizable = False

    page.theme_mode = "light"

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    #----------------------------------------------------

    def changeColor(e):
        t1.value = f'El valor del dropdown es: {d1.value}'
        page.update()

    d1 = ft.Dropdown(
           label='Colores',
           hint_text='Rojo',
           options=[
               ft.dropdown.Option('Azul'),
               ft.dropdown.Option('Verde'),
               ft.dropdown.Option('Rojo'),
               ft.dropdown.Option('Amarillo')
           ],
           on_change=changeColor,
           border=ft.InputBorder.UNDERLINE,
           border_color='orange',
           label_style=ft.TextStyle(color='red')
       )
    
    t1 = ft.Text(f'El valor del dropdown es: {d1.value}')

    page.add(
       d1,
       t1
    )

ft.app(main)