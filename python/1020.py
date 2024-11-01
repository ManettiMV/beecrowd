dias = int(input())         # Lê o input

anos = 0
meses = 0

while dias >= 30:           # Enquanto tiver mais de 30 dias ele vai dividir tudo em anos e meses
    if dias >= 365:         # E o que sobrar fica como 'dias'
        anos += 1
        dias -= 365
    if dias >= 30:
        meses += 1
        dias -= 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")