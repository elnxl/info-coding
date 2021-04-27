from scipy.linalg import hadamard
import numpy as np
import random

def hadamard_encode(data : bytearray):
    res = []
    for i in range(0, len(data), 4):
        res.append(matrix_hadamard[int(data[i:i+4],2)])
    res = np.array(res)
    return res

def hadamard_decode(data : bytearray):
    res = ''
    tmp = np.matmul(data, matrix_hadamard)
    for row in tmp:
        row[0] -= min(row)
        res += '{:04b}'.format(list(row).index(max(row)))
    return res

def make_errors(number_errors, number_block, data : bytearray):
    rand_list = random.sample(range(16), number_errors)
    print('Random elements:', *rand_list)
    for el in rand_list:
        if data[number_block][el] == 0:
            data[number_block][el] = 1
        else:
            data[number_block][el] = 0
    return data

if __name__ == '__main__':
    matrix_hadamard = np.where(hadamard(16) == 1, hadamard(16), 0)
    # print('Hadamard matrix (1 and 0): \n', matrix_hadamard)

    surname = str(input('Enter your encoded surname: '))
    # surname = '0111000000011100001000000010'

    encoded = hadamard_encode(surname.encode())
    print('Encoded: \n', encoded)
    decoded = hadamard_decode(encoded)
    print('Decoded: \n', decoded)

    if (surname == decoded):
        print('WOW! same results, nice job!!!')
    else:
        print('Try hard!')

    number_errors, number_block = int(input('Enter number of errors: ')), int(input('and block number: '))

    encoded_matrix_errors = make_errors(number_errors, number_block, encoded.copy())
    print('Encoded with {}'.format(number_errors), 'errors:\n', encoded_matrix_errors)
    decoded_matrix_errors = hadamard_decode(encoded_matrix_errors)
    print('Decoded with {}'.format(number_errors), 'errors:\n', decoded_matrix_errors)
    
    if (surname == decoded_matrix_errors):
        print('WOW! same results, nice job!!!')
    else:
        print('Try hard!')