def start():
  print('Enter "R" to roll the dice')
  print('Enter "E" to stop the Roll')
  value=input('Enter your choice:- ')
  return value

def rolling():
  import random
  print(random.randrange(1,6))

print('Rolling Dice Simulator...')
print('Press Enter to start the simulation...')

while (1):
  value=start()

  if(value=='R'):
    rolling()
  elif(value=='E'):
    print('Dice Simulator Stopped')
    break
  else:
    print('Invalid Input')
    break

