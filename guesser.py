from random import randrange

n = randrange(1000)
while True:
    v = int(input())
    if n == v:
        print('Parabéns! Você venceu!')
        break
    print('Menor' if (n < v) else 'Maior')