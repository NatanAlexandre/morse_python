final = []
cod = []
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
         '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--',
         '....-', '.....', '-....', '--...', '---..', '----.', '-----']
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2',
            '3', '4', '5', '6', '7', '8', '9', '0']

print('-' * 30)
pergunta = str(input('\033[34mTradutor 2000\n'
                     '* Traduzir código Morse [1]\n'
                     '* Codificar Texto [2]\n'
                     'R: \033[m'))
print('-' * 30)
while pergunta not in '12':
    print(' ' * 6, '\033[31mOpção Inválida\033[m')
    print('-' * 30)
    pergunta = str(input('\033[34mTradutor 2000\n'
                         '* Traduzir código Morse [1]\n'
                         '* Codificar Texto [2]\n'
                         'R: \033[m'))
    print('-' * 30)
if pergunta == '1':
    texto = str(input('\033[32mDigite o código que você deseja traduzir: \033[m')).strip().lower().split()
    print('-' * 30)
    for c in texto:
        if c == morse[0]:
            cod.append('a')
        if c == morse[1]:
            cod.append('b')
        if c == morse[2]:
            cod.append('c')
        if c == morse[3]:
            cod.append('d')
        if c == morse[4]:
            cod.append('e')
        if c == morse[5]:
            cod.append('f')
        if c == morse[6]:
            cod.append('g')
        if c == morse[7]:
            cod.append('h')
        if c == morse[8]:
            cod.append('i')
        if c == morse[9]:
            cod.append('j')
        if c == morse[10]:
            cod.append('k')
        if c == morse[11]:
            cod.append('l')
        if c == morse[12]:
            cod.append('m')
        if c == morse[13]:
            cod.append('n')
        if c == morse[14]:
            cod.append('o')
        if c == morse[15]:
            cod.append('p')
        if c == morse[16]:
            cod.append('q')
        if c == morse[17]:
            cod.append('r')
        if c == morse[18]:
            cod.append('s')
        if c == morse[19]:
            cod.append('t')
        if c == morse[20]:
            cod.append('u')
        if c == morse[21]:
            cod.append('v')
        if c == morse[22]:
            cod.append('w')
        if c == morse[23]:
            cod.append('x')
        if c == morse[24]:
            cod.append('y')
        if c == morse[25]:
            cod.append('z')
        if c == morse[26]:
            cod.append('1')
        if c == morse[27]:
            cod.append('2')
        if c == morse[28]:
            cod.append('3')
        if c == morse[29]:
            cod.append('4')
        if c == morse[30]:
            cod.append('5')
        if c == morse[31]:
            cod.append('6')
        if c == morse[32]:
            cod.append('7')
        if c == morse[33]:
            cod.append('8')
        if c == morse[34]:
            cod.append('9')
        if c == morse[35]:
            cod.append('0')
        if c not in morse:
            print(f'Apenas Morse! "{c}" não é válido!')
    for c in cod:
        print(f'\033[31m{c}', end='')
    print('\033[m')
    print('-' * 30)
if pergunta == '2':
    texto = str(input('\033[32mDigite o texto a ser codificado: \033[m')).strip().lower()
    print('-' * 30)
    list(texto)
    for c in texto:
        if c == alfabeto[0]:
            cod.append(morse[0])
        if c == alfabeto[1]:
            cod.append(morse[1])
        if c == alfabeto[2]:
            cod.append(morse[2])
        if c == alfabeto[3]:
            cod.append(morse[3])
        if c == alfabeto[4]:
            cod.append(morse[4])
        if c == alfabeto[5]:
            cod.append(morse[5])
        if c == alfabeto[6]:
            cod.append(morse[6])
        if c == alfabeto[7]:
            cod.append(morse[7])
        if c == alfabeto[8]:
            cod.append(morse[8])
        if c == alfabeto[9]:
            cod.append(morse[9])
        if c == alfabeto[10]:
            cod.append(morse[10])
        if c == alfabeto[11]:
            cod.append(morse[11])
        if c == alfabeto[12]:
            cod.append(morse[12])
        if c == alfabeto[13]:
            cod.append(morse[13])
        if c == alfabeto[14]:
            cod.append(morse[14])
        if c == alfabeto[15]:
            cod.append(morse[15])
        if c == alfabeto[16]:
            cod.append(morse[16])
        if c == alfabeto[17]:
            cod.append(morse[17])
        if c == alfabeto[18]:
            cod.append(morse[18])
        if c == alfabeto[19]:
            cod.append(morse[19])
        if c == alfabeto[20]:
            cod.append(morse[20])
        if c == alfabeto[21]:
            cod.append(morse[21])
        if c == alfabeto[22]:
            cod.append(morse[22])
        if c == alfabeto[23]:
            cod.append(morse[23])
        if c == alfabeto[24]:
            cod.append(morse[24])
        if c == alfabeto[25]:
            cod.append(morse[25])
        if c == alfabeto[26]:
            cod.append(morse[26])
        if c == alfabeto[27]:
            cod.append(morse[27])
        if c == alfabeto[28]:
            cod.append(morse[28])
        if c == alfabeto[29]:
            cod.append(morse[29])
        if c == alfabeto[30]:
            cod.append(morse[30])
        if c == alfabeto[31]:
            cod.append(morse[31])
        if c == alfabeto[32]:
            cod.append(morse[32])
        if c == alfabeto[33]:
            cod.append(morse[33])
        if c == alfabeto[34]:
            cod.append(morse[34])
        if c == alfabeto[35]:
            cod.append(morse[35])
        if c not in alfabeto:
            print(f'Apenas Texto e Números de 0 a 9! "{c}" não é válido!')
    for c in cod:
        print(f'\033[31m{c} ', end='')
    print('\033[m')
    print('-' * 30)



