def binaryToStr():
    inputValue = input('Masukkan bilangan binary\n\n')
    
    result = "".join([chr(int(binary, 2)) for binary in inputValue.split(" ")])
    print('\n' + result + '\n')
    awalan()

def strToBinary():
    inputValue = input('Masukkan text\n\n')
    
    result = ' '.join(format(ord(x), 'b') for x in inputValue)
    print('\n' + result + '\n')
    awalan()

def awalan():
    print('1. String / text to binary')
    print('2. Binary to string / text')
    pilihan = int(input('Pilih 1 atau 2(Tanpa tanda .)\n'))
    
    if(pilihan == 1):
        strToBinary()
    elif(pilihan == 2):
        binaryToStr()
    else:
        print('\nPilih yang bener anj\n')
        awalan()
awalan()





# result = ' '.join(format(ord(x), 'b') for x in string)
# print(result)