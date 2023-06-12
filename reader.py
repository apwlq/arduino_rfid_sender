import serial
import threading
import time
import serial.tools.list_ports
import platform

baud = 9600
ser = None

def find_serial_port():
    system = platform.system()
    if system == 'Windows':
        return find_windows_serial_port()
    elif system == 'Linux':
        return find_linux_serial_port()
    else:
        print("Unsupported operating system.")
        return None

def find_windows_serial_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if port.device.startswith("COM"):
            return port.device
    return None

def find_linux_serial_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "tty" in port.device:
            return "/dev/" + port.device
    return None

def main():
    global ser
    port = find_serial_port()
    if port is None:
        print("No serial port found.")
        return

    ser = serial.Serial(port, baud, timeout=1)

    thread = threading.Thread(target=serial_read, args=(ser,))
    thread.start()

    while True:
        ser.read(ser.inWaiting())
        time.sleep(1)

    ser.close()

def serial_read(ser):
    while True:
        data = ser.readline()
        if len(data) > 0:
            data_str = data.replace(b'\r\n', b'')
            print(data_str.decode('utf-8'))

main()
