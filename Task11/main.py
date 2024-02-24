# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    melt = {'Sn': 232, 'Zn': 420, 'Fe': 1539, 'Ni': 1455, 'Si': 1415, 'Be': 1287};
    one_el = str(input());
    two_el = str(input());
    razn = (melt[one_el] - melt[two_el])
    print (razn);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
