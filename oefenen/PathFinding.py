class vertex:
    def __init__(self, a, visited = False):
        self.value = a
        self.edges = []
        self.visited = visited
def depthFirst(graph, start):
    stack = [start]
    path = []
    while stack != []:
        vertex = stack.pop()
        path.append(vertex)
        graph[vertex].visited = True
        for i in graph[vertex].edges:
            if graph[i].visited == False and int(graph[i].value)-1 not in stack:
                stack.append(i)
    return path
def breadthFirst(graph, start):
    queue = [start]
    path = []
    while queue != [] and len(path) < len(graph):
        vertex = queue.pop(0)
        path.append(vertex)
        graph[vertex].visited = True
        for i in graph[vertex].edges:
            if graph[i].visited == False and int(graph[i].value) -1 not in queue:
                queue.append(i)
    return path
def findPath(G, start, end, path= []):
    path = path + [start]
    if start == end:
        return path
    newPath = []
    for v in G[start].edges:
        if v not in path:
            newPath += findPath(G,v,end,path)
    return newPath

numberVertices = int(input())
lijst = []
for i in range(0, numberVertices):
    lijst += [[int(a) for a in input().split()]]
lijst2 = [int(a) for a in input().split()]
start = lijst2[0]
goal = lijst2[1]

Graph = []
for b in range(0, len(lijst)):
    Graph.append(vertex(lijst[b]))
    for c in range(1, len(lijst[b])):
        Graph[b].edges.append(lijst[b][c])

paths = findPath(Graph, start, goal)
count = 0
indexArray = []
for i in range(0, len(paths)):
    count += 1
    if paths[i] == goal:
        indexArray.append(count)
        count = 0

lowest = min(indexArray)
print(lowest)

