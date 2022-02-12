
notas = []
media = 0

for i in range(15):
    print("> Digite a nota do aluno:")
    notas.append(float(input()))
    media += notas[-1]

media /= 15
print(str(media))
