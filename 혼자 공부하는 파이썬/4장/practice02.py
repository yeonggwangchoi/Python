pets=[
    {"name":"구름","age":5},
    {"name":"초코","age":4},
    {"name":"나비","age":2}
]

print("개들\n")
for pet in pets:
    print(pet["name"], str(pet["age"])+"살")