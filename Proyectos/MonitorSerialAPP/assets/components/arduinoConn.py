import serial
import time


class serialDivice():
    def __init__(self):
        self.divice=serial.Serial()
        self.data=[]

    def open_port(self,puerto,baud):
        if(puerto!="No encontrados"):
            self.divice.baudrate=baud 
            self.divice.port=puerto 
            self.divice.open()
            time.sleep(1)
            print("Conectado.")

    def close_port(self):
        self.divice.close()
        time.sleep(1)
        print("Desconectado.")

    def send_port(self,sms):
        mensaje=sms + "\n"
        self.divice.write(mensaje.encode("ascii"))

    def read_port(self):
        if(self.divice.is_open):
            self.divice.flushInput()
            lectura = self.divice.readline().decode().strip()
            self.data = lectura.split(",")
        

        
