import flet as ft
from assets.components.arduinoConn import serialDivice
from assets.styles.estilos import *
import serial

import serial.tools
import serial.tools.list_ports

class Conexion:
    def __init__(self,manager):
        self.manager = manager
        self.arduino=serialDivice()

        self.manager.page.session.set('arduino',self.arduino)
        print(id(self.arduino))

        self.controls = [self.build()]
        self.list_puertos(None)

    def build(self):
        self._center()

        return ft.Column(
                #expand=True,
                #alignment=ft.MainAxisAlignment.SPACE_AROUND,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Configuracion de conexion", size=20,height=50),
                    ft.Text("Puertos:"),
                    self.puertosCom,
                    ft.FilledButton(
                        'Actualizar',
                        on_click=self.list_puertos,
                        **style_FillBtn_Green
                    ),
                    ft.Divider(height=10, color="transparent"),
                    ft.Text("Baudrate:"),
                    self.baudRate,
                    ft.Divider(height=10, color="transparent"),
                    self.labelSwitch,
                    self.switchConn,
                    ft.Divider(height=50, color="transparent"),
                    ft.OutlinedButton(
                        'Regresar',
                        on_click=lambda _: self.manager.page.go('/'),
                        **style_Outlined
                    )
                ]
            )

    def _center(self):
        self.puertosCom = ft.Dropdown(
            label="Puertos",
            width=200,
            options=[]
        )
    
        self.baudRate = ft.Dropdown(
            label="Baudrate",
            width=200,
            options=[
                ft.dropdown.Option("9600"),
                ft.dropdown.Option("19200"),
                ft.dropdown.Option("38400"),
                ft.dropdown.Option("57600"),
                ft.dropdown.Option("115200")
            ]
        )
        
        self.switchConn = ft.Switch(
            value=False,
            on_change=self.conn,
        )
        
        self.labelSwitch = ft.Text("Conectar")

    def list_puertos(self,e):
        puertosLista = [p.device for p in serial.tools.list_ports.comports()]
        #print(puertosLista)

        if puertosLista:
            self.puertosCom.options = [ft.dropdown.Option(puerto) for puerto in puertosLista] 
        else:
            self.puertosCom.options= [ft.dropdown.Option('No encontrados')] 

        self.manager.page.update()


    def conn(self,event):
        estado = self.switchConn.value
        puerto = self.puertosCom.value
        baudrate = self.baudRate.value

        if puerto != None and baudrate != None and puerto != 'No encontrados':
            if estado:
                self.arduino.open_port(puerto,baudrate)
                self.labelSwitch.value = "Conectado"

            else:
                self.arduino.close_port()
                self.labelSwitch.value = "Desconectado"
            
            self.manager.page.update()
        else:
            print("Error: Puertos no encontrados")
            self.switchConn.value = False
            self.labelSwitch.value = "No selecciono puerto o baudrate"
            self.manager.page.update()

        
