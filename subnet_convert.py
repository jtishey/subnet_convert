#!/usr/bin/env python

""" Convert between CIDR / Subnet Mask / Wildcard Mask for IPV4. """

print("\n")
print(" Subnet Convert \n")
print("1. Convert CIDR to Subnet Mask")
print("2. Convert CIDR to Wildcard Mask")
print("3. Convert Subnet Mask to CIDR")
print("4. Convert Subnet Mask to Wildcard Mask")
print("5. Convert Wildcard Mask to CIDR")
print("6. Convert Wildcard Mask to Subnet Mask")
print('')
opt_sel = raw_input('Enter your choice: ')

try:
    if opt_sel == str('1'):
        import cidr_to_mask as run_convert
    if opt_sel == str('2'):
        import cidr_to_wildcard as run_convert
    if opt_sel == str('3'):
        import mask_to_cidr as run_convert
    if opt_sel == str('4'):
        import mask_to_wildcard as run_convert
    if opt_sel == str('5'):
        import wildcard_to_cidr as run_convert
    if opt_sel == str('6'):
        import wildcard_to_mask as run_convert
    run_convert()
except:
    print('Enter 1-6')
