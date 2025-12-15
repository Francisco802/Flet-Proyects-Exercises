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

    def checkRadio(e):
        t1.value = f"La opcion seleccionada es: {r1.value}"
        page.update()

    r1 = ft.RadioGroup(
           content=ft.Column(
               [
                   ft.Text('Elije una opcion:'),
                   ft.Radio(label="opcion 1", value=1),
                   ft.Radio(label="opcion 2", value=2),
                   ft.Radio(label="opcion 3", value=3),
                   ft.Radio(label="opcion 4", value=4)
               ]
           ),
           on_change=checkRadio
       )
    
    t1 = ft.Text(f"La opcion seleccionada es: {r1.value}")
    

    page.add(
       ft.Row(
           alignment='center',
           controls=[r1]
       ),
       t1
    )

ft.app(main)
