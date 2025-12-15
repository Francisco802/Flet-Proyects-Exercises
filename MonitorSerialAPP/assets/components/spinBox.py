import flet as ft

class SpinBox(ft.Row):
    def __init__(self):
        super().__init__()
        self.alignment=ft.MainAxisAlignment.CENTER

        #TextField + IconButtons
        self.txt_number = ft.TextField(
            value="1", 
            text_align=ft.TextAlign.CENTER, 
            width=100,
            focused_border_color='black',
            cursor_color='black',
            color='black'
            )

        self.controls = [
            ft.IconButton(ft.Icons.REMOVE, on_click=self.minus_click,icon_color='black'),
            self.txt_number,
            ft.IconButton(ft.Icons.ADD, on_click=self.plus_click,icon_color='black'),
        ]
    
    def valor(self):
        return int(self.txt_number.value)
    
    def minus_click(self,e):
        if int(self.txt_number.value) > 1:
            self.txt_number.value = str(int(self.txt_number.value) - 1)
            self.txt_number.update()
    
    def plus_click(self,e):
        if int(self.txt_number.value) < 9:
            self.txt_number.value = str(int(self.txt_number.value) + 1)
            self.txt_number.update()