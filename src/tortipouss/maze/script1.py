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


BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]


def save_maze_png(matrix, px, file_path2):
    data = []
    for row in matrix:
        total = []
        for cell in row:
            if cell == 0:
                total += BLUE * px
            elif cell == 1:
                total += RED * px
            elif cell == 2:
                total += BLACK * px
            elif cell == 3:
                total += GREEN * px

        data.extend([total] * px)

    shape_width, shape_height = len(matrix[0]), len(matrix)
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
    matrix = load_maze_txt(file_path)
    px = 20
    file_path2 = "maze.png"
    save_maze_png(matrix, px, file_path2)


main()
