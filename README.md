# Python Port Scanner 🛡️

## Project Overview
A custom network analysis tool developed in Python. This script uses raw TCP sockets to perform a "Connect Scan" on target IP addresses, identifying open ports and potential security vulnerabilities.

## Features
* **TCP Connect Scanning:** Utilizes the 3-way handshake method to verify port status.
* **Socket Timeouts:** Implements error handling to manage firewall packet drops and prevent hanging.
* **Command Line Interface:** Accepts dynamic target IPs via system arguments.

## How to Run
1.  Ensure you have Python installed.
2.  Run the command:
    ```bash
    python Scanner.py <Target_IP>
    ```
3.  Example:
    ```bash
    python Scanner.py scanme.nmap.org
    ```

## Disclaimer
This tool is for educational purposes and authorized security auditing only.
