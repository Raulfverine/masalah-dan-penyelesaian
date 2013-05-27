# 2013-05-27: My cyberfriend shared a RE challenge on FB. So here is the answer. 
# Source: http://www.ubicrypt.hgi.rub.de/mam/content/challengess2013.bin
# SHA1: 02B57620C8850F3BCAE41B3DF8C08FA6B0B36585

"""
Please enter a challenge: Raulfverine
Please enter the solution: 307-1159790554-30163536-202697
Congratulations, you made it!
"""	

challenge = "Raulfverine"
if len(challenge) < 6: 
	print "Minimum 6 huruf"
else:
	a = 0
	for i in range(0, len(challenge)): a += ord(challenge[i])
	result = "%d-%d-%d-%d" %(ord(challenge[1]) + ord(challenge[3]) + ord(challenge[4]), int('0xffffffff', 16) - int("0xbadf000d", 16) - int('0x18', 16), ord(challenge[0]) * ord(challenge[2]) * int('0xc48', 16), (a + int('0x7b',16)) ^ int('0x31337', 16))
	print result 