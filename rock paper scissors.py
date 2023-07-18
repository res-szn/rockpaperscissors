'''
    ROCK PAPER SCISSORS, MADE BY RESILIENCE MODIFIED AND IN CURRENT WORKS SO WON'T WORK AS EFFCIENTLY 
'''

import random
import os
import re


def check_play_status():
  valid_responses = ['yeah', 'nah']
  while True:
      try:
          response = input('Do you want to play again? (Yeah or Nah): ')
          if response.lower() not in valid_responses:
              raise ValueError('Yeah or Nah only')

          if response.lower() == 'yeah':
              return True
          else:
              os.system('cls' if os.name == 'nt' else 'clear')
              print('Thanks for playing!')
              exit()

      except ValueError as err:
          print(err)


def play_rps():
   play = True
   while play:
       os.system('cls' if os.name == 'nt' else 'clear')
       print('')
       print('Rock, Paper, Scissors - Shoot!')

       user_choice = input('Choose your weapon'
                           ' [R]ock], [P]aper, or [S]cissors: ')

       if not re.match("[SsRrPp]", user_choice):
           print('Please choose a letter:')
           print('[R]ock, [P]aper, or [S]cissors')
           continue

       print(f'You chose: {user_choice}')

       choices = ['R', 'P', 'S']
       opp_choice = random.choice(choices)

       print(f'I chose: {opp_choice}')

       if opp_choice == user_choice.upper():
           print('Tie!')
           play = check_play_status()
       elif opp_choice == 'R' and user_choice.upper() == 'S':
           print('Rock beats scissors, I win!')
           play = check_play_status()
       elif opp_choice == 'S' and user_choice.upper() == 'P':
           print('Scissors beats paper! I win!')
           play = check_play_status()
       elif opp_choice == 'P' and user_choice.upper() == 'R':
           print('Paper beats rock, I win!')
           play = check_play_status()
       else:
           print('You win!\n')
           play = check_play_status()


if __name__ == '__main__':
   play_rps()