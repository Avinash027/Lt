import os

# 1. Write, Read & Append (3 marks)
with open("example.txt","w") as f:
    f.write("Hello, File Handling in Python!\nThis is the second line.\n")

with open("example.txt","r") as f:
    print(f.read())

with open("example.txt","a") as f:
    f.write("This line is appended.\n")

# 2. Line-by-Line Reading (2 marks)
with open("example.txt","r") as f:
    for line in f:
        print(line.strip())

# 3. File Paths & Directories (2 marks)
os.makedirs("data",exist_ok=True)

with open("data/info.txt","w") as f:
    f.write("File inside data folder.\n")

print(os.path.exists("data/info.txt"))
print(os.listdir("data"))

# 4. Exception Handling (2 marks)
try:
    with open("non_existing.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

try:
    with open("/root/secure.txt","r") as f:
        print(f.read())
except (PermissionError,FileNotFoundError):
    print("Permission denied!")