
def calculate_color_code(major_index, minor_index):
    return major_index * 5 + minor_index

def print_color_map(major_index=None, minor_index=None):
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{calculate_color_code(i, j)} | {major} | {minor}')
            
    if major_index is not None and minor_index is not None:
        return calculate_color_code(major_index, minor_index)
    
    return len(major_colors) * len(minor_colors)


result = print_color_map()

assert(result == 25)

assert(calculate_color_code(1, 1) == 1)

assert(calculate_color_code(2, 3) == 8)

assert(calculate_color_code(3, 5) == 15)

assert(calculate_color_code(4, 2) == 17)

assert(calculate_color_code(5, 1) == 21)

print("All is well (maybe!)")
