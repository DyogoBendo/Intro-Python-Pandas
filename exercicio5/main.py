import pandas as pd

df = pd.read_fwf('usuarios.txt', header=None, names=['usuario', 'espaço utilizado'])

def byte_to_mega_byte(num):
    return round((num / (1024 * 1024)), 2)
espaco_total =df['espaço utilizado'].sum()

df['% de uso'] = round((df['espaço utilizado']* 100 /espaco_total),2)

df['espaço utilizado'] = byte_to_mega_byte(df['espaço utilizado'])

relatorio = 'ACME Inc.            Uso do espaço em disco pelos usuário\n'
relatorio += '----------------------------------------------------------\n'
relatorio += f'{"Nr.":6}{"Usuário:":20}{"Espaço utilizado:":20}{"% de uso:"}\n\n'

x = 1
for index, line in df.iterrows():    
    relatorio += f'{x:<5} {line["usuario"]:<12}{str(line["espaço utilizado"]) + " MB":>21}{line["% de uso"]:>12} %\n'
    x += 1

relatorio += '\n'
relatorio += f'Espaco total ocupado: {byte_to_mega_byte(espaco_total)} MB\n'
relatorio += f'Espaco medio ocupado: {byte_to_mega_byte(espaco_total/6)} MB\n'

print(relatorio)

with open('relatorio.txt', 'w') as arquivo:
    arquivo.write(relatorio)