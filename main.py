import socket

#Menu:
def menu():
    print("   ______________________________")
    print("   |        PYORT_SCANMAP        |")
    print("   |_____________________________|")
    print("   |  version: 0.4               |")
    print("   |  made by: Iago Manoel       |")
    print("   |                             |")
    print("   |  opitions:                  |")
    print("   |  scan: 1                    |")
    print("   |  see scan_historic: 2       |")
    print("   |_____________________________|")
    print(" ")

menu()
def loop():
    opition = int(input("which option will you use? "))
    
    def scan():
        #select the target:
        host = input("what is the target ? ")
        ports = [21,22,25,80,443,445,3306,5222]
        #open files to record:
        file = open("scan_historic.txt", "a+")
        file.write(f"host: {host} \n")
        
        #scaning ports(result)
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(3.0)
            code = client.connect_ex((host, port))
            if code == 0:
                print("    the port: ",port, "is open")
                file.write(f"port: {port} is open \n")
            else:
                print("    the port: ",port, "is closed")
                file.write(f"port: {port} is closed \n")
            
        file.write("\n")
        file.close()
    
    if opition == 1:
        scan()
    if opition == 2:
        file = open("scan_historic.txt", "r")
        print(file.read())
        file.close

loop()
a = "b"
while a == "b":
    again = input("want to do another scan? [y/n] ")
    if again == "y":
        loop()
    else:
        a = "c"
    