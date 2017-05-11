""" This file is part of the File I/O exercise.

It should be used with the two input files, fruits_1.txt and fruits_2.txt."""


def open_and_read_file(filename):
    """Opens file as a file object and returns list of contents."""

    # Write your code below.
    open_file = open(filename)
    read_file = open_file.read()
    print open_file
    open_file.close()
    print open_file
    strip_file = read_file.strip()
    split_file = strip_file.split("\n")

    return split_file

def compare(lst1, lst2):
    """Takes in two lists and returns a list of items in common. """
    comparison_lst = []
    for i in lst1:
        if i in lst2:
           comparison_lst.append(i)
  
    return comparison_lst

    # Write your code below.



# Call your functions at the bottom, after they've been defined.

lst1 = open_and_read_file("fruits_1.txt")
lst2 = open_and_read_file("fruits_2.txt")
# print lst1
# print lst2
comparison_lst = compare(lst1, lst2)
print comparison_lst
