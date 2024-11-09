n = input().split() 
code = float(n[0])
quantity = float(n[1])

if code == 1:
    total = 4 * quantity
if code == 2:
    total = 4.5 * quantity
if code == 3:
    total = 5 * quantity
if code == 4:
    total = 2 * quantity
if code == 5:
    total = 1.5 * quantity

print(f"Total: R$ {total:.2f}")
