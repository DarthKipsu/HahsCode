import numpy as np

def read_data(path):
    """
    Returns tuple (data info, actual data)
    Modify according to what the actual data will be like :)
    """
    with open(path) as file:
        data = [[int(first) for first in line.split()] for line in file]
    data = np.array(data)
    return data[:1], data[1:]

def write_data(data, path):
    """
    writes the first ints of each row to file in given path
    Overwrites a previously existing file
    """
    f = open(path, "w+")
    for i in range(len(data)):
        f.write("%i\n" % data[i][0])
    f.close()
