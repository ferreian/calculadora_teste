"""
Calculadora simples em Python
Suporta: soma, subtração, multiplicação, divisão, potência, raiz quadrada e módulo.
"""

import math


def obter_numero(mensagem):
    """Solicita e retorna um número válido ao usuário."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")


def obter_numero_positivo(mensagem):
    """Solicita e retorna um número positivo (para raiz quadrada)."""
    while True:
        n = obter_numero(mensagem)
        if n >= 0:
            return n
        print("Para raiz quadrada, o número deve ser não negativo.")


def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def potencia(base, expoente):
    return base ** expoente


def raiz_quadrada(n):
    if n < 0:
        raise ValueError("Não existe raiz quadrada real de número negativo.")
    return math.sqrt(n)


def modulo(a, b):
    if b == 0:
        raise ValueError("Não é possível calcular módulo com divisor zero.")
    return a % b


def menu():
    print("\n" + "=" * 40)
    print("         CALCULADORA SIMPLES")
    print("=" * 40)
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (^)")
    print("6. Raiz quadrada (√)")
    print("7. Módulo (resto da divisão %)")
    print("0. Sair")
    print("=" * 40)


def main():
    while True:
        menu()
        opcao = input("Escolha uma operação (0-7): ").strip()

        if opcao == "0":
            print("Até logo!")
            break

        try:
            if opcao == "1":
                a = obter_numero("Primeiro número: ")
                b = obter_numero("Segundo número: ")
                resultado = soma(a, b)
                print(f"\n{a} + {b} = {resultado}")

            elif opcao == "2":
                a = obter_numero("Primeiro número: ")
                b = obter_numero("Segundo número: ")
                resultado = subtracao(a, b)
                print(f"\n{a} - {b} = {resultado}")

            elif opcao == "3":
                a = obter_numero("Primeiro número: ")
                b = obter_numero("Segundo número: ")
                resultado = multiplicacao(a, b)
                print(f"\n{a} * {b} = {resultado}")

            elif opcao == "4":
                a = obter_numero("Dividendo: ")
                b = obter_numero("Divisor: ")
                resultado = divisao(a, b)
                print(f"\n{a} / {b} = {resultado}")

            elif opcao == "5":
                base = obter_numero("Base: ")
                expoente = obter_numero("Expoente: ")
                resultado = potencia(base, expoente)
                print(f"\n{base} ^ {expoente} = {resultado}")

            elif opcao == "6":
                n = obter_numero_positivo("Número para raiz quadrada: ")
                resultado = raiz_quadrada(n)
                print(f"\n√{n} = {resultado}")

            elif opcao == "7":
                a = obter_numero("Dividendo: ")
                b = obter_numero("Divisor: ")
                resultado = modulo(a, b)
                print(f"\n{a} % {b} = {resultado}")

            else:
                print("Opção inválida. Escolha um número de 0 a 7.")

        except ValueError as e:
            print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
