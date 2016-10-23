"""
Run assertions of all file by calling main method of each file
"""

import mergesort
import quicksort
import binary_search
import binary_tree
import insertion_sort


def main():
    """
    Call main method of all files
    """
    mergesort.main()
    quicksort.main()
    binary_search.main()
    binary_tree.main()
    insertion_sort.main()


if __name__ == '__main__':
    main()
