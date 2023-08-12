import random

def choice():
    player_choice=input("Enter your choice: Rock, Paper, or Scissors ")
    computer_choice=random.choice(['rock','paper','scissors'])
    choice_dict={'player':player_choice,'computer':computer_choice}
    return choice_dict

def compare(player,computer):
    print(f'You chose {player} and computer chose {computer}')
    if player.lower()==computer.lower():
        return 'It\'s a tie'
    elif player.lower()=='rock':
        if computer.lower()=='scissors':
            return 'You won!'
        else:
            return 'Computer won.'
    elif player.lower()=='paper':
        if computer.lower()=='rock':
            return 'You won!'
        else:
            return 'Computer won.'
    elif player.lower()=='scissors':
        if computer.lower()=='paper':
            return 'You won!'
        else:
            return 'Computer won.'
    else:
        return 'Invalid choice! Choose either Rock, Paper or Scissors only. '
    
print("Let\'s Play Rock Paper Scissors Game! ")
data=choice()
print(compare(data['player'],data['computer']))