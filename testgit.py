#!/usr/bin/python3
# -*- coding=utf-8 -*-
#This code to study Pyhon
#QQ : 21390909
#my website:

import os
import re
print('testing git')


data = os.popen('ifconfig' + ' ens192').read()

# result = re.match('\ws*\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w*\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w.*',data)
result = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',data)
result1 = re.findall('[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}',data)

result2 = result1[0]
for ip in result:
    if ip[-1] == '0':
        mask = ip
    elif ip[-3:] == '255':
        broadcast = ip
    else:
        ipv4_ip = ip

print('%-20s : %20s' % ('Network Mask',mask))
print('%-20s : %20s' % ('Broadcast',broadcast))
print('%-20s : %20s' % ('IPv4 Addr',ipv4_ip))
print('%-20s : %20s' % ('MAC Addr',result2))