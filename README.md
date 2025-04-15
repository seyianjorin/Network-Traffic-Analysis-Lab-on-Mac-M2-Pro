# Network Traffic Analysis Lab on Mac M2 Pro
 

# 🛡️ Zeek Network Monitoring Lab

## 💡 Overview
This lab demonstrates real-time network traffic monitoring and threat detection using [Zeek](https://zeek.org/), running inside a bridged Ubuntu Server VM on macOS. It's designed to simulate real-world SOC analyst workflows and lays the foundation for more advanced projects in cloud, automation, and AI-powered security.

---

## 🔧 Environment

- Host: macOS M2 Pro (2022)
- Virtualization: UTM + Ubuntu Server 24.04
- Zeek Version: 7.2.0-dev.510
- Devices: Raspberry Pi 4, iPhone, MacBook

---

## 🚀 What I Did

| Task | Description |
|------|-------------|
| VM Setup | Created and configured Ubuntu server with network bridging |
| Zeek Install | Installed and ran Zeek from source |
| Live Capture | Captured and analyzed real network traffic |
| Nmap Simulation | Simulated an attacker using `nmap -sS` and observed detection in `conn.log` |
| DNS Monitoring | Observed DNS logs including queries from iPhone and local devices |

---

## 🔍 Key Logs

- `conn.log`: Captured SYN scan attempts with `REJ` state
- `dns.log`: Passive DNS visibility showing iPhone lookups
- `packet_filter.log`: Confirmed Zeek’s filtering behavior
- `notice.log`: Placeholder for future detection scripting

---

## 📚 Skills Practiced

- Linux + Terminal workflow
- Network configuration & subnet logic
- Log analysis & threat detection
- PCAP & packet-level understanding
- IDS fundamentals with Zeek
