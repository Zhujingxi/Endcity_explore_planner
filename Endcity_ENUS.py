import math
from tqdm import tqdm
import matplotlib.pyplot as plt

def distance_cal(cor1, cor2):
    x1, z1 = cor1
    x2, z2 = cor2
    return math.sqrt((x2 - x1) ** 2 + (z2 - z1) ** 2)

def generate_path(start_point, corlist, num_path):
    path = [corlist.pop(0)]

    with tqdm(total=num_path - 1) as pbar:
        for _ in range(1, num_path):
            min_distance = float('inf')
            min_index = -1
            for i, cor in enumerate(corlist):
                dist = distance_cal(path[-1], cor)
                if dist < min_distance:
                    min_distance = dist
                    min_index = i

            path.append(corlist.pop(min_index))
            pbar.update(1)

    return path

def plot_points_and_path(corlist, path):
    x_values, y_values = zip(*corlist)
    path_x_values, path_y_values = zip(*path)

    plt.plot(x_values, y_values, 'o', color='lightgray', label='All Points')
    plt.plot(path_x_values, path_y_values, '-o', color='red', label='Path')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    startx = input("Please input the X coordinate of the start point: ")
    startz = input("Please input the Z coordinate of the start point: ")

    start_point = [int(startx) if startx else 0, int(startz) if startz else 0]

    try:
        num_path = int(input("Please input the number of paths you want to explore: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit(1)

    shipOrNotIn = input("Please input 'Y' if you want to explore the ship, or 'N' otherwise: ")
    shipOrNot = shipOrNotIn.upper() == "Y"

    corlist = []

    with open("file.txt") as file:
        file.readline()
        for line in file:
            if "end_city" in line:
                seed, type, x, y, details = line.split(";", 4)
                x, y = int(x), int(y)
                if shipOrNot and "ship" in details or not shipOrNot:
                    corlist.append([x, y])
                    if shipOrNot:
                        print(line)

    path = generate_path(start_point, corlist, num_path)

    total_distance = sum(distance_cal(path[i], path[i+1]) for i in range(len(path)-1))
    distance_ratio = total_distance / num_path
    print(f"Total Distance: {total_distance:.2f}")
    print(f"Distance Ratio: {distance_ratio:.2f}")

    with open("output.txt", "w") as output_file:
        for counter, x in enumerate(path, 1):
            output_file.write(f"waypoint:{counter}:{counter}:{x[0]}:100:{x[1]}:11:false:0:gui.xaero_default:false:0:false\n")

    plot_points_and_path(corlist, path)

if __name__ == "__main__":
    main()
