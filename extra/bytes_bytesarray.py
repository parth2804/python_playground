# BYTES

by = bytes([65, 66, 67, 68, 69])
print(by)
print(by[0])
print(by[1])
print(by[2])
print(by[:])
print(by[1:])
print(by[:3])
print(by[2:5])
print(by[::-1])
print(bytes([97, 98, 99]))
print(bytes([48, 49, 50]))
print(bytes([80, 89, 84, 72, 79, 78]))
print(bytes(5))

# BYTEARRAY

ba = bytearray([65, 66, 67, 68, 69])
print(ba)
print(ba[0])
print(ba[1])
print(ba[2])
print(ba[:])
print(ba[1:])
print(ba[:3])
print(ba[2:5])
print(ba[::-1])
ba[0] = 90
ba[1] = 88
ba[2] = 89
print(ba)
print(chr(ba[0]))
print(chr(ba[1]))
print(chr(ba[2]))
print(bytearray([97, 98, 99]))
print(bytearray([48, 49, 50]))
print(bytearray(5))