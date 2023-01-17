print('Cezar Cipher Breaker')
print('Type a message encrypted with the Cezar cipher.')
mess = input('> ')

sym = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(sym)):
    translated = ''

    for symbol in mess:
        if symbol in sym:
            num = sym.find(symbol)
            num = num - i

            if num < 0:
                num = num + len(sym)

            translated = translated + sym[num]
        else:
            translated = translated + symbol

    print('Klucz #{}: {}'.format(i, translated))
