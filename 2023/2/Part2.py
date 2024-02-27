file_path = "puzzle_input.txt"

sum = 0

try:
    with open(file_path, "r") as file:
        file_contents = file.read()
        for line in file_contents.split("\n"):
        
            #Game 1: 7 red, 8 blue; 6 blue, 6 red, 2 green; 2 red, 6 green, 8 blue; 9 green, 2 red, 4 blue; 6 blue, 4 green
            #id = 1
            #blue = 8 + 6 + 8 + 4 = 26
            #red = 7 + 6 + 2 + 2 = 17
            #green = 6 + 2 + 6 + 9 + 4 = 27
            id = line.split(":")[0].split(" ")[1]
            line = line.split(":")[1].strip()
            games = iter(line.split("; "))
            game = next(games)
            min_red = min_green = min_blue = 0
            while game:
                red = green = blue = 0
                for cube in game.split(", "):
                    if "red" in cube:
                        red += int(cube.split(" ")[0])
                    elif "green" in cube:
                        green += int(cube.split(" ")[0])
                    elif "blue" in cube:
                        blue += int(cube.split(" ")[0])
                min_red = max(min_red, red)
                min_green = max(min_green, green)
                min_blue = max(min_blue, blue)
                game = next(games, None)
            sum += min_red * min_green * min_blue
            
        print(f"Sum of the power of the minimum cubes: {sum}")

                    
                    
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
