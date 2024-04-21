from Algo_and_data_structures.src.heap_based_priority_queue import BinaryHeap


def input_reading(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        print(lines)
        city = eval("[" + lines[0].strip() + "]")
        gas = eval("[" + lines[1] + "]")

        file.close()
    return city, gas


def output_writing(output, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for city in output:
            file.write(str(city) + "\n")
        file.close()
    return


def gas_supply(input_file, output_file):
    cities_lst, active_gas = input_reading(input_file)
    unable_supply = []
    for i in range(0, len(cities_lst)):
        city_to_check = cities_lst[i]
        able_gas = path_find(city_to_check, active_gas)
        unable_gas = [x for x in cities_lst if x not in able_gas]
        unable_supply.append([city_to_check, unable_gas])
        i += 1
    return output_writing(unable_supply, output_file)


def path_find(city_from, gas_road):
    queue = BinaryHeap()
    queue.add_element(city_from, 1)
    visited = [city_from]
    while queue.show_queue():
        current_city = queue.pop_element()
        for i, j in gas_road:
            if i == current_city and j not in visited:
                queue.add_element(j, 1)
                visited.append(j)
    return visited

