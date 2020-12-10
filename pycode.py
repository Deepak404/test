
def bubblesort(list):
    '''each pair of adjacent elements is compared and the elements are swapped if they are not in order.'''


    for iter_num in range(len(list)-1,0,-1):

        for idx in range(iter_num):
            if list[idx]>list[idx+1]:

                list[idx+1], list[idx] = list[idx], list[idx+1]

            print(list)
        print("\n")


if __name__ == "__main__":
    list = [19,2,31,45,6,11,121,27]
else:
    list = [int(x) for x in input("Enter Numbers to be sorted:").split()]

bubblesort(list)
print('Hello')
