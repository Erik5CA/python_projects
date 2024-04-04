import sys
import json
import clipboard

SAVED_DATA = 'clipboard.json'

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file)
        
def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    

if len(sys.argv)  == 2:
    command = sys.argv[1]
    # print(command)
    data = load_data(SAVED_DATA)
    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print('Data Saved!')
    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print('Key does not exist.')
    elif command == 'list':
        print('List of keys and values saved in the clipboard.')
        for key, value in data.items():
            print(f'{key} - {value}')
    else:
        print('invalid command')

else:
    print('Please pass exactly one command')