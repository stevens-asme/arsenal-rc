import serial
DNT = serial.Serial('/dev/ttyUSB0')
print(DNT.name)

try:
    while(1):
        while(DNT.out_waiting <= 11):
            DNT.write(b'hello dave ')
except KeyboardInterrupt:
    DNT.close()
