
contacts = {
    'number': 5,
    'students': [
        {'name': 'Sarah Holdersness', 'email': 'sarah@example.com'},
        {'name': 'Kristina Palmquist', 'email': 'kristina@example.com'},
        {'name': 'Hermione Granger', 'email': 'hermione@example.com'},
        {'name': 'Harry Potter', 'email': 'harry@example.com'},
        {'name': 'Ron Weasley', 'email': 'ron@example.com'},
    ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])
    