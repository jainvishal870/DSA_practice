#Bruteforce approach
def sort_n_1(Arr):

    for ind in range(len(Arr)-1,0,-1):

        if Arr[ind] < Arr[ind-1]:
            #swap
            Arr[ind],Arr[ind-1]=Arr[ind-1],Arr[ind]

    return Arr



if __name__=="__main__":

    Arr=[2,3,10,14,20,4]

    print(sort_n_1(Arr))