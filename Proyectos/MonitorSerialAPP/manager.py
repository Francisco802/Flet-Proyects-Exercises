import flet as ft
from assets.screens.home import Home
from assets.screens.conexion import Conexion
from assets.screens.controles import Controles
from assets.screens.switchmode import SwitchMode
from assets.screens.configuracion import Configuracion
from assets.screens.controlMode import ControlMode

class Ventana:
    def __init__(self,page:ft.Page):
        self.page = page
        self.window_settings()

        self.build_views()
        self.page.on_route_change = self.route_change
        self.page.go("/")  # Carga la primera página (Home)

    def window_settings(self):
        self.page.title = "Monitor Serial"
        self.page.window.height = 550       # Alto |
        self.page.window.width = 350        # Ancho __

        self.page.window.resizable = False  

        self.page.theme_mode = "light"
        self.page.theme = ft.Theme(
            color_scheme_seed='#247F4C',
            font_family= 'Roboto'
        )

        self.page.vertical_alignment = 'center'
        self.page.horizontal_alignment = 'center'

    def build_views(self):
        self.vistas = {
            "/":Home(self),
            "/conexion":Conexion(self),
            "/controles":Controles(self),
            "/switchMode":SwitchMode(self),
            "/configuracion":Configuracion(self),
            "/controlMode":ControlMode(self)
        }

    def route_change(self, route):
        self.page.views.clear()
        current_view = self.vistas.get(self.page.route)

        try:
            self.page.views.append(
                ft.View(
                    route,
                    #vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=current_view.controls,
                )
            )
        except:
            print("Error de clase o ruta")
            self.page.go("/")
        
        self.page.update()
        #print("----Actual----",self.page.views)

if __name__=="__main__":
    ft.app(target=Ventana)
