python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)

print(python.find("Java"))
#index = python.index("Java") index는 바로 프로그램을 종료시켜서 hi가 안나오고 find는 -1을 반환하고 프로그램은 지속 된다.
print("hi")

print(python.count("n"))