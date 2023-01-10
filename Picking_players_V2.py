import pandas as pd
import random

def all_players():
    
    df = pd.read_excel('all_players.xlsx')
    
    names = list(df.Name)
    
    overalls = list(df.Overall)
    
    players = {}
    
    for i in range(len(names)):
        players[names[i]] = overalls[i]
        
    return players

def random_first(user1, user2):
    
    coin = random.randint(0,1)
    
    if coin == 0:
        return user1
    else:
        return user2

def select_player(user, all):

    
    while True:
        
        player = {}

        choice = input ('Select player: ')
        
        if choice in all:

            value = all.get(choice)
            player[choice] = value


            break
            
            
        else:
            print('Please enter correct name.')
            continue
    
    user[choice] = value
    
    return user

def delete_player(user1, user2, all):
    
    for user in user1:
        if user in all:
            del all[user]
            
    for user in user2:
        if user in all:
            del all[user]
    
    
    return all

def check_overall(user):
    
    #can have 1 superstar
    superstar = 0

    #can have 2 players 85-90 overall
    allstar = 0

    #can have 3 players 80-84 overall
    star = 0

    #can have 4 players 73-79 overall
    bench = 0

    #can have 2 players MAX 72 overall
    role_player = 0


    for i in user:

        if user[i] > 90:

            superstar += 1

        elif 91 > user[i] > 84:

            allstar += 1
            
        elif 85 > user[i] > 79:

            star += 1

        elif 80 > user[i] > 72:

            bench += 1

        elif user[i] < 73:

            role_player += 1       


    if user[i] > 90 and superstar < 2:

        print(f'You added {list(user)[-1]} with overall {user[i]}')
        return True

    elif user[i] > 90 and superstar > 1:

        print('You already have 1 player above 90 overall')
        print(f'Now you tried to add {list(user)[-1]} with overall {user[i]}')
        print('Try again.')
        user.popitem()
        return False


    if 91 > user[i] > 84 and allstar < 3:

        print(f'You added {list(user)[-1]} with overall {user[i]}')
        return True
                
    elif 91 > user[i] > 84 and allstar > 2:

        print('You already have 2 players between 90-85 overall')
        print(f'Now you tried to add {list(user)[-1]} with overall {user[i]}')
        print('Try again.')
        user.popitem()
        return False

    elif 85 > user[i] > 79 and star < 4:

        print(f'You added {list(user)[-1]} with overall {user[i]}')
        return True

    elif 85 > user[i] > 79 and star > 3:

        print('You already have 3 players between 84-80 overall')
        print(f'Now you tried to add {list(user)[-1]} with overall {user[i]}')
        print('Try again.')
        user.popitem()
        return False

    elif 80 > user[i] > 72 and bench < 5:

        print(f'You added {list(user)[-1]} with overall {user[i]}')
        return True

    elif 80 > user[i] > 72 and bench > 4:

        print('You already have 4 players between 79-73 overall')
        print(f'Now you tried to add {list(user)[-1]} with overall {user[i]}')
        print('Try again.')
        user.popitem()
        return False

    elif user[i] < 73 and role_player < 3:

        print(f'You added {list(user)[-1]} with overall {user[i]}')
        return True

    elif user[i] < 73 and role_player > 2:

        print('You already have 2 player under 73 overall')
        print(f'Now you tried to add {list(user)[-1]} with overall {user[i]}')
        print('Try again.')
        user.popitem()
        return False

all = all_players()

user1 = {}
user2 = {}
i = 0

turn = random_first(user1, user2)

#print(all)

for i in range(24):


    if turn == user1:

        print("Marius, your turn")
        
        while True:

            print('Select option:')
            print('1. My team')
            print('2. Select new player')
            print('3. All free players')
            print('4. Superstars 91+ overall')
            print('5. Allstars 85-90 overall')
            print('6. Stars 80-84 overall')
            print('7. Bench 73-79 overall')
            print('8. Role players 72 and lower overall')
            choice = (input('Select option: '))

            if choice == '1':
                print('Your team is:')
                print(user1)

            elif choice == '2':
                user1 = select_player(user1, all)
        
                if check_overall(user1):

                    all = delete_player(user1, user2, all)
                
                    turn = user2

                    break

                else:

                    continue

            elif choice == '3':
                print('All free players:')
                print(all)

            elif choice == '4':
                for i in all:
                    if all[i] > 90:
                        print(i)

            elif choice == '5':
                for i in all:
                    if 91 > all[i] > 84:
                        print(i)

            elif choice == '6':
                for i in all:
                    if 85 > all[i] > 79:
                        print(i)

            elif choice == '7':
                for i in all:
                    if 80 > all[i] > 72:
                        print(i)

            elif choice == '8':
                for i in all:
                    if all[i] < 73:
                        print(i)

            else:
                print('Picked wrong number.\n Try again.')
                continue


    elif turn == user2:

        print("Paulius, your turn")

        while True:

            print('Select option:')
            print('1. My team')
            print('2. Select new player')
            print('3. All free players')
            print('4. Superstars 91+ overall')
            print('5. Allstars 85-90 overall')
            print('6. Stars 80-84 overall')
            print('7. Bench 73-79 overall')
            print('8. Role players 72 and lower overall')
            choice = (input('Select option: '))

            if choice == '1':
                print('Your team is:')
                print(user2)

            elif choice == '2':
                user2 = select_player(user2, all)
        
                if check_overall(user2):

                    all = delete_player(user1, user2, all)
                
                    turn = user1

                    break

                else:

                    continue

            elif choice == '3':
                print('All free players:')
                print(all)

            elif choice == '4':
                for i in all:
                    if all[i] > 90:
                        print(i)

            elif choice == '5':
                for i in all:
                    if 91 > all[i] > 84:
                        print(i)

            elif choice == '6':
                for i in all:
                    if 85 > all[i] > 79:
                        print(i)

            elif choice == '7':
                for i in all:
                    if 80 > all[i] > 72:
                        print(i)

            elif choice == '8':
                for i in all:
                    if all[i] < 73:
                        print(i)

            else:
                print('Picked wrong number.\n Try again.')
                continue