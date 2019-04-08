import urllib.parse
import binascii
text = ''
while text != 'stop':
    text = input()
    out = ''
    for c in text:
        out = out + '%' + binascii.hexlify(c.encode('utf-8')).decode('utf-8')
    print(out)
