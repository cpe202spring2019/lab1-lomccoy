
def max_list_iter(int_list):  # must use iteration not recursion
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
   
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   pass

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   pass
