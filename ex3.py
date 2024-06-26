import random
invsum = random.randint(100, 10000)
print("Майк и Иван хотят вложиться в стартап.")
print("Минимальныя сумма инвестиций", invsum, "долларов.")

print("Сколько денег у Майка?")
cmike = int(input())
print("Сколько денег у Ивана?")
civan = int(input())

if (cmike >= invsum) & (civan >= invsum):
    result = "Оба могут вложиться (2)"
elif (cmike >= invsum):
    result = "Майк может вложиться (Mike)"
elif (civan >= invsum):
    result = "Иван может вложиться (Ivan)"
elif (cmike + civan >= invsum):
    result = "Могут сброситься и вложиться (1)"
else:
    result = "Никто не может вложиться (0)"

print(result)