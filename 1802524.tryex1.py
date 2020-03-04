# Carlos Henrique Durante da Silva
# (11)96340-9937
# carlos.durante@outlook.com
# https://linkedin.com/in/carloshdurante
# Execeptions

continuar = True
while continuar:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
        if x <= 0 or y <= 0:
            raise TypeError
    except ZeroDivisionError:
        print("Erro: divisao por zero")
    except TypeError:
        print("Os numeros informados devem ser positivos")
    except ValueError:
        print("O valor informado deve ser um número inteiro")
    except Exception:
        print("Erro")
    else:
        continuar = False
        print('O resultado da divisão é:', z)
