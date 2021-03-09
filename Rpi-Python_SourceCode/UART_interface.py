# sudo stty -echo -F /dev/ttyS0 115200 command to change baudrate
# of com-port
# the -echo flag prevents the tty from sending back "echoing" 
# the recieved input

import serial
import logging

logging.basicConfig(filename="meter.log", level=logging.DEBUG, format="%(asctime)s:%(levelno)s:%(message)s" )


COM_PORT = "/dev/ttyS0"
BAUD_RATE = 115200
MAX_LINE_LEN = 30

def UART_Init():
    global stream
    global stream_status
    try:
        stream = serial.Serial(COM_PORT,BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        logging.error("Could not Open Serial Port.Check UART pins Connections")

def UART_Getline():
    global stream
    global stream_status

    try:
        stream_status = stream.isOpen()
        if stream_status == False:
            # print("Error: can not open Serial Stream!")
            raise serial.SerialException
    except serial.SerialException:
        logging.error("Serial Port Not Open.Check UART pins Connections")
        return 0
    
    try:
        rx = stream.readline(MAX_LINE_LEN)
    except serial.SerialTimeoutException:
        logging.error("UART Reading timed out")
        return 0

    try:
        output= rx.decode("utf-8")
    except (UnicodeDecodeError,UnicodeTranslateError):
        logging.error("Decoding Error:UART Recieved Corrupted Data")
        return 0
    else:
        return output

def UART_SendLine(line):
    global stream
    global stream_status
    if stream_status == False:
        print("Error: can not open Serial Stream!")
        return 0
    else:
        stream.write(line.encode())
        return 1

if __name__=="__main__":
    UART_Init()
    print("Listening to Serial Port...\n")
    while True:
        rx_line = UART_Getline()
        print(rx_line)
        # UART_SendLine(rx_line)

