'''Base 10'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
a=a*1000
b=b*100
c=c*10
d=d*1
x=a+b+c+d
res=x*2
print(res)

'''Base 2'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
a = a*(2**3)
b = b*(2**2)
c = c*(2**1)
d = d*(2**0)
res=a+b+c+d
print(res)

''' Somando strings'''
a = input()
b = input()
c = input()
x = a+b
y = a+c
z = b+a
w = b+c
i = c+a
j = c+b
print(x)
print(y)
print(z)
print(w)
print(i)
print(j)

'''A Compra Responsável'''
x = int(input())
y = int(input())
if x>=y: 
    resposta = 'pode comprar tudo'
if x<y:
    resposta = 'saldo insuficiente'
print(resposta)

'''A Compra Responsável Informada'''
x = int(input())
y = int(input())
z = x-y
if x>=y:
    print('se você comprar tudo o saldo será:', z)
elif x<y:
   print('seu saldo é insuficiente para essa compra')

''' Idade para votar'''
idade = int(input())
if idade>=16: 
    resposta = 'Tem idade para votar'
if idade<16:
    resposta = 'Jovem demais para votar, espere até 16'
print(resposta)

'''Voto obrigatório ou facultativo?'''
idade = int(input())
if idade == 16 or idade == 17:
  resposta = 'Seu voto é facultativo: você pode votar ou não'
elif idade <= 15:
  resposta = 'Jovem demais para votar, espere até 16'
elif idade >=70:
  resposta = 'Seu voto é facultativo: você pode votar ou não'
else:
  resposta = 'Seu voto é obrigatório'
print(resposta)

''' Mes: de número para nome abreviado'''
x = int(input())
if x==1:
    print('jan')
elif x==2:
    print('fev')
elif x==3:
    print('mar')
elif x==4:
    print('abr')
elif x==5:
    print('mai')
elif x==6:
    print('jun')
elif x==7:
    print('jul')
elif x==8:
    print('ago')
elif x==9:
    print('set')
elif x==10:
    print('out')
elif x==11:
    print('nov')
elif x==12:
    print('dez')

'''Final da placa'''
x = int(input())
print(x%10)

'''Rodízio de automóveis'''
x = int(input())
a = (x%10)
if (a==1 or a==2):
    print('segunda-feira')
elif (a==3 or a==4):
    print('terça-feira')
elif (a==5 or a==6):
    print('quarta-feira')
elif (a==7 or a==8):
    print('quinta-feira')
elif (a==9 or a==0):
    print('sexta-feira')

''' Romanos'''
x=str(input())
if(x=='I'):
    print('1')
if(x=='V'):
    print('5')
if(x=='X'):
    print('10')
if(x=='L'):
    print('50')
if(x=='C'):
    print('100')
if(x=='D'):
    print('500')
if(x=='M'):
    print('1000')

'''Secular'''
x = int(input())
a = (x//100)
b = (x%100)
if(b==0):
  res = a
else:
  res = a+1
print(res)

'''Futebol'''
t1 = str(input())
t2 = str(input())
p1 = int(input())
p2 = int(input())
if(p1==p2):
    print('prorrogação!')
    pr1 = int(input())
    pr2 = int(input())
    if(pr1==pr2):
        print('disputa de penaltis!')
    else:
        if(pr1>pr2):
          print('vitoria:', t1)
        else:
          print('vitoria:', t2)
else:
    if(p1>p2):
        print('vitoria:', t1)
    else:
        print('vitoria:',t2)

'''Vogal?'''
l = str(input())
if (l in ('a', 'e', 'i', 'o', 'u')):
    print('vogal minúscula')
elif (l in ('A','E','I','O','U')):
    print('vogal maiúscula')
else:
    print('não é vogal')

'''Usando o teclado para jogar'''
t = str(input())
if (t=='a'or t=='A'):
    print('LEFT')
elif (t=='s'or t=='S'):
    print('DOWN')
elif (t=='w'or t=='W'):
    print('UP')
elif (t=='d'or t=='D'):
    print('RIGHT')
else:
    print('?')

'''Soma, subtração, multiplicação, divisão, módulo, divisão inteira e potência'''
x = int(input())
y = int(input())
div = x/y
print(x+y)
print(x-y)
print(x*y)
print('%.2f'% div)
print(x%y)
print(x//y)
print(x**y)

'''Operação da vez'''
x = int(input())
y = int(input())
z = str(input())
if (z=='+'):
    print(x+y)
elif (z=='-'):
    print(x-y)
elif (z=='*'):
    print(x*y)
elif (z=='/'):
    print(x/y)
elif (z=='//'):
    print(x//y)
elif (z=='%'):
    print(x%y)
elif (z=='**'):
    print(x**y)

''' + - * ** / // %'''
z = str(input())
x = int(input())
y = int(input())
if (z=='+'):
    print(x+y)
elif (z=='-'):
    print(x-y)
elif (z=='*'):
    print(x*y)
elif (z=='/'):
    print(x/y)
elif (z=='//'):
    print(x//y)
elif (z=='%'):
    print(x%y)
elif (z=='**'):
    print(x**y)

'''Maior Menor'''
n1 = int(input())
n2 = int(input())
if (n1>n2):
    print('maior:',n1)
    print('menor:',n2)
else:
    print('maior:',n2)
    print('menor:',n1)

'''Bandeira'''
c = str(input())
if(c=='azul'):
    print('circunferência')
elif(c=='amarelo'):
    print('losango')
elif(c=='verde'):
    print('retângulo')
elif(c=='branco'):
    print('faixa')
else:
    print('não tem essa cor')
