import json
import os

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

# 1
def create_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)  
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        json.dump(content, file, indent=4)

# 2
def read_file(directory, filename):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'r') as file:
        return json.load(file)

# 3
def update_file(directory, filename, new_content):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        json.dump(new_content, file, indent=4)

# 4
def write_dict_to_file(directory, filename, data_dict):
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        json.dump(data_dict, file, indent=4)


create_file('chess_players', 'players.json', chess_players)


players = read_file('chess_players', 'players.json')
print("საწყისი მოთამაშეები:", players)


new_entries = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]


update_file('chess_players', 'players.json', players + new_entries)


write_dict_to_file('chess_players', 'new_players.json', new_entries)
