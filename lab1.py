
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    
    if int_list == None:
        raise ValueError
    if len(int_list) == 0:
        return None
    maxval = int_list[0]
    for int in int_list:
        if int > maxval:
            maxval = int
        elif int <= maxval:
            pass
    return maxval 
   

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""

    if int_list == None:
        raise ValueError
    x = len(int_list) - 1
    if int_list == []:
        return []
    if len(int_list) == 1:
        return int_list
    else:
        return [int_list[x]] + reverse_rec(int_list[:-1])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError
    if int_list == []:
        return None
    midpoint = (low + high) //2
    if int_list[midpoint] == target:
        return midpoint
    if high<low and int_list[midpoint] != target:
        return None
    elif int_list[midpoint] > target:
        high = midpoint - 1
        return bin_search(target,low,high,int_list)
    elif int_list[midpoint] < target:
        low = midpoint + 1
        return bin_search(target,low,high,int_list)
   
 
