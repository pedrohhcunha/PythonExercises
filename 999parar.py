num = 0
nums = []
while True:
    num = int(input('Digite um número! [999 para parar]: '))
    if num == 999:
        break
    nums.append(num)
print('A soma dos valores digitados é {}' .format(sum(nums)))
