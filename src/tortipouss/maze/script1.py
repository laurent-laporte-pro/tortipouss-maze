from pathlib import Path
import png


def load_maze_txt(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    final_list = []
    for line in lines:
        maze_row = []
        for item in line.strip():
            maze_row.append(int(item))

        final_list.append(maze_row)

    return final_list


def save_maze_png(maze_row, px, file_path2):
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    WHITE = [255, 255, 255]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]

    data = []
    for row in maze_row:
        total = []
        for cell in row:
            if cell == 2:
                BK = BLACK * px
                total += BK
            if cell == 0:
                B = BLUE * px
                total += B
            if cell == 1:
                R = RED * px
                total += R
            if cell == 3:
                G = GREEN * px
                total += G

        data.append(total)

    shape_width, shape_height = len(maze_row[0]), len(maze_row)
    filename = Path(file_path2)
    with filename.open(mode="wb") as fd:
        writer = png.Writer(
            width=shape_width * px,
            height=shape_height * px,
            greyscale=False,
        )
        writer.write(fd, data)


def main():
    file_path = "Laby1.txt"
    maze_row = load_maze_txt(file_path)
    px = 1
    file_path2 = "maze.png"
    save_maze_png(maze_row, px, file_path2)


main()
