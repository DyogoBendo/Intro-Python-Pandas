from random import randint

if __name__ == '__main__':
    dados = [[0, []] for _ in range(6)]

    for i in range(1, 101):
        lancamento = randint(1, 6)
        dados[lancamento - 1][0] += 1
        dados[lancamento - 1][1].append(str(i))
    
    for d in range(6):
        print(f"O valor {d + 1} apareceu em {dados[d][0]} lançamentos -> {', '.join(dados[d][1])}")
    