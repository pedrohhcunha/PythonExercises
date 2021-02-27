num = int(input('Digite um numero: '))
print('A tabuada deste numero é: ')
for c in range(1, 11):
    print('{:2} X {:2} = {:2}' .format(num, c, num*c))
