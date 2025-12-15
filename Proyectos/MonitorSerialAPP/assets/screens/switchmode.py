import flet as ft
from assets.styles.estilos import *

class SwitchMode:
    def __init__(self,manager):
        self.manager = manager
        self.controls = [self.build()]

        self.arduino = self.manager.page.session.get('arduino')
        print(id(self.arduino))


    def build(self):
        return ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Switch Mode", size=20, height=50),
                    self.botonesGrid(),
                    ft.Divider(height=20,color='transparent'),
                    ft.FilledButton(
                        "Configuracion",
                        **style_FillBtn_Green,
                        on_click=lambda _: self.manager.page.go("/configuracion")
                    ),
                    ft.OutlinedButton(
                        'Regresar',
                        on_click=lambda _: self.manager.page.go("/controles"),
                        **style_Outlined
                    )
                ]
            )

    def botonesGrid(self):
        self.grid = ft.GridView(
            runs_count=3,
            spacing=10,
            run_spacing=10,
            padding=10
        )

        for i in range(9):
            n=i+1
            self.grid.controls.append(
                ft.Button(
                    f"{i+1}",
                    on_click=lambda e, n=n: self.enviar(e,n),
                    bgcolor='#23704A',
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    icon=ft.Icons.POWER_SETTINGS_NEW,
                    color='white'
                )
            )
        
        return self.grid

    def enviar(self,e,id):
        datos = self.manager.page.session.get("sw_datos")
        dato = datos[id-1]

        #print(dato)

        try:
            self.arduino.send_port(dato)
        except:
            print("No estas conectado a un puerto")
        
