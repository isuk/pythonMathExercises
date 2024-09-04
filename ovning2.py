
n = int(input("Range for fibonacci: "))
num1 = 0
num2 = 1
nextNumber = num2
count = 0

while count <= n:
    count += 1
    print(f"{nextNumber} ")
    num1 = num2
    num2 = nextNumber
    nextNumber = num1 + num2

