import sys

def search(data, start, goal):

    parent = {}
    cost = {start:0}
    visited = []
    level = {start:0}
    bound_cost = sys.maxsize

    while bool(level):
        node = min(level, key=level.get)
        level.pop(node, None)
        visited.append(node)

        if node is goal:
            bound_cost = cost[goal]

        for subnode,tcost in data[node].items():
            if cost[node]+tcost > bound_cost:
                continue
                
            if subnode in visited:
                if cost[subnode] <= tcost:
                    continue
            cost[subnode] = cost[node] + tcost
            level[subnode] = tcost
            parent[subnode] = node
    
    path = [goal]
    node = goal

    while True:
        path.append(parent[node])
        node = parent[node]
        if(node) is start:
            break
    path.reverse()
    print(data)
    print(parent)
    print(cost)


    return {'path': path, 'cost': cost[goal]}