# start

numbers: list[int] = []
SENTINEL: int = -999
for i in range(4):
    numbers.append(0)

while True:
    try:
        number = int(input('enter a number:'))
        if numbers == SENTINEL:
            break
        for i in range(5):
            if numbers[i]:
                print('enter again')
    except IndexError:
        print('the number is incorrect')
    except ValueError:
        print('this is wrong')
print(f'the number {number} is in index {i}')

# stop
