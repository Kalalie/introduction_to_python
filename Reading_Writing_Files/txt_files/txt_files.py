names = []

with open("names.txt") as txt_files:
    for line in txt_files:
        print(line)
        line = line.strip()
        names.append(line)

print(names)

with open("names_output.txt", "w") as txt_files:
    for name in names:
        txt_files.write(name + "\n")