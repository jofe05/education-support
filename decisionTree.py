#!/usr/bin/python
from graphviz import Digraph

#----------- Functions declaration starts here -----------
#Function Definition:  How Many Paths Start With A Specific Task
def howManyStartWith(task, paths):
    counter = 0
    for path in paths:
        if path[0] == task:
            counter += 1
    return counter

#Function Definition:  Wich paths are contained in others
def isContained(paths):
    i = 0
    j = 0
    indent = 0
    pathsOcc = []
    for path in paths:
        pathSet = set(path)
        flag = 0
        ocurrencies = [] # *****
        for path2 in paths:
            path2Set = set(path2)
            if pathSet.issubset(path2Set) and path != path2:
                ocurrencies.append(j)
                flag = 1
            j += 1
        if flag == 0:
            indent += 1
            #print( str(indent) + ". " +str(path)+ " is not a subset")
        pathsOcc.append(ocurrencies)
        i += 1
        j = 0
    return pathsOcc

def createGraph(path, name):
    graph = Digraph(name, filename="graph#"+name, format="png")
    for i in range(0, len(path)):
        graph.node(path[i], path[i])
        if i > 0:
            graph.edge(path[i-1], path[i])
    graph.view()

def showPaths(paths):
    i = 0
    for path in paths:
        print("Path#" + str(i+1) + " : " + str(path) + " \n")
        i += 1

def pathDifference(paths, index):
    i = 0
    j = i + 1
    numDif = []
    for i in range(0, len(index)):
        pathSet = set(paths[index[i]])
        ocurrencies = [] # *****
        for j in range(0, len(index)):
            path2Set = set(paths[index[j]])
            ocurrencies.append(len(list(pathSet.difference(path2Set))))
            j += 1
            #print( str(indent) + ". " +str(path)+ " is not a subset")
        numDif.append(ocurrencies)
        i += 1
        j = i + 1
    return numDif
#----------- Functions declaration ends here -----------

## ************ MAIN ************
if __name__ == "__main__":
    print("*** Path Selector ***\n")
    print("\nLoading Tasks: ")
    tasksDic = {"B2":3000, "B3":1496, "B4":744, "D2":2000, "D3":996, "D4":660, "D5":436, "D6":392,\
    "D7":353, "F2":1600, "F3":796, "F4":527, "F5":347, "F6":312, "F7":279, "F8":250, "H2":1600, \
    "H3":796, "H4":527, "H5":347, "H6":312, "H7":279, "H8":250, "H9":234, "J2":3000, "J3":1496, \
    "J4":744, "J5":368, "J6":303, "J7":248, "J8":222}
    print("Number of tasks " + str(len(tasksDic)) + "\n")
    nPaths = 723
    nTasks = 40 
    pathParents = [] # Are the path not contained in any other path
    paths = [[0 for x in range(nTasks)] for y in range(nPaths)]
    pathsContained = [[0 for x in range(nPaths)] for y in range(nPaths)]
    filePath = open("paths.csv", "r")
    i = 0
    for line in filePath:
        line = line.replace("\n", "")
        paths[i] = line.split(",")
        i += 1

    #showPaths(paths) #Uncomment to show all paths 
    i = 0
    total = 0
    for key,value in tasksDic.items():   
        starters = howManyStartWith(key,paths)
        if starters == 0:
            i += 1
        print ("There are "+ str(starters) + " paths that start with task: " + key )
        total += starters
    print("\nNumber of paths checked: " + str(total) + "\n")
    print("Number of tasks are not at the start of any path: " + str(i) + "\n")
    pathsContained = isContained(paths)
    
    i = 456
    print("Path " + str(i-1) + ": " + str(paths[i]))

    #print("Path #" + str(i) + " is contained in " + str(len(pathsContained[i])))
    
   
   
   
    c = 0
    for i in range(0, len(paths)):
        if len(pathsContained[i]) == 0:
            pathParents.append(i)
            c +=1
            #createGraph(paths[i], str(i))
    print("There are " + str(c) + " paths out of " + str(total) + " that are not contained other paths\n")        
    a = []
    a = pathDifference(paths, pathParents)

    print("\n\n==================== MATRIX OF THE DIFFERENCES BETWEEN UNIQUE PATHS ====================\n")
    for i in a:
        print(i, len(i))

    
    

    