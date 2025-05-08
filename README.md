# Zeek Network Monitoring Lab

## Overview

This project demonstrates real-time network traffic monitoring and threat detection using [Zeek](https://zeek.org/) on an Ubuntu Server VM, bridged into a live network using UTM on macOS. The goal is to simulate an enterprise-level Security Operations Center (SOC) detection workflow.

---

##  Environment Setup

- **Host Machine:** MacBook Pro (M2, 2022)
- **Virtualization:** [UTM](https://mac.getutm.app/) running Ubuntu Server 24.04 LTS
- **Monitoring Tool:** Zeek IDS (compiled from source)
- **Network Mode:** Bridged to host Wi-Fi (ensures VM is on the same subnet as physical devices)
- **Client Devices:** Raspberry Pi 4, MacBook Pro, iPhone

---

## Simulated Traffic & Detection Scenarios

| Simulation | Description |
|------------|-------------|
| `nmap` Port Scan | Ran SYN scan from MacBook to VM using `nmap -sS` |
| iPhone Traffic | Captured multicast DNS & Bonjour lookups from iPhone |
| Live DNS Queries | Detected passive DNS activity across devices |
| ICMP Echo | Verified network visibility using `ping` from/to Raspberry Pi |
| Zeek Live Capture | Monitored real-time traffic on `enp0s1` interface via `sudo zeek -i enp0s1` |

---

## Project Contents

```bash
Network-Traffic-Analysis-Lab-on-Mac-M2-Pro/
├── screenshots/
│   ├── Nmap port scan via terminal
│   ├── python script created for automated log sanitization and fetching
│   └── Ubuntu VM running on UTM
├── README.m # This file
├── Sanitize_and_fetch.py # automation script to fetch the latest conn.log file and sanitize it by redacting IP address and other unwanted data. 
├── final_conn.log # Redacted connection log
