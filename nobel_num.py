'''
Arr=[-1, -3, 3, 5, -10, 4]

sorted_artr = [-10, -3, -1, 3, 4, 5]
count_small = 0,1,2,3,4,5
'''

def nobel_num(Arr):
    nobel=0
    nobel_arr=[]
    count_less=0
    Arr.sort(reverse=False)
    for ele in range(len(Arr)):

        if Arr[ele]!=Arr[ele-1]:
            count_less=ele

        if count_less==Arr[ele]:
            nobel+=1
            nobel_arr.append(Arr[ele])

    print(nobel,nobel_arr)



if __name__=="__main__":
    Arr1=[3,3,0,6,2,2]
    Arr=[1,1]
    #sorted_arr=[0,2,2,3,3,6]
    #count_less= 0,1,1,3,3,5

    nobel_num(Arr)


        