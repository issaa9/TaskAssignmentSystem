List = [2,4,8,1,16,13,59,42,25]

def MergeSort(List):
 if len(List) > 1:
     mid = len(List) // 2
     LeftList = List[:mid]
     RightList = List[mid:]
     MergeSort(LeftList)
     MergeSort(RightList)
     #add elements from right and left into
     #merged list in order
     i = 0
     j = 0
     k = 0
     while i < len(LeftList) and j < len(RightList):
         if LeftList[i] < RightList[j]:
             List[k] = LeftList[i]
             i = i + 1
         else:
             List[k] = RightList[j]
             j = j + 1
         k = k + 1
         #check if left list has elements not merged
     while i < len(LeftList):
             List[k] = LeftList[i]
             i = i + 1
             k = k + 1
         #check if right list has elements not merged
     while j < len(RightList):
             List[k] = RightList[j]
             j = j + 1
             k = k + 1
     return(List)

def BinarySearch(List, item ,count,left,right):
 found = False
 mid = (1+left+right)//2
 if count > (len(List)//2):
     return False
 if left < 0:
     return False
 if List[mid] == item:
     print("After",count,"tries")
     return True
 elif item <List[mid]:
     return BinarySearch(List,item,(count+1),left,mid-1)
 elif item> List[mid]:
     return BinarySearch(List,item,(count+1),mid+1,right)


SortedList = MergeSort(List)
search = BinarySearch(SortedList,17,0,0,len(SortedList))
print(search)
