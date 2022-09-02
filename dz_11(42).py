# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# a. входные и выходные данные хранятся в отдельных текстовых файлах

def rle_encode(string):
    encoding = ''
    prev_char = ''
    count = 1
    for char in string:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
en = rle_encode("rrrrrrrrrrtttttttyyyyyyyy")
print(en)

def rle_decode(string):
    decode = ''
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode
de = rle_decode("10r10t8y")
print(de)

with open('rle_encode.txt', 'w', encoding='utf-8') as encode:
    encode.write(en)
with open('rle_decode.txt', 'w', encoding='utf-8') as decode:
    decode.write(de)