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

    def checktxt(e):
        t1.value = f"El valor del textfield es: {tx1.value}"
        page.update()

    tx1 = ft.TextField(
           label='Nombre',
           hint_text="Makima",
           on_blur=checktxt,

        #    border=ft.InputBorder.UNDERLINE,

        #    color='red',
        #    label_style=ft.TextStyle(color='green'),

        #    focused_border_color='yellow',
        #    focus_color='purple',

        #    selection_color='blue',
        #    cursor_color='pink'
       )
    
    t1 = ft.Text(f"El valor del textfield es: {tx1.value}")

    page.add(
        tx1,
        t1,
        ft.Button("Ingresar",on_click=checktxt)
       
    )

ft.app(main)

