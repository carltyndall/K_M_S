data = bytearray(b"cat")
data[0] = ord("b")
print("mutable bytes:", data.decode())