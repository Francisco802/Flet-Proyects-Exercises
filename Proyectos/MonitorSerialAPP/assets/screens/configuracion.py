import flet as ft
from assets.styles.estilos import style_Outlined
from assets.components.spinBox import SpinBox

class Configuracion:
    def __init__(self,manager):
        self.manager = manager
        self.dark_white="#e7e6e9"
        self.controls = [self.build()]

        self.datos = ['NNN' for i in range(9)]
        self.manager.page.session.set("sw_datos", self.datos)

    def build(self):
        return ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Configuracion", size=20,height=25),
                    self.botonesOpciones(),
                    ft.OutlinedButton(
                        'Regresar',
                        on_click=lambda _: self.manager.page.go("/switchMode"),
                        **style_Outlined
                    )
                ]
            )

    def botonesOpciones(self):
        self.numberButton = SpinBox()
        self.valorBox = ft.TextField(
            hint_text="data", 
            text_align=ft.TextAlign.CENTER, 
            width=200,
            on_blur=self.guardarDatos
            )

        return ft.Column(
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text('Numero del Boton:'),
                self.numberButton,
                ft.Text('Valor del Boton:'),
                self.valorBox,
                ft.ElevatedButton("Guardar",color='white',bgcolor='#23704A',width=100,
                                  on_click=self.guardarDatos)
            ]
        )

    def guardarDatos(self,e):
        id = self.numberButton.valor()
        dato = self.valorBox.value
        self.datos[id-1] = dato

        #print("ANTES DE GUARDAR:", self.datos)
        self.manager.page.session.set("sw_datos", self.datos)
        #print("DESPUES:", self.manager.page.session.get("sw_datos"))
        self.valorBox.value = ''
        self.manager.page.update()




#ft.Text('Valor del Boton:',color='black',width=200,text_align=ft.TextAlign.LEFT),
