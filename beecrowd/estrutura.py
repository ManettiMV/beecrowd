age = int(input())

years = age//365
months = 0
days = age%365

while days>=30:
    days-=30
    months+=1

print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")