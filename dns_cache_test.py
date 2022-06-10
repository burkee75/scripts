# run this script to test DNS cache values. Answer should change with the TTL of the record.

import socket
import logging
import time

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

# enter the DNS record you are curious about here
url = "isitdns.com"

message = 

timer = 0
while time < 120:
    response = socket.gethostbyname(url)
    logging.debug(f"Resolving {url}: {response}")
    timer += 1
    time.sleep(1)
  
