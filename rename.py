import argparse
from pathlib import Path
from os import system, name


# Functions
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def get_files(directory, recursive):
    if directory.is_dir():
        if recursive:
            return list(directory.rglob('*.*'))
        else:
            return list(directory.glob('*.*'))


# Argument setup
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='Root Directory')
parser.add_argument('-r', '--recursive', action='store_true')
args = parser.parse_args()

# Sets the root directory which is where the file renaming will start.
if args.directory is None:
    root_dir = Path.cwd()
else:
    root_dir = Path(args.directory)
    if not root_dir.is_dir():
        print(f'"{args.directory}" is not a valid directory.')

files = get_files(root_dir, args.recursive)

clear()
print('\nPython script used to change the names of many files.\n\n')
change = input('Enter what you would like to add: ')
while True:
    beginning_test = f'{change}{files[0].name}'
    end_test = f'{files[0].stem}{change}{files[0].suffix}'
    try:
        location = int(input('\nWhere would you like to add this?\n'
        f'1). Beginning -- ex. {beginning_test}\n'
        f'2). End -- ex. {end_test}\n'
        '3). Quit\n'
        '--> '))
        if 0 < location < 4:
            break
        else:
            raise ValueError
    except ValueError:
        print('That is not a valid answer.')

to_change = dict()

if location == 1:
    for f in files:
        file_name = f'{change}{f.name}'
        to_change[f] = f.with_name(file_name)
elif location == 2:
    for f in files:
        file_name = f'{f.stem}{change}{f.suffix}'
        to_change[f] = f.with_name(file_name)
elif location == 3:
    quit()

clear()
print('These are the files that will be changed.\n')
for key in to_change.keys():
    print(f'{key} -> {to_change[key]}')

if input('\nPlease type "YES" to make the changes: ') == 'YES':
    for item in to_change:
        item.rename(to_change[item])
        print(to_change[item])
    print('\nCompleted')
else:
    print('Aborting the name change.')