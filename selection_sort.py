def selection_sort(list):
    for i in range(len(list)-1,0,-1):
        j=0
        for k in range(1,i+1):
            if list[k]>list[j]:
                j=k
        list[i],list[j]=list[j],list[i]

list=[54,26,93,17,77,31,44,55,20]
selection_sort(list)
print(list)
