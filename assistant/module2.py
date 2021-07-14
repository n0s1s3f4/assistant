import serial
ser = serial.Serial('com4',9600);
while(1):
    a = input()

    if a == '3':
                    val = '4'
                    ser.write(val.encode())