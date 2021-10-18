import pandas as pd

df = pd.read_fwf('./usuarios.txt', header=None, names=['usuario', 'espaço utilizado'])

def byte_to_mega_byte(num):
    return round((num / (1024 * 1024)), 2)
espaco_total =df['espaço utilizado'].sum()

df['% de uso'] = round((df['espaço utilizado']* 100 /espaco_total),2)

df['espaço utilizado'] = byte_to_mega_byte(df['espaço utilizado'])
print(df)

relatorio = ('ACME Inc.            Uso do espaço em disco pelos usuário\n')
relatorio += ('----------------------------------------------------------\n')
relatorio += ('Nr. Usuário:      Espaço utilizado:       % de uso:\n')

x = 1
for index, line in df.iterrows():
    print(line)
    relatorio += f'{x} {line["usuario"]} \t {line["espaço utilizado"]} MB \t {line["% de uso"]} %\n'
    x= x+1

relatorio += '\n'
relatorio += f'Espaco total ocupado: {byte_to_mega_byte(espaco_total)} MB\n'
relatorio += f'Espaco medio ocupado: {byte_to_mega_byte(espaco_total/6)} MB\n'

with open('relatorio.txt', 'w') as arquivo:
    arquivo.write(relatorio)