# Do mergesort and count the number of inversions in the list

def mergesort(arr):

    inversions = 0

    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        data1 = mergesort(L)
        data2 = mergesort(R)
        inversions += data1[1] + data2[1]
        L = data1[0]
        R = data2[0]

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = R[j]
                j += 1
                inversions += len(L) - i
            else:
                arr[k] = L[i]
                i += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return (arr, inversions)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
data = mergesort(arr)
print(data[1])