import os

tabs = 0
current_path = 'D:\PyProjects\/folder A'


def print_dir(path):
    global tabs
    tabs = tabs + 1

    dir_data = next(os.walk(path))
    tabs_for_dirname = ''

    for i in range(0, tabs):
        tabs_for_dirname += '    '
    print(tabs_for_dirname, '[', '\033[1m' + os.path.basename(dir_data[0]) + '\033[0m', ']')

    for subdir in dir_data[1]:
        print_dir(os.path.join(dir_data[0], subdir))

    tabs_for_dirname += '    '
    for file_name in dir_data[2]:
        print(tabs_for_dirname, file_name)

    tabs = tabs - 1


print_dir(current_path)
