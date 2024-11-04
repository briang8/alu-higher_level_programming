#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # To keep track of the number of elements printed
    for i in range(x):  # Iterate up to x times
        try:
            print(my_list[i], end='')  # Print the element followed by a space
            count += 1  # Increment the count for each successful print
        except IndexError:
            break  # Exit the loop if an IndexError occurs (list index out of range)
    
    print()  # Print a newline after all elements have been printed
    return count  # Return the number of elements printed

result = safe_print_list([1, 2, 3, 4, 5], 10)
print("Number of elements printed:", result)
  