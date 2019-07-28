def set_min_max(x, min_max, min_max_new):
    x -= min_max[0]
    min_max[1] -= min_max[0]
    min_max_new[1] -= min_max_new[0]
    x = (x / min_max[1]) * min_max_new[1] + min_max_new[0]
    return x
    
def reverse_range(x, min_max):
    return min_max[1] - x + min_max[0]

def is_in_range(x, min_max, limits = ['c', 'c']):
    if min_max[0] < min_max[1]:
        if limits[0] == 'c':
            if limits[1] == 'c':
                if x >= min_max[0] and x <= min_max[1]:
                    return True
                else:
                    return False
            elif limits[1] == 'o':
                if x >= min_max[0] and x < min_max[1]:
                    return True
                else:
                    return False
        elif limits[0] == 'o':
            if limits[1] == 'c':
                if x > min_max[0] and x <= min_max[1]:
                    return True
                else:
                    return False
            elif limits[1] == 'o':
                if x > min_max[0] and x < min_max[1]:
                    return True
                else:
                    return False
    else:
        if limits[0] == 'c':
            if limits[1] == 'c':
                if x <= min_max[0] and x >= min_max[1]:
                    return True
                else:
                    return False
            elif limits[1] == 'o':
                if x <= min_max[0] and x > min_max[1]:
                    return True
                else:
                    return False
        elif limits[0] == 'o':
            if limits[1] == 'c':
                if x < min_max[0] and x >= min_max[1]:
                    return True
                else:
                    return False
            elif limits[1] == 'o':
                if x < min_max[0] and x > min_max[1]:
                    return True
                else:
                    return False
                    
def range_lerp(min_max, t):
    x = min_max[0] + (min_max[1] - min_max[0]) * t
    return x

def find_lerp(x, min_max):
    return set_min_max(x, min_max, [0, 1])
    
def clamp(x, min_max):
    if x < min_max[0]:
        return min_max[0]
    if x > min_max[1]:
        return min_max[1]
    return x

