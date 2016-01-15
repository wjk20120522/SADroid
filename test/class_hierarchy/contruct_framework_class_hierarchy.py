import os
import re


class_hierarchy_framework = {}

if __name__ == "__main__":

    T = Test()
    T.get_class()
    T.parse_file_in_directory()

    if 'parents' in class_hierarchy_framework['Landroid/widget/TextView.java'].keys():
        print class_hierarchy_framework['Landroid/widget/TextView.java']

    print T.count


