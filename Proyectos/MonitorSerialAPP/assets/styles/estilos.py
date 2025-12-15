import flet as ft

style_FillBtn_Green = {
    #"bgcolor": "#23704A",
    "style":ft.ButtonStyle(
                text_style=ft.TextStyle(
                    size=12,
                    #font_family="Roboto",
                    weight=ft.FontWeight.W_500
                ),
                #color='white'
            ),
    #"color":"white",
    "width":120,
    "height":30
}

style_FillBtn_Gray = {
    "bgcolor": "#CCCCCC",
    "style":ft.ButtonStyle(
                text_style=ft.TextStyle(
                    size=12,
                    #font_family="Roboto",
                    weight=ft.FontWeight.W_500
                ),
                color='black'
            ),
    #"color":"black",
    "width":120,
    "height":30
}

style_Outlined = {
    "style":ft.ButtonStyle(
                text_style=ft.TextStyle(
                    size=12,
                    #font_family="Roboto",
                    weight=ft.FontWeight.W_500
                ),
                color='#23704A'
            ),
    "width":120,
    "height":30
}

style_switch = {
    "thumb_color": {
        ft.ControlState.DEFAULT: 'white',
        ft.ControlState.SELECTED: 'white'
    },
    "active_track_color":"#247F4C",
    "inactive_track_color":'#CCCCCC',

    "label_style":ft.TextStyle(color='black')

    #"track_outline_color":'black',
}

class FilledMd1(ft.FilledButton):
    def __init__(self, texto, estilo='filled_green',on_click=None):
        super().__init__()

        estilos = {
            'filled_green':["white","#23704A"],
            'filled_gray':["black","#CCCCCC"],
        }
        modStyle = estilos.get(estilo)

        self.content=ft.Text(
            texto, 
            color=modStyle[0], 
            size=12,
            font_family='Roboto'
        )

        self.on_click=on_click

        self.bgcolor = modStyle[1]

        self.width=120
        self.height=30

class OutlinedMd1(ft.OutlinedButton):
    def __init__(self, texto,on_click=None):
        super().__init__()

        self.content=ft.Text(
            texto, 
            color="#23704A", 
            size=12,
            font_family='Roboto'
        )

        self.on_click=on_click

        self.width=120
        self.height=30
                