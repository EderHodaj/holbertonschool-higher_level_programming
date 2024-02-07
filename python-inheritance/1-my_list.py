#!/usr/bin/python3

'''
Python simple module
for demonstarative purpose
'''


class MyList(list):
    '''
    Class that inherits from list class
    '''

    def print_sorted(self):
        '''
        Instance method that prints the object array sorted
        '''
        sorted_list = sorted(self)
        print(sorted(self))
        return sorted_list
