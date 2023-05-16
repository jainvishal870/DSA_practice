'''
How to find the minimum cost to remove all elements from the array
'''


def minimum_cost(Arr):

    if len(Arr)==1:
        sum_total=Arr[0]
        
    else:
        Arr.sort(reverse=True)
        sum_total=0

        for element in range(len(Arr)):
            sum_total+= (element+1)*Arr[element]

    print(sum_total)


if __name__ == "__main__":
    Arr=[2,1,4]
    minimum_cost(Arr)



