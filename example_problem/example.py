
def read_data(path):
    with open(path) as file:
        data = [line.split() for line in file]
    print(data[0])
    return data

def write_data(data, path):
    f = open(path, "w+")
    f.write("%s\n" % len(data))
    for i in range(len(data)):
        f.write("%s\n" % data[i])
    f.close()

def solve(path):
    data = read_data(path)
    output = []
    for x in range(1, len(data)):
        lineStart = -1
        for y in range(int(data[0][1])):
            if data[x][0][y] == '#':
                if lineStart < 0:
                    lineStart = y
            else:
                if lineStart >= 0:
                    output.append("PAINT_LINE %i %i %i %i" % (x-1,lineStart,x-1,y-1))
                    lineStart = -1
        if lineStart >= 0:
            output.append("PAINT_LINE %i %i %i %i" % (x-1,lineStart,x-1,int(data[0][1])-1))
    return output

write_data(solve("learn_and_teach.in"), "learn_and_teach.out")
write_data(solve("logo.in"), "logo.out")
write_data(solve("right_angle.in"), "right_angle.out")
