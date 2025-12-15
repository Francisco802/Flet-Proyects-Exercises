import flet as ft
from assets.styles.estilos import *

class Controles:
    def __init__(self,manager):
        self.manager = manager
        self.controls = [self.build()]


    def build(self):
        return ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Controles", size=20,height=50),
                    ft.FilledButton(
                        "Switch mode",
                        on_click=self.nav,
                        **style_FillBtn_Gray,
                        data = '/switchMode'
                    ),
                    ft.FilledButton(
                        "Control mode",
                        on_click=self.nav,
                        **style_FillBtn_Gray,
                        data = '/controlMode'
                    ),
                    ft.FilledButton(
                        "Terminal mode",
                        on_click=self.nav,
                        **style_FillBtn_Gray,
                        data = '/terminal'
                    ),
                    ft.OutlinedButton(
                        'Regresar',
                        on_click=self.nav,
                        **style_Outlined,
                        data = '/'
                    )
                ]
            )
    
    def nav(self,e):
        page = e.control.data
        self.manager.page.go(page)
        
