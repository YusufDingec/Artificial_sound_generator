import serial
import socket

ser = serial.Serial(
    # Serial port to read the data from
    port='COM4',

    # Rate at which the information is shared
    baudrate=9600,

    # Applying parity check
    parity=serial.PARITY_NONE,

    # Pattern of bits to read
    stopbits=serial.STOPBITS_ONE,

    # Total number of bits to read
    bytesize=serial.EIGHTBITS,

    # Number of serial commands to accept before timing out
    timeout=1
)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", 5052)

while True:
    global right
    global left
    for i in range(0, 2):
        x = ser.readline().decode("utf")
        if x[0:5] == "sag: ":
            right_vel = round((int(x[5:])/1023)*30)
            right = str(right_vel)

        else:
            left_vel = round((int(x[5:])/1023)*30)
            left = str(left_vel)

    message = right + "," + left
    print(message)
    sock.sendto(str.encode(message), address)
