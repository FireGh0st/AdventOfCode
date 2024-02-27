file_path = "puzzle_input.txt"


sum = 0

try:
    with open(file_path, "r") as file:
        file_contents = file.read()
        for line in file_contents.split("\n"):
            lastdigitfound = 0
            firstdigit = 0
            for i in range(len(line)):
                if len(line) - i >= 3:
                    threedigits = line[i] + line[i + 1] + line[i + 2]
                    if threedigits == "one":
                        if firstdigit == 0:
                            firstdigit = 1
                        lastdigitfound = 1
                        i += 2
                    if threedigits == "two":
                        if firstdigit == 0:
                            firstdigit = 2
                        lastdigitfound = 2
                        i += 2
                    if threedigits == "six":
                        if firstdigit == 0:
                            firstdigit = 6
                        lastdigitfound = 6
                        i += 2
                if len(line) - i >= 4:
                    fourdigits = line[i] + line[i + 1] + line[i + 2] + line[i + 3]
                    if fourdigits == "five":
                        if firstdigit == 0:
                            firstdigit = 5
                        lastdigitfound = 5
                        i += 3
                    if fourdigits == "four":
                        if firstdigit == 0:
                            firstdigit = 4
                        lastdigitfound = 4
                        i += 3
                    if fourdigits == "nine":
                        if firstdigit == 0:
                            firstdigit = 9
                        lastdigitfound = 9
                        i += 3
                if len(line) - i >= 5:
                    fivedigits = line[i] + line[i + 1] + line[i + 2] + line[i + 3] + line[i + 4]
                    if fivedigits == "three":
                        if firstdigit == 0:
                            firstdigit = 3
                        lastdigitfound = 3
                        i += 4
                    if fivedigits == "seven":
                        if firstdigit == 0:
                            firstdigit = 7
                        lastdigitfound = 7
                        i += 4
                    if fivedigits == "eight":
                        if firstdigit == 0:
                            firstdigit = 8
                        lastdigitfound = 8
                        i += 4

                if line[i] >= "0" and line[i] <= "9":
                    if firstdigit == 0:
                        firstdigit = int(line[i])
                    lastdigitfound = int(line[i])
            sum += firstdigit * 10 + lastdigitfound
        print(f"Sum of all numbers in file '{file_path}' is {sum}")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
