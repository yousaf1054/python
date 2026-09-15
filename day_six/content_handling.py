with open("student.txt","r") as file:
    for line in file:
        content=line.strip()
        # print(content)
        name,mark=content.split(",")
        print(f"{name} -> {mark}")


try:
    with open("unknown.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")