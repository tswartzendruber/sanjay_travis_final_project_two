import csv
import random

players = []


def get_players() -> list:
    """
    Function to open and read the csv file containing NBA players and their information
    :return: list containing every player's information from the csv file
    """
    global players
    database = open('database.csv', 'r', encoding='utf-8-sig')

    content = csv.reader(database, delimiter=',')
    for line in content:
        players.append(line)

    database.close()

    return players


def randomizer() -> list:
    """
    Function to randomly choose an NBA player from the pool of players
    :return: list containing a randomly chosen NBA player and their information
    """
    player_pool = get_players()
    random_number = random.randint(1, len(player_pool)-1)
    generated_player_info = player_pool[random_number]

    return generated_player_info


def guessing() -> None:
    """
    Function to compare the guessed player's information to the randomly generated information and direct the user in
    the right direction :return: nothing
    """
    random_player_info = randomizer()
    guesses = 1
    current_guess = input('Guess 1: ')

    while guesses <= 7:
        if current_guess != random_player_info[0]:
            # Finding the information of guessed player
            for line in players:
                if (line[0] != current_guess) and (line != players[-1]):
                    continue
                elif line[0] == current_guess:
                    current_guess_info = line
                    print(current_guess_info)

                    # Conference
                    if current_guess_info[1] == random_player_info[1]:
                        print('You got the conference right.')
                    else:
                        print('You got the conference wrong')

                    # Division
                    if current_guess_info[2] == random_player_info[2]:
                        print('You got the division right.')
                    else:
                        print('You got the division wrong.')

                    # Team
                    if current_guess_info[3] == random_player_info[3]:
                        print('You got the team right.')
                    else:
                        print('You got the team wrong.')

                    # Height
                    current_guess_height = current_guess_info[4].split('-')
                    random_player_height = random_player_info[4].split('-')

                    current_guess_feet = int(current_guess_height[0])
                    current_guess_inches = int(current_guess_height[1])

                    random_player_feet = int(random_player_height[0])
                    random_player_inches = int(random_player_height[1])

                    if current_guess_height == random_player_height:
                        print('You got the height right.')
                    elif ((random_player_feet == current_guess_feet) and (
                            random_player_inches > current_guess_inches)) or (random_player_feet > current_guess_feet):
                        print('The player we are looking for is taller than your guessed player.')
                    elif ((random_player_feet == current_guess_feet) and (
                            random_player_inches < current_guess_inches)) or (random_player_feet < current_guess_feet):
                        print('The player we are looking for is shorter than your guessed player.')

                    # Age
                    current_guess_age = int(current_guess_info[5])
                    random_player_age = int(random_player_info[5])
                    if random_player_age == current_guess_age:
                        print('You got the age right.')
                    elif random_player_age > current_guess_age:
                        print('The player we are looking for is older than your guessed player')
                    elif random_player_age < current_guess_age:
                        print('The player we are looking for is younger than your guessed player')

                    # Jersey No.
                    current_guess_jersey = int(current_guess_info[6])
                    random_player_jersey = int(random_player_info[6])

                    if random_player_jersey == current_guess_jersey:
                        print('You got the jersey number right.')
                    elif random_player_jersey > current_guess_jersey:
                        print('The player we are looking for has a higher jersey number than your guessed player.')
                    elif random_player_jersey < current_guess_jersey:
                        print('The player we are looking for has a lower jersey number than your guessed player.')

                    # Position
                    if current_guess_info[7] == random_player_info[7]:
                        print('You got the position right.')
                    else:
                        print('You got the position wrong.')

                    guesses += 1
                    print('Incorrect')
                    current_guess = input(f'Guess {guesses}: ')

                    break
                else:
                    guesses += 1
                    print('Player not found.')
                    current_guess = input(f'Guess {guesses}: ')
                    break
        else:
            break

    # Guess 8
    if current_guess == random_player_info[0]:
        print('Correct!')
    else:
        print(f'Sorry! The player we were looking for was {random_player_info[0]}')
