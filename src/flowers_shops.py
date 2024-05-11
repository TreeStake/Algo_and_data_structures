def input_reading(filename):
    graph = {}
    with open(filename, "r", encoding="ANSI") as file:
        lines = file.readlines()
        farms = lines[0].strip().split(';')
        farms = list(filter(None, farms))
        shops = lines[1].strip().split(';')
        shops = list(filter(None, shops))
        graph["Farms"] = {farm: float('inf') for farm in farms}

        for shop in shops:
            graph[shop] = {"Shops": float('inf')}

        data_routes = [item for item in lines[2].split(';')]

        routes = [[subitem.strip() for subitem in item.split(',')] for item in data_routes]

        for route in routes:
            source, destination, capacity = route
            if source not in graph:
                graph[source] = {}
            graph[source][destination] = int(capacity)
    return "Farms", "Shops", graph


def dfs_search(graph, farms, shops):
    stack = [(farms, float("inf"), None)]
    visited = set()
    path = []
    min_value = float("inf")
    found_end_vertex = False

    while stack and not found_end_vertex:
        current_node, value, parent = stack.pop()
        if parent:
            path.append((parent, current_node))

        if value < min_value:
            min_value = value

        if current_node in shops:
            found_end_vertex = True

        elif current_node in graph:
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    stack.append((neighbor, weight, current_node))

    if not path or path[-1][1] != shops or path[0][0] != farms:
        return [], 0

    return path, min_value


def update_capacity(graph, path, value):
    for s, e in path:
        graph[s][e] -= value
        if graph[s][e] == 0:
            del graph[s][e]


def ford_fulkerson(filename):
    farms, shops, graph = input_reading(filename)
    max_flow_value = 0

    while True:
        path, value = dfs_search(graph, farms, shops)
        if value == 0 or path[0][0] != farms:
            break
        max_flow_value += value
        update_capacity(graph, path, value)

    return max_flow_value
