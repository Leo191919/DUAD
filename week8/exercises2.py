import csv
import os


def add_game(name, gender, developer, clasification_esrb):

    game={
        'name': name,
        'gender': gender,
        'developer': developer,
        'clasification_esrb':clasification_esrb,
    }
    return game

def save_tsv ( games_list, file_name = 'games.tsv' ):
    try:
        if not games_list:
            print('The list of games is empty. No file will be saved.')
            return 
        with open(file_name,'w', newline= '', encoding = 'utf-8' )as file_tsv:
            fields = games_list[0].keys()
            writer_tsv=csv.DictWriter(file_tsv, fieldnames=fields, delimiter='\t')

            writer_tsv.writeheader()

            writer_tsv.writerows(games_list)
        print(f'The data has been successfully saved in {file_name}')

    except Exception as e:
        print(f'Error saving TSV file: {e}')


def request_data():
    name= input('Please, input the name of video game: ' )
    gender = input('Please, input the gender of video game: ' )
    developer= input('Please, input the developer of  video game: ' )
    clasification_esrb= input('Please, input the clasification ESRB of video game: ' )
    return add_game(name,gender,developer, clasification_esrb)

games_list=[]


while True: 
    games_list.append( request_data())
    answer=input('would you want add another game? (yes /no): ')
    if answer.lower()!='yes':
        break

save_tsv(games_list)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_relative= os.path.join(current_dir, 'games_relative.tsv')
save_tsv(games_list,file_path_relative)