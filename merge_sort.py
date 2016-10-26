def merge_sort(list):
    print('splitting',list)
    if len(list)>1:
        mid=len(list)//2
        left_half=list[:mid]
        right_half=list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                list[k]=left_half[i]
                i=i+1
                print('1:%d'%i)
            else:
                list[k]=right_half[j]
                j=j+1
                print('2:%d'%j)
            k=k+1
        while i<len(left_half):
            list[k]=left_half[i]
            i=i+1
            k=k+1
            print('3:%d'%i)
            print('4:%d'%k)
        while j<len(right_half):
            list[k]=right_half[j]
            j=j+1
            k=k+1
            print('5:%d'%k)
    print('merging',list)
list=[54,26,93,17,77,31,44,55,20]
merge_sort(list)
print(list)
            
