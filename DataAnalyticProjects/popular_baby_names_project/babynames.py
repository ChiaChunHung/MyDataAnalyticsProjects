"""
File: babynames.py
Name: Chia-Chun Hung
--------------------------
This project simulates how a back-end engineer organizes
the collected rankings of popular baby names from various years
into a dictionary data structure.
It also allows users to search for names by entering a partial string,
retrieving all names in the dictionary that match the entered substring.
"""

import sys


# 3
def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        name_data[name] = {year: rank}
    else:
        if year in name_data[name]:                       # 名字在裡面且年份重複出現
            # rank 比大小，並決定是否重新賦值
            if int(name_data[name][year]) <= int(rank):   # 注意：因為原始資料是str，比str會變成比ASCII而非比數值，故應把資料轉int()！
                pass
            else:
                name_data[name][year] = rank
        else:                                             # 名字在裡面但年份不重複
            name_data[name][year] = rank


# 2
def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    switch = True
    with open(filename, 'r') as f:
        for line in f:
            if switch:
                year = line.strip()
                switch = False
            else:
                lst = line.split(',')  # 注意delimiter到底是啥！原文本中，切割工具是逗號！非space!；注意.split()後的Data Type是list
                rank = lst[0].strip()
                name1 = lst[1].strip()
                name2 = lst[2].strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


# 1
def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


# 4
def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    matching_names = []

    # 抓出每筆name
    for name in name_data:

        # loop over每筆name去確認有無相同片段字串
        switch = False
        for i in range(len(name)-len(target)+1):
            if name[i: i+len(target)].lower() == target.lower():
                switch = True

        # loop over check is there is a match?
        if switch:  # 代表有遇到相同字串片段，把這個資料蒐集進names list
            matching_names.append(name)

    return matching_names


def print_names(name_data):
    """
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
