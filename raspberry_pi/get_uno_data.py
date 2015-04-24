import serial

device = "/dev/ttyACM0"
try:
    print("\nTrying...", device)
    arduino = serial.Serial(device, 9600)
except:
    print("\nFailed to connect on ", device)

while True:
    data = arduino.readline()
    print("\narduino data: ", data)
