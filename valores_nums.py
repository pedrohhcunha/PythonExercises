cont = 0
nums = []
op = 's'
while op == 's':
    n = int(input('Digite um número: '))
    nums.append(n)
    op = str(input('Digite [S] para continuar: ')).lower().strip()[0]
    print('_-='*10)
print('A média entre os números digitedos é {:.2f}' .format(
    sum(nums) / len(nums)))
print('O maior número é {} e o menor número é {}' .format(max(nums), min(nums)))
