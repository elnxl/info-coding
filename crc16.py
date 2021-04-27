import libscrc

def crc16(data : bytearray, offset, length):
    if data is None or offset < 0 or offset > len(data) - 1 and offset + length > len(data):
        return 0

    crc = 0xFFFF
    for i in range(length):
        crc ^= data[offset + i]
        for j in range(8):
            if ((crc & 0x1) == 1):
                crc = int((crc / 2)) ^ 0xa001
            else:
                crc = int(crc / 2)
    return crc & 0xFFFF
    

surname = str(input('Enter your encoded surname: '))
#surname = '0111000000011100001000000010'
surname, surname_length = surname.encode(), len(surname)
print('surname:', surname, 'length:', surname_length)
res_1 = crc16(surname, 0, surname_length)
print('crc16 result: %x' % res_1)

res_2 = libscrc.modbus(surname)
print('calculating crc16 with imported function: %x' % res_2)

if (res_1 == res_2):
    print('WOW! same results, nice job!!!')
else:
    print('Try hard!')