# Calculadora Simples

Calculadora em Python com operações matemáticas básicas e avançadas, via menu interativo no terminal.

## Operações

| Opção | Operação        | Descrição              |
|-------|-----------------|------------------------|
| 1     | Soma (+)        | Adição de dois números |
| 2     | Subtração (-)   | Diferença entre dois números |
| 3     | Multiplicação (*) | Produto de dois números |
| 4     | Divisão (/)     | Quociente (evita divisão por zero) |
| 5     | Potência (^)    | Base elevada ao expoente |
| 6     | Raiz quadrada (√) | Raiz quadrada (números ≥ 0) |
| 7     | Módulo (%)      | Resto da divisão inteira |
| 0     | Sair            | Encerra o programa      |

## Requisitos

- Python 3.x (usa apenas biblioteca padrão `math`)

## Como executar

```bash
python calculadora.py
```

No Windows (PowerShell ou CMD):

```powershell
python calculadora.py
```

## Exemplo de uso

```
========================================
         CALCULADORA SIMPLES
========================================
1. Soma (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Potência (^)
6. Raiz quadrada (√)
7. Módulo (resto da divisão %)
0. Sair
========================================
Escolha uma operação (0-7): 5
Base: 2
Expoente: 10

2.0 ^ 10.0 = 1024.0
```

## Tratamento de erros

- Entrada inválida: o programa pede novamente um número válido.
- Divisão por zero: mensagem de erro e retorno ao menu.
- Raiz quadrada de número negativo: mensagem de erro e retorno ao menu.

## Estrutura do projeto

```
.
├── calculadora.py   # Código principal da calculadora
└── README.md        # Este arquivo
```

## Licença

Uso livre para estudo e modificação.
