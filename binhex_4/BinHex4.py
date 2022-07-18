# BINHEX 4.0
# version 0.1
# input -> list of bytes: [0x1, 0x2, 0x3, 0x4]
# output -> string: binhex4.0 encoded input

from collections import deque
def load_dict(): # load binhex table

    with open("binhex_table.txt") as f:
        data = f.read()
        binhex_dict = {i:data[i] for i in range(len(data)-1)}
    return(binhex_dict)

def convert_ASCII_6(stream): # convert rle90 to ascii 6
    binhex_dict = load_dict()
    padding_bits = (len(stream) * 8) % 6
    x = ''
    for i in stream:
        x = x + f'{i:08b}'
    if padding_bits != 0:
        x = x + ''.join([str(0) for i in range(padding_bits)])
    y = []
    for i in range(0, len(x), 6):
        y.append(binhex_dict[int(x[i:i+6], 2)])
    return ''.join([str(i) for i in y])

def rle90(x): # Run Length Encoding 90
    if len(x) <= 2:
        return x
    ite = x[0]
    counter = 1
    new_x = []
    for i in range(1, len(x)):
        if ite == 0x90:
            new_x.extend([ite, 0])
            ite = x[i]
            counter = 1
            if i == (len(x) - 1):
                new_x.extend([ite, 0])
        else:
            if ite == x[i]:
                counter += 1
                if i == len(x) - 1:
                    if counter > 2:
                        new_x.extend([ite, 0x90, counter])
                    if counter == 2:
                        new_x.extend([ite, ite])
            else:
                if counter > 2:
                    new_x.extend([ite, 0x90, counter])
                if counter == 2:
                    new_x.extend([ite, ite])
                if counter == 1:
                    new_x.append(ite)              
                
                ite = x[i]
                if i == (len(x) - 1):
                    new_x.append(x[i])
            
                counter = 1

    return new_x

def binhex_enc(stream_input):
    return convert_ASCII_6(rle90(stream_input))

def main():
    inputStream = [0x1, 0x2, 0x25, 0x25, 0x25, 0x24, 0xF3, 0xF3] # input byte list
    encode_stream = binhex_enc(inputStream)
    print(encode_stream)
    
if __name__ == "__main__":
    main()

