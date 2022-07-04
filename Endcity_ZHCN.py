import math

start_point = [0 , 0]
corlist = []
num_path = 0
path = []

already_list = []

def distance_cal (cor1,cor2):
    x1 = cor1[0]
    z1 = cor1[1]
    x2 = cor2[0]
    z2 = cor2[1]
    return math.sqrt(((x2-x1)**2)+((z2-z1)**2))

def which_cal(start):
    distance_list = []
    counter = 0
    for x in corlist:
        if x in path:
            pass
        else:
            distance_list.append([distance_cal(start,x),counter])
        counter += 1

    distance_list.sort(key=lambda distance_list:distance_list[0])
    #print("distance",distance_list[0])
    return distance_list[0][1]


startx = input("请输入起始坐标x: ")
startz = input("请输入起始坐标z: ")
num_path = int(input("请输入需要探索的个数: "))
while num_path is False:
    print("输入不合法")
    num_path = int(input("请输入需要探索的个数: "))

if startx is False:
    pass
else:
    start_point[0] = int(startx)

if startz is False:
    pass
else:
    start_point[1] = int(startz)


file = open(r".\file.txt")
file.readline()
while True:
    readline = file.readline()
    if readline:
        x,y=readline.split(",",1)
        x = int(x)
        y = int(y)
        corlist.append([x , y])
    else:
        break


path.append(corlist[which_cal(start_point)])

coutner = 1
while coutner < num_path:
    path.append(corlist[which_cal(path[-1])])
    coutner += 1

coutner = 1

output_file = open(r'.\output.txt', 'w')

for x in path:
    print("waypoint:", end='')
    output_file.write("waypoint:")
    print(coutner, end='')
    output_file.write(str(coutner))
    print(":", end='')
    output_file.write(":")
    print(coutner, end = '')
    output_file.write(str(coutner))
    print(":", end = '')
    output_file.write(":")
    print(x[0], end = '')
    output_file.write(str(x[0]))
    print(":100:", end='')
    output_file.write(":100:")
    print(x[1], end = '')
    output_file.write(str(x[1]))
    print(":", end='')
    output_file.write(":")
    print("11", end='')
    output_file.write("11")
    print(":false:0:gui.xaero_default:false:0:false", end='')
    output_file.write(":false:0:gui.xaero_default:false:0:false")
    print()
    output_file.write('\n')
    coutner += 1
output_file.close()
