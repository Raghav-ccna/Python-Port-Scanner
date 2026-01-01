import socket
import sys
from datetime import datetime

# 1. Define the target
# We accept the target IP as an argument (e.g., python scanner.py 192.168.1.1)
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # 2. Loop through ports (Standard range is 1-65535, but let's do 1-1000 for speed)
    for port in range(50, 85):  
        
        # 3. Create the socket
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so it doesn't hang on a filtered port (1 second)
        s.settimeout(1)
        
        # 4. Attempt to connect
        # connect_ex returns 0 if the connection was successful, error code otherwise
        result = s.connect_ex((target, port)) 
        
        if result == 0:
            print(f"Port {port} is OPEN")
            
        # 5. Close the connection to free up resources
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()