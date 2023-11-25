'''
"10.0.0.0", "10.0.0.50"
the structure is
byte.byte.byte.byte

each byte can range from 00000000 to 11111111, with 256 possible combinations
in decimal representation, the addresses can range from 0.0.0.0 to 255.555.255.255

think about it as a 256 digits system
'''

def ips_between(start, end):
    decimate = lambda ip: (sum (256 ** idx * int(val) for idx, val in enumerate(ip.split(".")[::-1]) ))
    return decimate(end) - decimate(start)
