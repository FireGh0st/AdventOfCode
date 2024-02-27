file_path = "puzzle_input.txt"

sum = 0
expected_red_cube = 12
expected_green_cube = 13
expected_blue_cube = 14

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
            good = True
            while game and good:
                red = green = blue = 0
                for cube in game.split(", "):
                    if "red" in cube:
                        red += int(cube.split(" ")[0])
                    elif "green" in cube:
                        green += int(cube.split(" ")[0])
                    elif "blue" in cube:
                        blue += int(cube.split(" ")[0])
                if red > expected_red_cube or green > expected_green_cube or blue > expected_blue_cube:
                    good = False
                game = next(games, None)
            if good:
                sum += int(id)
            
        print(f"Sum of the IDs of the good games: {sum}")

                    
                    
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
