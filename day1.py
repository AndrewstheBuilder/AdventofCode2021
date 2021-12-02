import fileinput
def main(): 
    prev = 0
    curr = 0
    increased = 0;
    for line in fileinput.input():
        curr = int(line)
        if(prev != 0 and prev < curr):
            increased+=1
        prev = curr
    print(increased)
main()
