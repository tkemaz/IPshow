#!/bin/sh

get_ip_address() {
  ip_address=$(ip addr show | awk '/inet / {print $2}' | cut -d/ -f1 | head -1)
  if [ -z "$ip_address" ]; then
    ip_address="127.0.0.1"
  fi
  echo "$ip_address"
}

echo "ip: $(get_ip_address)" # Print ip address to the terminal