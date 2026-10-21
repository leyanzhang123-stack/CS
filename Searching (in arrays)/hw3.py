# Both array element access and modification are O(1) 
# because the index is already known. 
# Using the index, the computer can calculate the exact memory address directly 
# (address = base + index × element_size) 
# and go straight to that position — no need to look at any other elements. 
# The number of steps is always the same regardless of array size