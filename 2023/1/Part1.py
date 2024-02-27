file_path = "puzzle_input.txt"

sum = 0

try:
    with open(file_path, "r") as file:
        file_contents = file.read()
        for line in file_contents.split("\n"):
            lastdigitfound = 0
            firstdigit = 0
            for i in range(len(line)):
                if line[i] >= "0" and line[i] <= "9":
                    if firstdigit == 0:
                        firstdigit = int(line[i])
                    lastdigitfound = int(line[i])
            sum += firstdigit * 10 + lastdigitfound
        print(f"Sum of all numbers in file '{file_path}' is {sum}")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
