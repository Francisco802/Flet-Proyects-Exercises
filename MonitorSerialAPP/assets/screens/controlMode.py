import flet as ft
from assets.styles.estilos import style_Outlined

class ControlMode:
    def __init__(self,manager):
        self.manager = manager
        self.controls = [self.build()]

        self.arduino = self.manager.page.session.get('arduino')

    def build(self):
        return ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Control Mode", size=20,height=50),
                    self.create_slider(),
                    ft.OutlinedButton(
                        'Regresar',
                        on_click=lambda _: self.manager.page.go("/controles"),
                        **style_Outlined
                    )
                ]
            )
    
    def create_slider(self):
        self.slide = ft.Slider(
            label="RGB",
            min=0,
            max=100,
            value=50,
            on_change=self.sliderChange,
            divisions=100,
            round=1
        )
        
        return self.slide
    
    def sliderChange(self,e):
        valor = str(int(self.slide.value))

        try:
            self.arduino.send_port("$SLD1"+valor)
        except:
            print("No estas conectado a un puerto")


    
    
        
