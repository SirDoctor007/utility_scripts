from pathlib import Path
from datetime import date
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == '__main__':

    today = str(date.today())
    year, week, _ = date.today().isocalendar()

    templates_dir = Path('S:/Programming/Python/EventMgr/Templates/')
    events_dir = Path('S:/Programming/Python/EventMgr/Events/')

    if not Path.is_dir(templates_dir):
        Path.mkdir(templates_dir, parents=True)

    if not Path.is_dir(events_dir):
        Path.mkdir(events_dir, parents=True)

    # Gets the event ID
    while True:
        try:
            event_id = int(input('\nEnter the event ID: '))
            break
        except ValueError:
            print('That was not a valid event ID.')

    # Grabs the templates and gives the user the options
    files = dict()
    counter = 1
    for item in templates_dir.iterdir():
        if item.is_file():
            files[counter] = item
            counter += 1

    # clear()
    while True:
        print('\nSelect a template to use.')
        for file in files:
            print(f'{file}) {files[file].name}')
        try:
            file_item = int(input('--> '))
            if file_item in files.keys():
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            print('That was not a valid answer.')

    # Gets the template data
    with open(files[file_item], 'r') as f:
        template_data = f.readlines()

    template_data[0] = str(event_id) + template_data[0][10:]
    if files[file_item].stem == 'Other':
        category = input('Enter the event category: ')
        template_data[0] = template_data[0].replace('[CATEGORY]', category)
    else:
        category = files[file_item].stem

    file_name = f'{event_id}_Notes.txt'

    event_path = Path(events_dir, f'{year}/Week_{week}/{today}_{event_id}_{category}/')

    if not Path.is_dir(event_path):
        Path.mkdir(Path(event_path, 'Snapshots'), parents=True)

    file_path = Path(event_path, file_name)

    with open(file_path, 'w') as f:
        f.writelines(template_data)

    print(f'\nEvent notes created at {file_path}')
