arr = [1,2,3,4,5,6,7,8,9]



def binary_search(arr:list, item:int):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1 # среднее больше чем искомый элеметнт отбрасываем все что справа от среднего(mid) и ищем там 
        else:
            low = mid + 1 # среднее меньше чем искомый элеметнт отбрасываем все что слева от среднего(mid) и ищем там 
    return None

print(binary_search(arr,-3))