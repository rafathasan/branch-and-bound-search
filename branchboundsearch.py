import sys

path = []
pathcost = 0

def save_path(start, goal, parent, cost):
    global path, pathcost
    path = [goal]
    node = goal

    while True:
        path.append(parent[node])
        node = parent[node]
        if(node) is start:
            break
    path.reverse()
    pathcost = cost[goal]


def search(data, start, goal):
    parent = {}
    cost = {start:0}
    visited = []
    level = [start]
    bound_cost = sys.maxsize

    while len(level):
        node = level[0]
        level.remove(node)
        visited.append(node)

        for subnode,tcost in data[node].items():
            if (cost[node] + tcost) >= bound_cost:
                continue
            if subnode in visited:
                if (cost[node] + tcost) >= cost[subnode]:
                    continue

            cost[subnode] = cost[node] + tcost
            parent[subnode] = node
            if subnode is goal:
                bound_cost = cost[subnode]
                save_path(start, goal, parent, cost)
                continue

            level.append(subnode)


    return {'path': path, 'cost': pathcost}