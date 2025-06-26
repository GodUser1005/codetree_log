binary = input()

# Please write your code here.
def bin_to_dec(binary):
    num = 0
    for bit in binary:
        num *= 2
        if int(bit) == 1:
            num += 1
    return num

print(bin_to_dec(binary))