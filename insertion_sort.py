def insertion_sort(list):
    for index in range(1,len(list)):
        current_value=list[index]
        position=index
        while position>0 and list[position-1]>current_value:
            list[position]=list[position-1]
            position=position-1
        list[position]=current_value
def insertion_sort_binary_search(list):
    for index in range(1,len(list)):
        current_value=list[index]
        position=index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)//2
            if list[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        while position>low:
            list[position]=list[position-1]
            position=position-1
        list[position]=current_value

list=[3,23,54,64,62,77,22,53]
insertion_sort(list)
print(list)
list=[3,23,54,64,62,77,22,53,99,59]
insertion_sort_binary_search(list)
print(list)
        
