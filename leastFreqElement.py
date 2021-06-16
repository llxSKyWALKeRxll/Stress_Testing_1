import random, time

def findLeastFreqElementNaive(arr):
    leastCtr, leastElement = len(arr), -99
    for i in range(len(arr)):
        currentCtr = 0
        for j in range(len(arr)):
            if (arr[i] == arr[j]):
                currentCtr += 1
        if (currentCtr < leastCtr):
            leastCtr, leastElement = currentCtr, arr[i]
    return leastElement, leastCtr

def findLeastFreqElementSorting(arr):
    temp_arr, leastCtr, leastElement, currentCtr = arr.copy(), len(arr), -99, 1
    temp_arr.sort()
    for i in range(len(temp_arr) - 1):
        if (temp_arr[i] == temp_arr[i + 1]):
            currentCtr += 1
        else:
            if (currentCtr < leastCtr):
                leastCtr, leastElement = currentCtr, temp_arr[i]
            currentCtr = 1
    if (currentCtr < leastCtr):
        leastCtr, leastElement = currentCtr, temp_arr[len(temp_arr) - 1]
    return leastElement, leastCtr

def findLeastFreqElementMapping(arr):
    dictMap = {}
    for i in range(len(arr)):
        if (arr[i] in dictMap.keys()):
            dictMap[arr[i]] += 1
        else:
            dictMap[arr[i]] = 1
    leastElementCtr = min(dictMap.values())
    for i in dictMap:
        if dictMap[i] == leastElementCtr:
            leastElement = i
            break
    return leastElement, leastElementCtr
    

if __name__ == '__main__':
    testCases, testCase = 15, 0
    start = time.time()
    while (testCase < testCases):
        arr = []
        # n = random.randint(10, 20)
        n = 5000
        for i in range(n):
            arr.append(random.randint(100, 110))
        timeNaive1 = time.time()
        leastFreqElementNaive, ctr1 = findLeastFreqElementNaive(arr)
        timeNaive2 = time.time()
        timeSorting1 = time.time()
        leastFreqElementSorting, ctr2 = findLeastFreqElementSorting(arr)
        timeSorting2 = time.time()
        timeMapping1 = time.time()
        leastFreqElementMapping, ctr3 = findLeastFreqElementMapping(arr)
        timeMapping2 = time.time()
        print("======== Test case ", testCase, "========")
        print('Array:', arr)
        print('The least frequent element in the array is (NAIVE):', leastFreqElementNaive)
        print("Count of", leastFreqElementNaive, " (NAIVE):", ctr1)
        print(f"Time taken (NAIVE): {timeNaive2 - timeNaive1}")
        print('The least frequent element in the array is (SORTING):', leastFreqElementSorting)
        print("Count of", leastFreqElementSorting, " (SORTING):", ctr2)
        print(f"Time taken (SORTING): {timeSorting2 - timeSorting1}")
        print('The least frequent element in the array is (MAPPING):', leastFreqElementMapping)
        print("Count of", leastFreqElementMapping, " (MAPPING):", ctr3)
        print(f"Time taken (MAPPING): {timeMapping2 - timeMapping1}")
        testCase += 1
    end = time.time()
    print(f'Total time taken: {end - start}')

# if __name__ == "__main__":
#     arr = [17, 10, 11, 11, 10]
#     leastFreqElementMapping, ctr3 = findLeastFreqElementMapping(arr)
#     print("====OPTIMIZED ALGORITHM WITH MAPPING====")
#     print("Given array:", arr)
#     print("The least frequent element in the array is:", leastFreqElementMapping)
#     print("Count of", leastFreqElementMapping,":", ctr3)