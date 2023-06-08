# 제너레이터

def generator_alphabet(start_letter, end_letter):
    start = ord(start_letter)
    end = ord(end_letter)

    list = []
    while start <= end:
        list.append(chr(start))
        start += 1
    return list

runner = generator_alphabet('A', 'F')

for letter in runner:
    print(letter)