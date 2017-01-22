#!/usr/bin/python3

encoded = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

shift = 2

from string import ascii_lowercase as al

trans = "".maketrans(al, al[shift:] + al[:shift])
decoded = encoded.translate(trans)
print(decoded)

with open('web', 'r') as f:
	web = f.read().strip().split('/')
web[-1] = web[-1].rstrip('html').translate(trans) + 'html'
print('/'.join(web))
