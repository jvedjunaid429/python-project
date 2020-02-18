from random import randint
  
player = input('rock , paper  or scissors?')
if player == 'rock':
  print('O', end=' ')
  
elif player == 'paper':
  print('___', end=' ')
  
elif player == 'scissors':
  print('>8', end=' ')
  
else:
  print('??')
  
print('vs', end=' ')
chosen = randint(1,3)
if chosen == 1 :
  computer = 'rock'
  print('O')
  
elif chosen == 2 :
  computer = 'paper'
  print('___')
  
else:
  computer = 'scissors'
  print('>8')
if player == computer:
  print('DRAW!, try again to progress')
  
elif player == 'rock' and computer == 'scissors':
  print('Player wins!')
  
elif player == 'rock' and computer == 'paper':
  print('Computer wins!, try again to progress')
  
elif player == 'paper' and computer == 'rock':
  print('Player wins!')
  
elif player == 'paper' and computer == 'scissors':
  print('Computer wins!, try again to progress')

elif player == 'scissors' and computer == 'paper':
  print('Player wins!')
  
elif player == "scissors" and computer == 'rock':
  print('Computer wins! try again to progress')
else:
  print("huh?")