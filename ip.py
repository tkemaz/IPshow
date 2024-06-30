import socket
import os
import time

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip_address = s.getsockname()[0]
    except Exception:
        ip_address = '127.0.0.1'
    finally:
        s.close()
    return ip_address

def clear():
    os.system('clear')

def main():
    # ASCII Colors
    RESET = "\033[0m" 
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    clear()
    time.sleep(1)
    print(f"""{CYAN}
  ___ ____      _                    
 |_ _|  _ \ ___| |__   _____      __ 
  | || |_) / __| '_ \ / _ \ \ /\ / / 
  | ||  __/\__ \ | | | (_) \ V  V /  
 |___|_|   |___/_| |_|\___/ \_/\_/   
                                     
  {RESET}""")
    print(" ")
    print(f"Your device ip address: {YELLOW}{get_ip_address()}{RESET}")

if __name__ == '__main__':
    main()
