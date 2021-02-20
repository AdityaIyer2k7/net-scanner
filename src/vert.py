import socket

def vert_scan(ip_base, startr, endr, port, timeout=0.01):
    running = []
    err = []
    for p4 in range(int(startr), int(endr)+1):
        ip = f"{ip_base}.{p4}"
        addr = (ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect(addr)
            running.append(f"{ip}:{port}")
        except Exception as e:
            err.append(str(e))
    return running, err
    

if __name__ == "__main__":
    ip = ".".join(input("IP (0.0.0): ").split(".")[:3])
    startr, endr = input("Range (0:255): ").split(":")
    port = int(input("Port: "))
    print(
        *(vert_scan(ip, startr, endr, port)[0]),
        sep = ' -> Running\n'
    )