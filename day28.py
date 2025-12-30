file = open("data.txt", "w")
file.write("Hello Python")
file.close()

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()