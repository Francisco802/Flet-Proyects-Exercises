import flet as ft
from assets.styles.estilos import *

class Home:
    def __init__(self,manager):
        self.manager = manager
        self.controls = [self.build()]

    def build(self):
        return ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Menu principal", size=24),
                    ft.Divider(height=40, color="transparent"),
                    ft.FilledButton(
                        "Conexion",
                        on_click=self.nav,
                        **style_FillBtn_Green,
                        data="/conexion"
                    ),
                    ft.FilledButton(
                        "Controles",
                        on_click=self.nav,
                        **style_FillBtn_Green,
                        data="/controles"
                    ),
                    ft.FilledButton(
                        "Vizualizar",
                        on_click=self.nav,
                        **style_FillBtn_Green,
                        data="/"
                    ),
                    ft.FilledButton(
                        "Informacion",
                        on_click=self.nav,
                        **style_FillBtn_Green,
                        data="/"
                    ),
                    ft.Divider(height=120, color="transparent"),
                    ft.OutlinedButton(
                        'Salir',
                        on_click=lambda _: self.manager.page.window.close(),
                        **style_Outlined
                    )
                ]
            )

    def nav(self,e):
        page = e.control.data
        self.manager.page.go(page)
        
        


