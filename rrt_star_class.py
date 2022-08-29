import numpy
import random
import matplotlib.pyplot as plt 

start = [0,0]
goal = [5,5]
step = 0.1
error = 0.5
radius = 0.5

class Node():
    pos = [0,0]
    parent = [0,0]
    cost = 0

coordinates = [0,0]
new_node = Node()
parent_node = Node()

L = []
initial_node = Node()
initial_node.pos = start
initial_node.parent = None
initial_node.cost = 0
L.append(initial_node)

while True:
    coordinates = [numpy.random.uniform(start[0],goal[0]),numpy.random.uniform(start[1],goal[1])]
    min_dist = 10000
    for i in range(len(L)):
        dist = numpy.hypot((coordinates[0]-L[i].pos[0]),(coordinates[1]-L[i].pos[1]))
        if dist < min_dist:
            min_dist = dist
            parent_node = L[i]

    i_cap = (coordinates[0]-parent_node.pos[0])/numpy.hypot((coordinates[0]-parent_node.pos[0]),(coordinates[1]-parent_node.pos[1]))
    j_cap = (coordinates[1]-parent_node.pos[1])/numpy.hypot((coordinates[0]-parent_node.pos[0]),(coordinates[1]-parent_node.pos[1]))

    new_node.pos = [parent_node.pos[0]+step*i_cap,parent_node.pos[1]+step*j_cap]
    new_node.parent = [parent_node.pos[0],parent_node.pos[1]]       # physically closest parent

    min_cost = 10000
    cost = 0

    #finding parent node
    for i in range(len(L)):
        dist = numpy.hypot((L[i].pos[0]-new_node.pos[0]),L[i].pos[1]-new_node.pos[1])
        if dist < radius:
            if L[i].cost<min_cost:
                min_cost = L[i].cost
                parent_node = L[i]
                cost = L[i].cost + dist
    
    L.append(None)
    L[-1] = Node()
    L[-1].pos = new_node.pos
    L[-1].parent = parent_node.pos
    L[-1].cost = cost

    rad = numpy.hypot((goal[0]-new_node.pos[0]), (goal[1]-new_node.pos[1]))
    if rad<error:
        L.append(None)
        L[-1] = Node()
        L[-1].pos = goal
        L[-1].parent = new_node.pos
        L[-1].cost = None
        break

L1 = []
for j in range(len(L)):
    L1.append(L[j].pos)
L1 = numpy.array(L1)
x = L1[:,0]
y = L1[:,1]

plt.scatter(x,y,s=2)
plt.show()
    
Selected_Nodes = []
current_node = L[-1]
Selected_Nodes.append(current_node)
while True:

    for j in range(len(L)):
        if L[j].pos[0] == current_node.parent[0] and L[j].pos[1] == current_node.parent[1]:
            current_node = L[j]
            Selected_Nodes.append(current_node)
            break
    if current_node.parent == None:
        print("Reached start!")
        break

L2 = []
for k in range(len(Selected_Nodes)):
    L2.append(Selected_Nodes[k].pos)
L2 = numpy.array(L2)
x = L2[:,0]
y = L2[:,1]

plt.scatter(x,y,s=1)
plt.show()