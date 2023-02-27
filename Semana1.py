'''O Próximo'''
x = int(input())
x = x+1
print(x)

'''O Anterior'''
x = int(input())
x = x-1
print(x)

'''O Dobro'''
x = int(input())
x = x*2
print(x)

''' A Metade'''
x = int(input())
x = x/2
print(x)

''' Divisão Inteira'''
x = int(input())
y = int(input())
a = int(x//y)
b = int(x%y)
print(a)
print(b)

'''Bem-vinda'''
nome = input()
print('Bem-vinda', nome)

'''Cadastro Light'''
nome = input()
sobrenome = input()
print(nome,' ',sobrenome)

'''Rejuvenescimento Light'''
nome = input()
idade = int(input())
print(idade-2)
print(nome)

'''Decimais à moda antiga'''
valor = float(input())
print('%.2f'%valor)
print('%.4f'%valor)
print('%.6f'%valor)
print('%.8f'%valor)
print('%.10f'%valor)

'''O Aumento no Salário'''
x = int(input())
y = int(input())
a = y/100
print(x*a)

'''O Salario Reajustado'''
x = int(input())
y = int(input())
a = (x*y/100)
print (a+x)

'''A Compra Questionável'''
x = int(input())
y = int(input())
res = x-y
print(res)

'''Gorjeta'''
x = float(input())
y = int(input())
a = (x*y/100)
b = (x+a)
print('%.2f'%b)

''' Horas e minutos'''
x = int(input())
y = (x//60)
z = (x%60)
print("{}min = {}h{}min".format(x, y, z))

'''PIN perigoso'''
x = int(input())
y = int(input())
print(x+y)

'''Minuteria'''
m = int(input())
s = int(input())
total = m*60+s
print(total)

'''Trabalho voluntário #1'''
nx = int(input())
nc = int(input())
cc = int(input())
print(nx*240,'ml')
print(nc*15,'ml')
print(cc*5,'ml')

'''Operadores de Comparação'''
x = int(input())
y = int(input())
print('x==y:',x==y)
print('x!=y:',x!=y)
print('x>y:',x>y)
print('x<y:',x<y)
print('x>=y:',x>=y)
print('x<=y:',x<=y)

'''Operadores Lógicos'''
x = input()
valor = (x=='True')
print(not valor)

'''Papagaio Engraçado'''
x=input()
print(x)
print(x)