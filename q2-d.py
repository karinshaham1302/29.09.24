# start

nunber: int = None
try:
    number = int(input('enter a number:'))
    raise ValueError(f'the number {number} is incorrect')
except:
    print('wrong number')
print('try again')

# stop
