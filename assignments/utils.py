def display(data, padding=-1):
    """
        Display multidimensional list.
    """

    for i in range(len(data)):
        if len(data[i]) > 0 and isinstance(data[i][0], list):
            print " === {} ===".format(i)
            for j in range(len(data[i])):
                print '[', '\t'.join(map(lambda v: justify(v, padding), data[i][j])), ']'
        else:
            print '[', '\t'.join(map(lambda v: justify(v, padding), data[i])), ']'


def justify(value, padding):
    res = str(value)
    if padding > 0:
        res = res.rjust(padding)
    return res
