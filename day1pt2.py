import fileinput
def main(): 
    prev = 0
    curr = 0
    arr = []
    arrSums = []
    increased = 0

    for line in fileinput.input():
        arr.append(int(line))

    for i in range(0,len(arr)):
        if(i+2 < len(arr)):
            arrSums.append(arr[i] + arr[i+1] + arr[i+2])

    for j in range(0,len(arrSums)):
        curr = arrSums[j]
        if(prev != 0 and prev < curr):
            increased+=1
        prev = curr

    print(increased)
main()
