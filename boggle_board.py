import random 

class BoggleBoard:

  dice_list = []
  for i in range(16):
    die = []
    for x in range(6):
      die.append((chr(random.randint(ord('A'), ord('Z')))))
    dice_list.append(die)
    random.shuffle(dice_list)

  def __init__(self):
    board = ''
    for x in range(16):
      if x % 4 == 0:
        board += '\n'
      board += '_'
    board += '\n'
    print(*board)

  def shake(self):
    board = ''
    new_letter = ''
    for i,x in enumerate(BoggleBoard.dice_list):
      if i % 4 == 0:
        board += '\n'
      new_letter = x[random.randint(0,5)]
      if new_letter == 'Q':
        board += new_letter + 'u '
      else:
        board += new_letter + '  ' 
    board += '\n'
    # print(*board)
    print('{:}'.format(board))

board_new = BoggleBoard()
board_new.shake()