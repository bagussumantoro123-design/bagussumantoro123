number = 24
string1 = str(number)
print(string1)
# output ➜ 24

number = 24
string1 = f"{number}"
print(string1)
# output ➜ 24

items = [1, 2, 3, 4]
string2 = f"{items}"
print(string2)
# output ➜ [1, 2, 3, 4]

obj = {
    "name": "AMD Ryzen 5600g",
    "type": "processor",
    "igpu": True,
}
string3 = f"{obj}"
print(string3)
# output ➜ {'name': 'AMD Ryzen 5600g', 'type': 'processor', 'igpu': True}
