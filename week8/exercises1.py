import csv 
import os 

def add_video_game(name, gender, developer, clasification_esrb):
    videogame={
        'name': name,
        'gender': gender,
        'desarrollador':developer,
        'clasification_esrb': clasification_esrb,
    }
    return videogame


def save_csv( videogames_list,file_name='videogames.csv' ):
    try:
        if not videogames_list:
            print( 'The list of video games is empty. No files will be saved' )
            return

        with open(file_name, 'w', newline='', encoding='utf_8') as file_csv:
            fields = videogames_list[0].keys()
            writer_csv=csv.DictWriter(file_csv,fieldnames=fields)

            writer_csv.writeheader()

            writer_csv.writerows(videogames_list)
        print(f'Data saved correctly in {file_name}')

    except Exception as e:
        print(f'Error saving CSV file: {e}')


def request_data_of_videogames():
    name=input('Please, input the name of the video game: ' )
    gender= input('Please, input the gender of the video game: ')
    developer= input('Please, input the developer of the video game: ')
    clasification_esrb = input('Please, input the clasification_esrb of the video game: ')
    return add_video_game(name,gender, developer, clasification_esrb)

video_games = []


while True:
    video_games.append(request_data_of_videogames())
    answer = input( 'Would you like to add another video game (yes/no): ')
    if answer.lower() !='yes':
            break


save_csv(video_games)

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_relative = os.path.join(current_dir,'videogames_relative.csv')
save_csv(video_games, file_path_relative)

