import os

folders = input("please provide list of folders names with spaces in b/w :" ).split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valide folder name")
        break

    print("listing files for the folder - " + folder )

    for file in files:
        print(file)

