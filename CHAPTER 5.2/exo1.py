1| for firstName in nameList:
2|     for secondName in nameList:
3|         print(firstName, "equals", secondName, ":", firstName == secondName)

1| while len(nameList) > 0:
2|     print(nameList[0])
3|     del nameList[0]

 1| def recursive_binary_search(searchList, searchTerm):
 2|     searchList.sort()
 3| 
 4|     if len(searchList) == 0:
 5|         return False
 6| 
 7|     middle = len(searchList) // 2
 8|     
 9|     if searchList[middle] == searchTerm:
10|         return True
11|     elif searchTerm < searchList[middle]:
12|         return binary_search(searchList[:middle], searchTerm)
13|     else:
14|         return binary_search(searchList[middle + 1:], searchTerm)
15|
16| recursive_binary_search(nameList, name)

1| if len(nameList) > 0:
2|     print(nameList[-1])

