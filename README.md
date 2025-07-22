# Network Scanner & MAC Address Changer

This project includes two Python tools built using `Scapy` and `subprocess`:

- **ARP Network Scanner**: Scans a given IP or IP range for active devices.
- **MAC Address Changer**: Changes the MAC address of a given network interface.

## Requirements

- Python 3.x
- `scapy` library 

Install dependencies using:

```bash
pip install scapy
```

## Usage

### 1. ARP Network Scanner

**Command:**

```bash
sudo python3 scanner.py -t <target-ip-or-range>
```

**Example:**

```bash
sudo python3 scanner.py -t 192.168.1.1/24
```

### 2. MAC Address Changer

**Command:**

```bash
sudo python3 mac_changer.py -i <interface> -m <new-mac>
```

**Example:**

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Notes

- **Root privileges are required** to run both scripts.
- Tested on Linux systems using `ifconfig`.

## Disclaimer

Use only on networks you own or have permission to scan/change.
