#!/usr/bin/env python

""" convert CIDR notation to wildcard mask """

print('Enter IPs with CIDR to convert to Subnet Mask (one per line):')
ip_addr = '\n'.join(iter(raw_input, ''))
ip_addr = ip_addr.split("\n")
for addr in ip_addr:
    addr = addr.replace('/32', ' 255.255.255.255')
    addr = addr.replace('/31', ' 255.255.255.254')
    addr = addr.replace('/30', ' 255.255.255.252')
    addr = addr.replace('/29', ' 255.255.255.248')
    addr = addr.replace('/28', ' 255.255.255.240')
    addr = addr.replace('/27', ' 255.255.255.224')
    addr = addr.replace('/26', ' 255.255.255.192')
    addr = addr.replace('/25', ' 255.255.255.128')
    addr = addr.replace('/24', ' 255.255.255.0')
    addr = addr.replace('/23', ' 255.255.254.0')
    addr = addr.replace('/22', ' 255.255.252.0')
    addr = addr.replace('/21', ' 255.255.248.0')
    addr = addr.replace('/20', ' 255.255.240.0')
    addr = addr.replace('/19', ' 255.255.224.0')
    addr = addr.replace('/18', ' 255.255.192.0')
    addr = addr.replace('/17', ' 255.255.128.0')
    addr = addr.replace('/16', ' 255.255.0.0')
    addr = addr.replace('/15', ' 255.254.0.0')
    addr = addr.replace('/14', ' 255.252.0.0')
    addr = addr.replace('/13', ' 255.248.0.0')
    addr = addr.replace('/12', ' 255.240.0.0')
    addr = addr.replace('/11', ' 255.224.0.0')
    addr = addr.replace('/10', ' 255.192.0.0')
    addr = addr.replace('/9', ' 255.128.0.0')
    addr = addr.replace('/8', ' 255.0.0.0')
    addr = addr.replace('/7', ' 254.0.0.0')
    addr = addr.replace('/6', ' 252.0.0.0')
    addr = addr.replace('/5', ' 248.0.0.0')
    addr = addr.replace('/4', ' 240.0.0.0')
    addr = addr.replace('/3', ' 224.0.0.0')
    addr = addr.replace('/2', ' 192.0.0.0')
    addr = addr.replace('/1', ' 128.0.0.0')
    addr = addr.replace('/0', ' 0.0.0.0')
    print addr.rstrip()
