import serial
import threading
import time

port = "COM7"
baud = 9600
ser = serial.Serial(port, baud, timeout=1)

def main():
    thread = threading.Thread(target=serial_read, args=(ser,))
    thread.start()

    while True:
        ser.read(ser.inWaiting())
        time.sleep(1)



def serial_read(ser):
    while True:
        data = ser.readline()
        if len(data) > 0:
            str = data.replace(b'\r\n', b'')
            print(str.decode('utf-8'))

    ser.close()
main()
