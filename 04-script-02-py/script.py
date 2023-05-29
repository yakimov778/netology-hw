import socket
import time

service_addr = {
    'drive.google.com': '0',
    'mail.google.com': '0',
    'google.com': '0'
}


for item in service_addr:
    initial_addr = socket.gethostbyname(item)
    service_addr[item] = initial_addr

while True:

    for item in service_addr:
        old_addr = service_addr[item]
        new_addr = socket.gethostbyname(item)
        if new_addr != old_addr:
            service_addr[item] = new_addr
            print("[ERROR] "+item+" IP mismatch: old IP "+old_addr+", new IP "+new_addr)
        print(item + " - " + service_addr[item])
    print("***")
    time.sleep(5)