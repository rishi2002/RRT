import numpy
import random
import matplotlib.pyplot as plt

# startx = float(input("Enter x-coordintate of start:"))
#
# starty = float(input("Enter y-coordintate of start:"))
#
# goalx = float(input("Enter x-coordintate of goal:"))
#
# goaly = float(input("Enter y-coordintate of goal:"))
#
# step = float(input("Enter step length:"))
startx=0
starty=0
goalx=10
goaly=10
step=0.1


def rrt(startx, starty, goalx, goaly, step):
    L1 = []
    L2 = []
    L3 = []

    L1.append([startx, starty])
    L3.append([startx, starty])
    L2.append(None)
    error = 1

    coordinates = [0, 0]  # random coordinate chosen
    parent_node = [0, 0]  # pre-existing coordinate closest to random coordinate
    new_node = [0, 0]  # coordinate obtained after moving the step length

    while True:
        # print(L1)
        coordinates[0] = numpy.random.uniform(startx, goalx)
        coordinates[1] = numpy.random.uniform(starty, goaly)
        # L3.append([coordinates[0],coordinates[1]])
        # coordinates = [goalx, goaly]
        min_dist = 10000 # ((goalx-startx)**2 + (goaly-starty)**2)+1
        for j in range(len(L1)):      # finding parent node for j in range(len(L1))
            # dist = (coordinates[0]-L1[j][0])**2 + (coordinates[1]-L1[j][1])**2
            dist = numpy.hypot((coordinates[0]-L1[j][0]),(coordinates[1]-L1[j][1]))
            if dist < min_dist:
                min_dist = dist
                parent_node = [L1[j][0], L1[j][1]]
        i_cap = (coordinates[0]-parent_node[0])/numpy.sqrt((coordinates[0]-parent_node[0])**2+(coordinates[1]-parent_node[1])**2)
        j_cap = (coordinates[1]-parent_node[1])/numpy.sqrt((coordinates[0]-parent_node[0])**2+(coordinates[1]-parent_node[1])**2)
        new_node[0] = parent_node[0] + step*i_cap
        new_node[1] = parent_node[1] + step*j_cap

        L1.append([new_node[0],new_node[1]])
        L2.append([parent_node[0],parent_node[1]])
        # print(L1)
        print(len(L1))

        radius = numpy.sqrt((new_node[0]-goalx)**2+(new_node[1]-goaly)**2)
        if radius < error:
            print("Came Close to Goal")
            L1.append([goalx, goaly])
            L2.append(new_node)
            break
    # L3 = numpy.array(L3)
    # x = L3[:, 0]
    # y = L3[:, 1]
    #
    # plt.scatter(x, y)
    # plt.show()
    return [L1, L2]

def backtrack(L1, L2):
    print("Entered backtrack")
    print(L1)
    L3=[]
    i = len(L1)
    current_node = L1[i-1]
    L3.append(current_node)
    parent_node = L2[i-1]
    while True:

        current_node = parent_node
        L3.append(current_node)
        i = L1.index(current_node)
        parent_node = L2[i]
        if parent_node is None:
            print("Reached start")
            break

    return L3


[L1, L2] = rrt(startx, starty, goalx, goaly, step)
print("RRT complete")

L3 = backtrack(L1, L2)
print("Backtrack finished")
print(len(L3))

for i in range(len(L3)):
    print(L3[i])

L1 = numpy.array(L1)
x = L1[:,0]
y = L1[:,1]

plt.scatter(x,y,s=2)
plt.show()

"""
(x1,y1), (x2,y2)
np.hypot((x1-x2),(y1-y2))
"""
