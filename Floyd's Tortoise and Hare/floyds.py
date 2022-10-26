
# This program is an example of floyds tortoise and hare algorithm where, in this example, it searches for a duplicate number in a list

# Duplicate always present, only 1 number is repeated n times

# Alternate methods could be hash map (high storage complexity) or sorting and checking neighbours

"""
The idea behind the algorithm is that, if you have two pointers in a linked list, one moving twice as fast (the hare) than the other (the tortoise), then if they intersect, there is a cycle in the linked list. If they don't intersect, then there is no cycle.
"""


input_list = [3,2,1,4,5]


def findDuplicate(list):
    # Initialise both points at index 0
    tortoise = list[0]
    hare = list[0]

    # cycle through the list until both points are on the same value
    while True:
        tortoise = list[tortoise]
        hare = list[hare]
        if tortoise == hare:
            # Break out the loop
            break

    # Work back through the index between the start and the tortoise to find the value that is duplicated
    point1 = 0
    point2 = tortoise
    while point1 != point2:
        # Cycle the list until they reach the mid point between start and tortoise
        point1 = list[point1]
        point2 = list[point2]

    # Return the duplicate number
    return point1

    # There is always a duplicate so no checking if value None

print(findDuplicate(input_list))