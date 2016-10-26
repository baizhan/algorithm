def quick_sort(list):
    quick_sort_helper(list,0,len(list)-1)
def quick_sort_helper(list,first,last):
    if first<last:
        split_point=partition(list,first,last)
        quick_sort_helper(list,first,split_point-1)
        quick_sort_helper(list,split_point+1,last)

def partition(list,first,last):
    pivot_value=list[first]
    left_mark=first+1
    right_mark=last
    done=False
    while not done:
        while left_mark<=right_mark and list[left_mark]<=pivot_value:
            left_mark=left_mark+1
            print('left_mark:%s'%left_mark)
        while list[right_mark]>=pivot_value and right_mark>=left_mark:
            right_mark=right_mark-1
            print('right_mark:%s'%right_mark)
        if right_mark<left_mark:
            done=True

        else:
            temp=list[left_mark]
            list[left_mark]=list[right_mark]
            list[right_mark]=temp
            print('%s>%s'%(list[right_mark],list[left_mark]))
            print(list)
    temp=list[first]
    list[first]=list[right_mark]
    list[right_mark]=temp
    print('change first')
    print(list)
    return right_mark

list=[54,62,26,93,17,77,31,44,55,20]
quick_sort(list)
print(list)
