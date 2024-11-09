# Lê os inputs e separa eles
n = input().split()
n1 = float(n[0])
n2 = float(n[1])
n3 = float(n[2])
n4 = float(n[3]) 

# Tira a média
average = (n1 * 2 + n2 * 3 + n3 * 4 + n4 *1)/(10)

print(f'Media: {average:.1f}')

if average>=7:  # Se maior ou igual a 7 passa
    print('Aluno aprovado.')
elif average>=5:    # Se não vai a exame
    print('Aluno em exame.')
    n5 = float(input())     # Lê a nota do exame
    print(f'Nota do exame: {n5}')  
    average = (average+n5)/2    # Tira a nova média
    if average>=5:  # Se for maior ou igual a 5 passa
        print('Aluno aprovado.')
    else:   # Se não, reprova
        print('Aluno reprovado.')
    print(f'Media final: {average:.1f}')
else:   # Caso a média inicial seja menor que 5, reprova
    print('Aluno reprovado.')