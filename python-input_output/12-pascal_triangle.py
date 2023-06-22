#!/usr/bin/python3
"Task 12"


def pascal_triangle(n):
    """Representation of Pascal's triangle

    Args:
        n (integer): Number of rows

    Returns:
        List: with the values of the Pascal's triangle
    """
    pascal_base = [[1]]
    while len(pascal_base) != n:
        # this iterated variable takes from the second member of the list.
        iterated = pascal_base[-1]
        # This other list is initialized to a single member: 1
        pascal_row = [1]
        for index in range(len(iterated) - 1):
            # appending to pascal_row the actual value of i, + the next value
            pascal_row.append(iterated[index] + iterated[index + 1])
    # because pascal's triangle end with a 1, we append a literal 1 in the end
        pascal_row.append(1)
    # Now, we update the pascal base with the row containing the sumed values
        pascal_base.append(pascal_row)
    return pascal_base
