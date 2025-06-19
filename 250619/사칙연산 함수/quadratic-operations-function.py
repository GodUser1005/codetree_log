def is_operation(o):
    if o in '+/-*':
        return True
    return False

def operate(o,a,c):
    if o == '+':
        return a + c
    elif o == '-':
        return a - c
    elif o == '*':
        return a * c
    elif o == '/':
        return a // c


a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
if is_operation(o):
   print(f"{a} {o} {c} = {operate(o,a,c)}") 
else:
    print('False')