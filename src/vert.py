import socket

def vert_scan(ip_base, startr, endr, port, timeout=0.1):
    running = []
    for p4 in range(int(startr), int(endr)+1):
        ip = f"{ip_base}.{p4}"
        addr = (ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect(addr)
            running.append(f"{ip}:{port}")
        except Exception as e:
            print(e)
    return running
    

if __name__ == "__main__":
    ip = input("IP (0.0.0): ").split(".")[:3]
    startr, endr = input("Range (0:255): ").split(":")
    port = int(input("Port:"))
    print(
        vert_scan(ip, startr, endr, port),
        sep = '\n'
    )