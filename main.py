# Random labyrinth generator

clipboardImported = False

import random
try:
    import clipboard
    clipboardImported = True
except:
    pass

def inputPosition(name):
    return (
        int(input(f"Print {name} x position: ")),
        int(input(f"Print {name} y position: "))
    )

def printGrid(grid):
    for i in range(len(grid)):
        if i % 2 == 0:
            print(" ", end="")
        for j in range(len(grid[i])):
            print(grid[i][j], " ", end="")
        print("")

def renderGrid(sizex, sizey, walls):

    grid = []

    for i in range(sizey):
        arr = []
        grid.append(arr)
        for j in range(sizex):
            arr.append('.')

    for i in range(walls):
        x = random.randint(0, sizex-1)
        y = random.randint(0, sizey-1)
        grid[y][x] = '#'

    return grid

def printCPPGrid(grid):
    print("Start .cpp")

    cppString = ""

    cppString += "void randomlab(vector<field>& labyrinths){\n"
    cppString += "    int p = labyrinths.size();\n"
    cppString += f"    labyrinths.push_back(field({len(grid)}, {len(grid[0])}));\n"
    cppString += "    victory * v = new victory(&labyrinths[p])\n;"

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "#":
                cppString += f"    labyrinths[p].set_cell({y},{x}, new wall(NULL));\n"
            elif grid[y][x] == "*":
                cppString += f"    labyrinths[p].set_cell({y},{x}, v);\n"
            elif grid[y][x] == "@":
                cppString += f"    labyrinths[p].set_start_row({y});\n"
                cppString += f"    labyrinths[p].set_start_col({x});\n"
            
    cppString += "}"
    print(cppString)
    print("End .cpp")
    if (clipboardImported):
        clipboard.set(cppString)
        print("This file copied in your copy buffer")

if __name__ == "__main__":

    sizex = int(input("Write width of labyrinth: "))
    sizey = int(input("Write height of labyrinth: "))

    print(f"Size of labyrinth is ({sizex}, {sizey}), area: {sizex*sizey}")
    print("This labyrinth can be impossible because it is generates randomly")

    walls = int(input("How many walls do you want: "))

    print(f"{walls} walls will be generated on the grid")

    victory = (-1, -1)
    player = (-1, -1)

    grid = renderGrid(sizex, sizey, walls)    

    while True:
        printGrid(grid)

        print("What do you want to do?")
        print("Print 1 if you want to get c++ labyrinth generator")
        print("Print 2 if you want to retry")
        print("Print 3 if you want to set player position")
        print("Print 4 if you want to set victory position")
        print("Print 5 if you want to set new wall position")
        print("Print 6 if you want to exit")

        choice = int(input("Write your choice: "))

        if choice == 1:
            printCPPGrid(grid)

        elif choice == 2:
            grid = renderGrid(sizex, sizey, walls)

        elif choice == 3:
            
            curplayerx, curplayery = player

            if curplayerx != -1 and curplayery != -1:
                grid[curplayery][curplayerx] = "."

            playerx, playery = inputPosition("player")

            grid[playery][playerx] = "@"

        elif choice == 4:

            curvictoryx, curvictoryy = victory

            if curvictoryx != -1 and curvictoryy != -1:
                grid[curvictoryy][curvictoryx] = "."
            
            victoryx, victoryy = inputPosition("victory")

            grid[victoryy][victoryx] = "*"
            
        elif choice == 5:

            wallx, wally = inputPosition("wall")
            grid[wally][wallx] = "#"

        elif choice == 6:
            break

    print("Goodbye!")
