import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN on {ip}")
        sock.close()
    except socket.error:
        print(f"[-] Cannot connect to {ip}:{port}")

def main():
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    max_threads = 100

    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")

    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target_ip, port)

if __name__ == "__main__":
    main()
