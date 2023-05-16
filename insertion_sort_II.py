def insertion_sort(Arr):

    N=len(Arr)
    #Arr=[11,10,4,9,21,2]

    for i in range(1,N):
        anchor=i

        while anchor>0 and Arr[anchor]<Arr[anchor-1]:
            Arr[anchor],Arr[anchor-1]=Arr[anchor-1],Arr[anchor]
            anchor-=1
    return Arr


if __name__=="__main__":
    Arr=[11,10,4,9,21,2]
    print(insertion_sort(Arr))

