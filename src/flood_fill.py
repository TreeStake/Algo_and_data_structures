def recolor_field_from_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        height_input, width_input = map(int, lines[0].strip().split(','))
        line, column = map(int, lines[1].strip().split(','))
        recolour = lines[2].strip().strip("'")
        field_to_recolour = []
        for row in lines[3:]:
            row = row.strip().strip("[],\n").split(",")
            row = [element.strip("' ") for element in row]
            field_to_recolour.append(row)

    result_field = recolor_field(field_to_recolour, height_input, width_input, line, column, recolour)

    with open("output.txt", "w", encoding="utf-8") as file:
        for row in result_field:
            file.write(str(row) + "\n")
        file.close()
    return result_field


def recolor_field(field, height, width, line, column, recolour):
    visited = []
    queue = []
    colour = field[line-1][column-1]
    queue.append([line-1, column-1])

    while queue:
        current = queue.pop()
        field[current[0]][current[1]] = recolour
        visited.append([current[0], current[1]])
        line = current[0]
        column = current[1]

        if 0 <= line - 1 < height and field[line-1][column] == colour and [line-1, column] not in visited:
            queue.append([line-1, column])
        if 0 <= column - 1 < width and field[line][column-1] == colour and [line, column-1] not in visited:
            queue.append([line, column-1])
        if 0 <= column + 1 < width and field[line][column+1] == colour and [line, column+1] not in visited:
            queue.append([line, column+1])
        if 0 <= line + 1 < height and field[line+1][column] == colour and [line+1, column] not in visited:
            queue.append([line+1, column])
    return field
