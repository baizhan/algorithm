def short_bubble_sort(list):
    exchanges=True
    pass_num=len(list)-1
    while pass_num>0 and exchanges:
        exchanges=False
        for i in range(pass_num):
            if list[i]>list[i+1]:
                exchanges=True
                list[i],list[i+1]=list[i+1],list[i]
        pass_num=pass_num-1

if __name__=='__main__':
    list=[20,40,30,10,50]
    short_bubble_sort(list)
    print(list)
    
