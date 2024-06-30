### GET IP ADDRESS SCRIPT

**This script retrieves the IP address of the machine it's running on and displays it on the terminal**

# REQUIREMENTS

~ `Python3`

~ `git`

-------
# CLONING

To clone this repostory, simply write this into your terminal:

    git clone https://github.com/tkemza/IPshow.git

# USAGE

~ After cloning repostory, go to the `IPshow directory` (`cd IPshow`) and type:

1. Using `Python3`:

    python3 ip.py

2. Using `Shell`:

    chmod +x ip.sh 
    bash ip.sh
    
# OUTPUT
 
~ The script will output the IP address of the machine, or `127.0.0.1` if no IP address is found.
    Output upon running this script:
        Your device ip address: [`device_ip_address`]

# Preview

![IPshow](IPshow.png)

--------
# How it Works

~ The script uses the `ip addr show` command to get a list of network interfaces and their IP addresses. It then uses `awk` and `cut` to extract the IP address from the output, and `head` to get the first IP address (in case there are multiple).

If no IP address is found, the script sets it to `127.0.0.1`.

------------
# Requirements - Tested


* This script requires the `ip` command to be available on the system.
* It has been tested on `Linux systems`, but may work on other `Unix-like` systems as well.

------------
# License

**This script is released under the `MIT License`. See the `LICENSE` file for details.**

------------
# Author

`tkemza`
