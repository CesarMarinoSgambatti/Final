from json import *

def input_ID():
    while True:
        ID = input('ID: ')
        if len(ID) == 8:
            try:
                int(ID)
                return ID
            except:
                print('Error: ID must be a number !')
        else:
            print('Error: ID must have 8 digits !')

students = {'students': []}
try:
    with open('students.json', 'r') as f:
        students = load(f)
except:
    pass

while True:
    print('Commands:')
    print('    add - add a student')
    print('    search - search for a student by ID')

    cmd = input('> ')

    if cmd == 'add':
        students['students'].append({'name': input('Name: '), 'id': input_ID()})
        for i in range(len(students['students']) - 1):
            s = students['students'][i]
            if s['id'] == students['students'][-1]['id']:
                print('Error: Student with same ID already exists !')
                del students['students'][-1]
                break
        with open('students.json', 'w') as f:
            dump(students, f)

    elif cmd == 'search':
        ID = input_ID()
        for s in students['students']:
            if s['id'] == ID:
                print('Student found for ' + ID + ':  ' + s['name'])
                break
        else:
            print('Student ' + ID + ' not found !')

    else:
        print('Unknown command !')

    print('')
