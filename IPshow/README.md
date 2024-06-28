### Get IP Address Script

**This script retrieves the IP address of the machine it's running on and displays it on the terminal**

### Usage

To use this script, simply run it in your terminal:
    ``` 
    sh:
        python3 ip.py ('ip.py')
    or:
        chmod +x ip.sh
        bash ip.sh ('ip.sh')
    ```

### OUTPUT 
    The script will output the IP address of the machine, or `127.0.0.1` if no IP address is found.
    ```
    Output upon running this script:
        ip: [device_ip_address]
    ```

### How it Works
------------

The script uses the `ip addr show` command to get a list of network interfaces and their IP addresses. It then uses `awk` and `cut` to extract the IP address from the output, and `head` to get the first IP address (in case there are multiple).

If no IP address is found, the script sets it to `127.0.0.1`.

### Requirements
------------

* This script requires the `ip` command to be available on the system.
* It has been tested on Linux systems, but may work on other Unix-like systems as well.

### License
-------

**This script is released under the MIT License. See the `LICENSE` file for details.**

### Author
------

[tkemaz]
