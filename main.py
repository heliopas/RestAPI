from flask import Flask
import time
import serial
import socket
import subprocess


def getCOMMport(): # obtem com port arduino nano
    aux = subprocess.run(["powershell.exe", "pnputil.exe", "/enum-devices", "/connected", "/class", "'Ports'"],
                         capture_output=True)
    aux = aux.stdout.decode(encoding='utf-8', errors='strict')
    aux = aux.split('\r')
    #print(aux)

    for i in range(len(aux)):
        if "CH340" in aux[i]:
            stringCOM = aux[i]
            stringCOM = stringCOM.split(':')
            stringCOM = stringCOM[1].lstrip().removeprefix('USB-SERIAL CH340 (').removesuffix(')')
            return stringCOM

#configura porta serial
comport = serial.Serial(port=getCOMMport(), baudrate= 9600, timeout=2, stopbits= serial.STOPBITS_ONE)
comport.close()
comport.open()
#implementar detecção automatica de porta serial Arduino nano

app = Flask(__name__)

@app.route('/SetRele1')
def setRele1():
    comport.write(b"\n\r1\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele2')
def setRele2():
    comport.write(b"\n\r2\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele3')
def setRele3():
    comport.write(b"\n\r3\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele4')
def setRele4():
    comport.write(b"\n\r4\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele5')
def setRele5():
    comport.write(b"\n\r5\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele6')
def setRele6():
    comport.write(b"\n\r6\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele7')
def setRele7():
    comport.write(b"\n\r7\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/SetRele8')
def setRele8():
    comport.write(b"\n\r8\n\r")
    SerialREAD = comport.read_all()
    return SerialREAD

@app.route('/help')
def help():
    testHelp = b"----------Server options----------" \
               b"Enable/disable reles /SetRele(1-8)" \
               b"--------HQA server test!!!--------" \
               b"----------------------------------"
    return testHelp

if __name__ == '__main__':
    #get IP from hostname
    hostnamme = socket.gethostname()
    ip = socket.gethostbyname(hostnamme)
    app.run(host=ip, port=5000)