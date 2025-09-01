# Data strucutre in python 
#list,tuple,heap,linkedlist,stack,queue,and many mores 

#1 . list
A = [1,2,3,4,5]
A.append(6)
print(A)

#2 . Tuple 
B = (1,2,3,4,5)
print(B)

#3 . Set
C = {1,2,3,4,5}
print(C)

#4 Directoryes 
my_dict = {"name": "Om", "age": 20}
my_dict["city"] = "Mumbai"
print(my_dict["name"])

#5 Heap 
def heap_sort(arr):
    import heapq
    heapq.heapify(arr)  # Convert list to min-heap
    return [heapq.heappop(arr) for _ in range(len(arr))]

arr = [12, 3, 5, 7, 1]
print("Heap Sort:", heap_sort(arr))
