my_set = {1, 3, 5}

# List within dictionaries
my_dict = {'name': 'Jose', 'age': 90, 'grades': [13, 15, 66, 90]}
# Could be numbers
another_dict = { 1:15, 2:75, 3:150 }

# Example a tuple within dictionaries
'''
lottery_player = {
    'name': 'Rolf',
    'numbers': (13, 14, 45, 66, 23, 56)
}
'''

lottery_players = [
    {
        'name': 'Rolf',
        'numbers': (13, 14, 45, 66, 23, 56)
    },
    {
        'name': 'John',
        'numbers': (1, 2, 3, 4, 5)
    }
]


# Example list of dictionaries
universities = [
    {
        'name': 'oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

#r = sum(lottery_player['numbers'])

#lottery_player['name'] = 'Ismael'

r = lottery_players[0].total()
r2 = lottery_players.total()

print(r)
print(r2)

