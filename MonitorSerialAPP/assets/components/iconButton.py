import flet as ft

class home:
    def __init__(self,manager):
        self.manager = manager
        self.dark_white="#e7e6e9"
        self.controls = [self.build()]

    def build(self):
        return ft.Container(
            expand=True,
            #bgcolor=ft.Colors.AMBER,
            #padding=ft.padding.only(bottom=100),
            alignment=ft.alignment.center,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Menu principal", color="black", size=22,font_family='Roboto'),
                    ft.Container(expand=True),
                    self._center2(),
                    ft.Container(expand=True),
                ]
            )
        )
    
    # def _icon_container(self, txt, icon, cmd):
    #     return ft.Container(
    #         width=90,
    #         height=35,
    #         border_radius=10,
    #         bgcolor=self.dark_white,
    #         alignment=ft.alignment.center,
    #         content=ft.Column(
    #             alignment=ft.MainAxisAlignment.CENTER,
    #             horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # más claro
    #             spacing=0,  # Espacio entre ícono y texto
    #             controls=[
    #                 ft.IconButton(
    #                     icon=icon,
    #                     icon_color="black",
    #                     on_click=lambda _: self.manager.navigate(cmd),
    #                     style=ft.ButtonStyle(padding=0),  # quita relleno si hay mucho
    #                 ),
    #                 ft.Text(txt, color="black", size=12, weight='bold')
    #             ]
    #         )
    #     )
    
    def crear_boton(self,texto, color_fondo, cmd):
        return ft.Button(
            content=ft.Text(texto, color="#FFFFFF", size=12),
            bgcolor=color_fondo,
            on_click=lambda _: self.manager.navigate(cmd),
            width=100,
            height=30,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=7),
            )
        )

    def _center(self):
        icons = [
            ft.Icons.MENU_SHARP,
            ft.Icons.LIGHT_ROUNDED,
            ft.Icons.MUSIC_NOTE,
            ft.Icons.THERMOSTAT,
            ft.Icons.SECURITY
        ]

        return ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                #vertical_alignment=ft.alignment.center,
                expand=True,
                controls=[
                    self._icon_container(txt='Opcion 1',icon=icons[0],cmd="/"),
                    self._icon_container(txt='Opcion 2',icon=icons[1],cmd="/"),
                ]
            )
    
    def _center3(self):
        return ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                #vertical_alignment=ft.alignment.center,
                expand=True,
                controls=[
                    self.crear_boton("ACEPTAR", "#23704A", "/"),
                    ft.Container(width=10),
                    self.crear_boton("CANCELAR", "#AA3333","/" )
                ]
            )
    
    # def _center2(self):
    #     return ft.Container(
    #             #bgcolor=ft.Colors.RED_100,
    #             #expand=True,
    #             content=ft.Column(
    #                 #expand=True,
    #                 #alignment=ft.MainAxisAlignment.CENTER,
    #         controls=[
    #             self._center3(),
    #             self._center3(),
    #             self._center3(),
    #             self._center3(),
    #             self._center3(),
    #         ]
    #     )
    #     )