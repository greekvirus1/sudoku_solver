def custom_size_list(s):
    '''
    returns list filled with 0s of size 's'
    :param s: int
    '''
    the_list = [0] * s
    return the_list

def custom_array_2d(x, y):
    '''
    returns 2d array of custom size
    :param x, y: int
    '''
    arr = [[0] * x for _ in range(y)] #wtf is this? - https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    return arr
