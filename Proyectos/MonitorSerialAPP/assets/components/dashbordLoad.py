# import flet as ft
# import math

# from mod import VerticalMenu
# from mod1 import MainContentColumn
# from mod2 import SidebarColumn

# class home:
#     def __init__(self,manager):
#         self.manager = manager
#         pantallas = (VerticalMenu,MainContentColumn,SidebarColumn)

#         # for F in pantallas:
#         #     frame = F()
#         #     component = frame.build()
#         #     controls.append(component)
            
#         controls = [F(self.manager).build() for F in pantallas]

#         self.controls = [
#             ft.Container(
#                 expand=True,
#                 bgcolor=self.manager.bg_color,  # Usa el color del gestor principal
#                 content=ft.Row(
#                     expand=True,
#                     controls=controls
#                 )
#             )
#         ]