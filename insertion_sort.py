
def insertion_sort(Arr):

    #Arr=[12, 6, 2, 8]
    N=len(Arr)

    #need to compare if unsorted lement is greater then the sorted part
    #iterate over the unsorted part and compare iit with sorted elements

    for i in range(1,N):

        for j in range(i-1,-1,-1):
            if Arr[j]>Arr[j+1]:
                Arr[j+1],Arr[j]=Arr[j],Arr[j+1]

    
    return Arr

if __name__=="__main__":

    Arr=[10,4,25,1,5]

    print(insertion_sort(Arr))
