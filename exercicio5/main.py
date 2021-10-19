from posix import listdir
import pandas as pd
import sys, os, webbrowser
from math import inf

def byte_to_mega_byte(num):
    return round((num / (1024 * 1024)), 2)

def calcula_porcentagem_uso(espaco_utilizado, espaco_total):
    return round(((espaco_utilizado * 100) / espaco_total), 2)


def gera_cabecalho_html():
    cabecalho = "<!DOCTYPE html>\n"
    cabecalho += '<html lang="en">\n'
    cabecalho += "<head>\n"
    cabecalho += '\t<meta charset="UTF-8">\n'
    cabecalho += '\t<link rel="stylesheet" href="style.css">\n'
    cabecalho += '\t<title>Relatório</title>\n'
    cabecalho += '</head>\n'
    cabecalho += '<body>\n'

    return cabecalho

def gera_relatorio_html(df, numero_usuarios, espaco_total):    
    relatorio = gera_cabecalho_html()
    relatorio += '\t<header>\n'
    relatorio += '\t\t<h1> ACME Inc. </h1>\n'
    relatorio += '\t\t<h2> Uso do espaço em disco pelos usuários </h2>\n'
    relatorio += '\t</header>\n'    
    relatorio += '\t\t<hr>\n' 
    relatorio += '\t<table>\n'
    relatorio += '\t\t<tr>\n'
    relatorio += '\t\t\t<th> Nr. </th>\n'
    relatorio += '\t\t\t<th> Usuário </th>\n'
    relatorio += '\t\t\t<th> Espaço Utilizado </th>\n'
    relatorio += '\t\t\t<th> % de Uso </th>\n'
    relatorio += '\t\t</tr>\n'        
    
    for index, line in df.iterrows():    
        relatorio += '\t\t<tr>\n'
        if numero_usuarios:
            relatorio += f'\t\t\t<td> {index + 1} </th>\n'
            relatorio += f'\t\t\t<td> {line["usuario"]} </th>\n'
            relatorio += f'\t\t\t<td> {line["espaço utilizado"]} MB </th>\n'
            relatorio += f'\t\t\t<td> {line["% de uso"]} % </th>\n'                        
            numero_usuarios -= 1
        else:
            break
        relatorio += '\t\t</tr>\n'

    relatorio += '\t</table>\n'
    relatorio += '\n'
    relatorio += '\t<footer>\n'
    relatorio += f'\t\t<h2>Espaço total ocupado: {byte_to_mega_byte(espaco_total)} MB</h2>\n'
    relatorio += f'\t\t<h2>Espaço médio ocupado: {byte_to_mega_byte(espaco_total/6)} MB</h2>\n'
    relatorio += '\t</footer>\n'

    relatorio += '</body>\n'
    relatorio += '</html>'
    return relatorio

def gera_relatorio_txt(df, numero_usuarios, espaco_total):
    relatorio = 'ACME Inc.            Uso do espaço em disco pelos usuário\n'
    relatorio += '----------------------------------------------------------\n'
    relatorio += f'{"Nr.":6}{"Usuário:":20}{"Espaço utilizado:":20}{"% de uso:"}\n\n'    
    for index, line in df.iterrows():    
        if numero_usuarios:
            relatorio += f'{index+1:<5} {line["usuario"]:<12}{str(line["espaço utilizado"]) + " MB":>21}{line["% de uso"]:>12} %\n'            
            numero_usuarios -= 1
        else:
            break

    relatorio += '\n'
    relatorio += f'Espaco total ocupado: {byte_to_mega_byte(espaco_total)} MB\n'
    relatorio += f'Espaco medio ocupado: {byte_to_mega_byte(espaco_total/6)} MB\n'
    return relatorio

def gera_relatorio(df, numero_usuarios, espaco_total, tipo):    
    if tipo == 0:
        relatorio = gera_relatorio_html(df, numero_usuarios, espaco_total)
        with open('index.html', 'w') as arquivo:
            arquivo.write(relatorio)                
        webbrowser.open(url="index.html", new=1)
    else:
        relatorio = gera_relatorio_txt(df, numero_usuarios, espaco_total)
        with open('relatorio.txt', 'w') as arquivo:
            arquivo.write(relatorio)        
        webbrowser.open(url="relatorio.txt", new=1)

if __name__ == "__main__":
    
    argv = list(map(int, sys.argv[1:]))
    
    tipo = 0
    ordem = True
    numero_usuarios = inf

    if len(argv) >= 1:
        tipo = argv[0]

        if len(argv) >= 2:        
            ordem = False if argv[1] else True

        if len(argv) == 3:
            numero_usuarios = argv[2]


    df = pd.read_fwf('usuarios.txt', header=None, names=['usuario', 'espaço utilizado'])
    espaco_total= df['espaço utilizado'].sum()

    df['% de uso'] = calcula_porcentagem_uso(espaco_utilizado=df["espaço utilizado"], espaco_total=espaco_total)
    df['espaço utilizado'] = byte_to_mega_byte(df['espaço utilizado'])

    df = df.sort_values('% de uso', ascending=ordem)  # ordenando pelo percentual de uso

    gera_relatorio(df, numero_usuarios, espaco_total, tipo)
        