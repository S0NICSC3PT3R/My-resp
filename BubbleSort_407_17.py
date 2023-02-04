arr = [4,3,6,2,9,0]
def bubbleSort(List):
     n = len(List)
     for c in range(1,n):
          for i in range(0,n-c):
               elem = List[i]
               if elem > List[i+1]:
                    List.remove(elem)
                    List.insert(i+1,elem)
     return(List)
print(bubbleSort(arr))
