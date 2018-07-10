#! /bin/sh

# ENCODE
import base64
string = 'message'
data = base64.b64encode(string.encode())
print(data)

# DECODE
# import base64
# string = 'base64_string'
# data = base64.b64decode(string.decode())
# print(data)