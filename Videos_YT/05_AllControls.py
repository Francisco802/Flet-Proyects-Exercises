#flet --version: 0.28.2
#python --version: 3.10.6

import flet as ft

class Ventana:
    def __init__(self,page:ft.Page):
        self.page = page
        self.window_settings()
        
        self.page.add(self.build())
        
    def window_settings(self):
        self.page.title = "Temas y Estilos"  
        self.page.window.height = 700       # Alto |
        self.page.window.width = 1200        # Ancho __

        self.page.window.resizable = False  

        self.page.theme_mode = "light"
        # self.page.theme = ft.Theme(
        #     color_scheme_seed="#247F4C",
        #     font_family="Comic Sans MS",
        #     use_material3=False
        # )

        self.page.vertical_alignment = 'center'
        self.page.horizontal_alignment = 'center'


    def build(self):
        return ft.Row(
            expand=True,
            controls=[
                self.col_1(),
                ft.VerticalDivider(),
                self.col_2(),
                ft.VerticalDivider(),
                self.col_3(),
                ft.VerticalDivider(),
                self.col_4()
            ]
        )
    
    def col_1(self):
        def theme_change(e):
            self.page.theme_mode = "dark" if self.page.theme_mode == "light" else "light"
            self.page.update()


        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            controls=[
                ft.Text("Tipos de botones:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.ElevatedButton("btn 2"),

                ft.FilledButton("btn3"),
                ft.FilledTonalButton("btn 4"),
                ft.OutlinedButton("btn 5"),
                ft.TextButton("btn5"),

                ft.FloatingActionButton("btn6",icon=ft.Icons.ADD),
                ft.IconButton(icon=ft.Icons.THERMOSTAT),

                ft.PopupMenuButton(
                    icon=ft.Icons.HOME,
                    items=[
                        ft.PopupMenuItem("button dos"),
                        ft.PopupMenuItem("button tres"),
                        ]
                    ),
                ft.Divider(),
                ft.Text("Checkbox:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Checkbox(
                            label="Motor",
                            value=True,
                            tristate=True
                        )
                    ]
                ),
                ft.Divider(),
                ft.Text("Switch:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Switch(
                            label="Encender",
                            value=False,
                            on_change=theme_change
                        )
                    ]
                ),
                
            ]
        )
    
    def col_2(self):
        def color_theme(e,color):
            #print(c1.value)
            if len(color)==7 or color == "": 
                self.page.theme = ft.Theme(
                    color_scheme_seed=color,
                    font_family="Comic Sans MS", 
                    #font_family="Shamson Signature",

                )
                self.page.update()


        c1 = ft.TextField(
            value='#AE615B',
            label="Color",
            on_blur=lambda e: color_theme(e,c1.value)
        )

        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            controls=[
                ft.Text("RadioGroup:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.RadioGroup(
                    content=ft.Column(
                        [
                            ft.Text("Elije una opcion:"),
                            ft.Radio(label="opcion 1",value=1),
                            ft.Radio(label="opcion 2",value=2),
                            ft.Radio(label="opcion 3",value=3),
                            ft.Radio(label="opcion 4",value=4),
                        ]
                    )
                ),
                ft.Divider(),
                ft.Text("TextField:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                c1,
                ft.Divider(),
                ft.Text("Dropdown:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Dropdown(
                    label="Hola",
                    hint_text="Numeros",
                    options=[
                        ft.dropdown.Option("uno"),
                        ft.dropdown.Option("dos"),
                        ft.dropdown.Option("tres"),
                    ]
                ),
                ft.Divider(),
                ft.Text("Slider:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Slider(
                    label="{value}%",
                    min=0,
                    max=100,
                    value=50,
                    divisions=100,
                    round=1
                ),
                
            ]
        )
    
    def col_3(self):
        calendario = ft.DatePicker()
        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            controls=[
                ft.Text("ListView:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.ListView(
                    controls=[
                        ft.Text("Elemento 1"),
                        ft.Text("Elemento 1"),
                        ft.Text("Elemento 1"),
                        ft.Text("Elemento 1"),
                        ft.Text("Elemento 1"),
                    ]
                ),
                ft.Divider(),
                ft.Text("DataTable:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.DataTable(
                    #border=ft.border.all(2,'black'),
                    #border_radius=8,
                    #vertical_lines=ft.border.BorderSide(2,'black'),
                    #horizontal_lines=ft.border.BorderSide(2,'black'),
                    #heading_row_color='black',
                    #heading_row_height=30,
                    columns=[
                        ft.DataColumn(ft.Text("Id")),
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Valor"))
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("0921")),
                                ft.DataCell(ft.Text("Makima")),
                                ft.DataCell(ft.Text("24")),
                            ]
                        )
                    ]
                ),
                ft.Divider(),
                ft.Text("ProgressBar:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.ProgressBar(
                    width=400,
                ),
                ft.Divider(),
                ft.Text("ProgressRing:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.ProgressRing(
                    width=60,
                    height=60,
                    #stroke_width=2,
                ),
                ft.Divider(),
                ft.Text("Calendario:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Button("Calendario",on_click=lambda e: self.page.open(calendario))
            ]
        )
    
    def col_4(self):
        def close_dialogo(e):
            self.page.close(banner)
            self.page.update()

        banner = ft.Banner(
            leading=ft.Icon(ft.Icons.WARNING,size=40),
            content=ft.Text(
                value="Aqui se muestra la descripcion del error.",
            ),
            actions=[
                ft.TextButton(
                    text="Reintentar",
                    on_click=close_dialogo,
                ),
                ft.TextButton(
                    text="Ignorar",
                    on_click=close_dialogo,
                ),
                ft.TextButton(
                    text="Cancelar",
                    on_click=close_dialogo,
                ),
            ]
        )
        
        return ft.Column(
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=1,
            controls=[
                ft.Text("Contenedores:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("SURFACE_CONTAINER_HIGHEST",color=ft.Colors.ON_SURFACE),
                            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST   #SURFACE
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("ON_SURFACE",color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                            bgcolor=ft.Colors.ON_SURFACE
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("ON_SURFACE_VARIANT",color=ft.Colors.ON_INVERSE_SURFACE),
                            bgcolor=ft.Colors.ON_SURFACE_VARIANT
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("SURFACE_TINT",color=ft.Colors.SURFACE_CONTAINER_HIGHEST),
                            bgcolor=ft.Colors.SURFACE_TINT
                        )
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("ON_INVERSE_SURFACE",color=ft.Colors.ON_SURFACE),
                            bgcolor=ft.Colors.ON_INVERSE_SURFACE
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            width=100,
                            height=100,
                            border_radius=8,
                            content=ft.Text("INVERSE_SURFACE",color=ft.Colors.PRIMARY), #INVERSE_PRIMARY #PRIMARY_CONTAINER
                            bgcolor=ft.Colors.INVERSE_SURFACE
                        )
                    ]
                ),
                ft.Text("Banner:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Button("Banner",on_click=lambda e: self.page.open(banner)),
                ft.Divider(),
                ft.Text("Tabs:",size=14,weight='bold',width=300,text_align=ft.TextAlign.LEFT),
                ft.Tabs(
                    selected_index=1,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="First",
                            content=ft.Container(
                                content=ft.Text("1")
                            )
                        ),
                        ft.Tab(
                            text="Second",
                            content=ft.Container(
                                content=ft.Text("2")
                            )
                        )
                    ]
                ),
                
                
            ]
        )

if __name__=="__main__":
    ft.app(target=Ventana)