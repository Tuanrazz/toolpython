'''
by Tuanrazz Tool
follow https://github.com/tuanrazz
'''
import os
import time
import platform
import socket
import subprocess

def clear():
    os.system("clear")

def loading(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():
    print("\033[1;32m")
    print("╔════════════════════════════════════╗")
    print("║        TERMINAL TOOL - PYTHON     ║")
    print("║          by Tuanrazz (2025)       ║")
    print("╚════════════════════════════════════╝")
    print("\033[0m")

def system_info():
    print("\n📋 SYSTEM INFO")
    print(" OS      :", platform.system())
    print(" Release :", platform.release())
    print(" Arch    :", platform.machine())
    print(" IP Addr :", socket.gethostbyname(socket.gethostname()))
    print(" Dir     :", os.getcwd())

def realtime_clock():
    try:
        while True:
            clear()
            banner()
            print("🕒 Jam Real-Time:")
            print(time.strftime("⏰ %H:%M:%S"), end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Dihentikan oleh user.")

def ping_host():
    host = input("🌐 Masukkan host/IP: ")
    print(f"\n🔍 Pinging {host}...\n")
    os.system(f"ping -c 4 {host}")

def port_scanner():
    target = input("🎯 Masukkan IP/host target: ")
    print(f"\n🚪 Memindai port umum pada {target}...\n")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[✔] Port {port} terbuka")
        sock.close()

def show_date():
    print("📅 Tanggal Sekarang:", time.strftime("%A, %d %B %Y"))

def show_calculator():
    try:
        while True:
            expr = input("🧮 Masukkan operasi (cth: 5+2): ")
            if expr.lower() in ['exit', 'keluar']:
                break
            print("Hasil:", eval(expr))
    except Exception as e:
        print("❌ Error:", e)

def main_menu():
    while True:
        clear()
        banner()
        print("""
[1] ℹ️  Info Sistem
[2] ⏰ Jam Real-Time
[3] 🌐 Ping Host
[4] 🚪 Port Scanner
[5] 📅 Tanggal Hari Ini
[6] 🧮 Kalkulator
[7] 🔚 Keluar
""")
        pilihan = input("Pilih opsi >> ")

        if pilihan == "1":
            clear(); banner(); system_info(); input("\nEnter untuk kembali...")
        elif pilihan == "2":
            realtime_clock()
        elif pilihan == "3":
            clear(); banner(); ping_host(); input("\nEnter untuk kembali...")
        elif pilihan == "4":
            clear(); banner(); port_scanner(); input("\nEnter untuk kembali...")
        elif pilihan == "5":
            clear(); banner(); show_date(); input("\nEnter untuk kembali...")
        elif pilihan == "6":
            clear(); banner(); show_calculator(); input("\nEnter untuk kembali...")
        elif pilihan == "7":
            print("👋 Keluar..."); break
        else:
            print("❌ Pilihan tidak valid."); time.sleep(1)

if __name__ == "__main__":
    clear()
    banner()
    loading("🔧 Memuat tools Tuanrazz...", 0.03)
    main_menu()