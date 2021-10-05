nome = input ('Qual seu nome? ')
while nome:

    salto1 = float (input ('Qual foi o valor do seu primeiro salto? '))
    salto2 = float (input ('Qual foi o valor do seu segundo salto? '))
    salto3 = float (input ('Qual foi o valor do seu terceiro salto? '))
    salto4 = float (input ('Qual foi o valor do seu quarto salto? '))
    salto5 = float (input ('Qual foi o valor do seu quinto salto? '))

    media = (salto1 + salto2 + salto3 + salto4 + salto5) / 5

    print('Resultado Final: ') 
    print('Atleta:', nome)
    print('Saltos:', salto1, '-', salto2, '-', salto3, '-', salto4, '-', salto5)
    print(f'Média dos Saltos: {media:.2f}m')

    nome = input ('Qual seu nome? ') 