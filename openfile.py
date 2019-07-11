import os 

BASEPATH = os.path.dirname()
print(BASEpath)

with open(BASEPATH + '/regex,py', 'r') as f:
    texto = f.readlines()

for linha in texto:
    print(linha)

with open(BASEPATH + '/xxx.igor', 'w') as f:
    f.write('este é um arquivo teste')

with open(BASEPATH + '/regex.py', 'rb') as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        print(byte.hex())





    