import fileinput
def main():
    arr = []
    hori = 0
    depth = 0
    for line in fileinput.input():
        arr.append(line)
    for i in range(0,len(arr)):
        direction = arr[i].split(" ")[0]
        magnitude = arr[i].split(" ")[1]
        #print(direction,magnitude)
        if(direction == 'forward'):
            hori += int(magnitude)
        elif(direction == 'up'):
            depth -= int(magnitude)
        elif(direction == 'down'):
            depth += int(magnitude)
    print(depth*hori)
main()
