def soma(a: int, b: int, c: int) -> int:
    """
    Retorna a soma de três números inteiros!
    """
    return a + b + c

if __name__ == '__main__':
    a, b, c = map(int, input("Por favor insira 3 valores, separados por espaço\nExemplo: 2 6 12\nInsira aqui: ").split())
    s = soma(a=a, b=b, c=c)
    print(f"O resultado da soma desses três números é: {s}")

