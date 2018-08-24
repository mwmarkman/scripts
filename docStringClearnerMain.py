# Cleans the docstrings of all .py files within a given directory (including all subdirectories)
# Fixes specific issue of no blank line between primary description and :param or :return values
# Also fixes subsequent tab issues created by adding a newline (see above)
# RUNNING MORE THAN ONCE ON THE SAME FILES IS BAD- ONLY RUN ONCE FOR CORRECT CLEANUP
#
# ***Causes the following docstring:***
#
# """Removes all duplicate PCR Reads
# :param: single or double: specify whether to remove duplicates for single or double end reads.
# Works on double end reads by default
# :param: max expected read length.
# """
#
# ***To be outputted as:***
#
# """Removes all duplicate PCR Reads
#
# :param: single or double: specify whether to remove duplicates for single or double end reads.
#      Works on double end reads by default
# :param: max expected read length.
# """
#
# Author: Matthew Markman, 2018

import os
import re


class DocstringCleaner:

    in_docstring = False
    loop_again = True
    last = None
    first_line = False
    path = ''

    def __init__(self, path):
        self.path = path

    @staticmethod
    def search_dir(path):
        for root, dirs, files in os.walk(path):
            for x_file in files:
                if x_file.endswith(".py"):
                    temp = os.path.join(root, x_file)
                    print(temp)
                    f = open(temp, 'r')
                    read_file = open(temp, 'r')
                    DocstringCleaner.fileparser(f, read_file, temp, 0, [], [])

    @staticmethod
    def fileparser(f, read_file, temp, line_count, newline_list, tab_list):
        for line in f:
            line_count += 1
            line = re.sub(r'\s+', '', line)
            if DocstringCleaner.in_docstring_checker(line):
                if DocstringCleaner.loop_again:
                    if DocstringCleaner.find_newline(line):
                        newline_list.append(line_count - 1)
                else:
                    if DocstringCleaner.find_tab(line):
                        tab_list.append(line_count)
            DocstringCleaner.last = re.sub(r'\s+', '', line)
        print("Newlines added: " + str(newline_list))
        print("Tabs added: " + str(tab_list))
        DocstringCleaner.alter_file(f, read_file, temp, newline_list, tab_list)
        DocstringCleaner.reset_globals()

    @staticmethod
    def in_docstring_checker(line):
        if line.count('"""') == 1 and not DocstringCleaner.in_docstring:
            DocstringCleaner.in_docstring = True
            DocstringCleaner.loop_again = True
        elif line.count('"""') == 1 and DocstringCleaner.in_docstring:
            DocstringCleaner.in_docstring = False
        return DocstringCleaner.in_docstring

    @staticmethod
    def find_newline(line):
        if ':par' in line or ':r' in line or ':typ' in line:
            DocstringCleaner.loop_again = False
            if DocstringCleaner.last is not None:
                if not ":par" in DocstringCleaner.last or ":r" in DocstringCleaner.last or ":typ" in DocstringCleaner.last:
                    if DocstringCleaner.last != "":
                        return True
        else:
            return False

    @staticmethod
    def find_tab(line):
        if DocstringCleaner.last is not None:
            if ':par' in DocstringCleaner.last or ':r' in DocstringCleaner.last or ':typ' in DocstringCleaner.last:
                if not line.startswith(":"):
                    return True
        else:
            return False

    @staticmethod
    def alter_file(f, read_file, temp, newline_list, tab_list):
        f.close()
        f_lines = read_file.readlines()
        insert_counter = 0
        read_file.close()
        for num in tab_list:  # tabs in correct lines
            line_holder = f_lines.pop(num - 1)
            f_lines.insert(num - 1, "    " + line_holder)
        for number in newline_list:  # adds newline chars in appropriate places
            f_lines.insert(number + insert_counter, "\n")
            insert_counter += 1
        insert_file = open(temp, 'w')
        insert_file.writelines(f_lines)
        insert_file.close()

    @staticmethod
    def reset_globals():
        DocstringCleaner.in_docstring = False
        DocstringCleaner.loop_again = True
        DocstringCleaner.last = None
        DocstringCleaner.first_line = False


def main(path):
    x = DocstringCleaner(path)
    x.search_dir(path)


if __name__ == "__main__":
    path = "/Users/MacProMatt/Desktop/blast"  # Switch file path here
    main(path)