a = 2 + 3 + 5
print (a)

# Tipos básicos
a = 1 #inteiros
b = 1.2 #ponto flutuante
c = 'c' #string 
d = 'hahahhaha, é o bixo piruleta' #string também

e = d[3] # caracter 'a'
print (a, b, c, d, e)

#Operadores Aritméticos
# a <op>=  b ======== a = a <op> b
x = 1 + 2
y = 4 - 3
z = 4/2
w = 5%2
u = 5//2
f = 5**3
t = 625**(0.5)
m = int(25**0.5)
print(x, y, z, w, u, f, t, m)


# conversão entre tipos 
r = int(5.0)
s = float(5)
i = str(r)
g = float('23.9') + 2
print(r, s, i, g)



#STRINGS 
msg = 'the quick brown fox jumps over the lazy dog'
s0 = msg [4:9]
print('0:', s0)
print(msg[0], len(msg))
s1 = msg[40:]
print('1:',s1)
s2 = msg[:3]
print('2:', s2)
s3 = msg[-8:-4]
print('3:', s3)

s4 = msg[-1]
print  ('4:', s4)

s5 = msg.lower()
s6 = msg.upper()
print(s5)
print(s6)
s7 = 'Carol, eu te amo'.upper()

print(s7)

msga = '                hh   hhh               '
print(msga.strip())

msgb = '\n             hh   hhh               \t\t'
print(msgb.strip())

msgc = '\n     3;4;5;6;-7;8;9;beijo;xxx;motherrussia    \n'.strip()
print(msgc.split(';'))

print(s7 + ' ' + msga.strip())
# CARACTERES DE ESCAPE : \?, onde ? é um   'comando'
#\n : nova linha 
# \t : tab (identação)
# \\: \ 
# \': ' 
# \": "

caracteres = "\n\t\'\\\""
print(caracteres)




#   ARRAYS/ LISTAS  
li = [1,2,3, "2","kid".upper()]
print(li, len(li))





# Lógica Booleana
q0 = True  
q1= False
q2 = q0 and q1
q3 = q0 or q1
q4 = not q3

#DECISÃO
if q4 and not q3:
    a += 4
    print('olá')
elif q1 and not q2:
    print('etcha')
else:
    print("tchau")


#Comparações




# laço
print('laço:')
stri = ''
for i in range(6,109, 6):
    stri += str(i) + ' '
print(stri)
stri = ''
for i in range(6,181, 6):
    stri += str(i) + ' '
print(stri)
stri = ''
for i in range(10,1001, 10):
    stri += str(i) + ' '
print(stri)



li = [1,2,3,4,5,6,7,8]
stri = ''
for el in  li:
    stri += str(el) + ' '   
print(stri)


li5 = [1,2,3,4,5,6,7,8,9,0]
for i, el in enumerate(li):
    print(i, ":", el)


# for(i = 0; i < li.length; i++) {console.log(li[i]); }

#operador + concatena listas
print(list(range(1,4)) + ['***'] + [5,6,7])
#método append insere elementos na lista 
li.append('novo elemento')
print(li)



#coisas chícs
li0 = list(range(1,100,2))
print(li0)
li1 = list(i**2 for i in li0)sgsdvs
print(li1)
li2 = list(e for e in li0 if e%3 == 0)
print(li2)
#matriz
matriz = list(list((i,j) for j in range(4)) for i in range(4))
for linha in matriz:
    print(linha)
