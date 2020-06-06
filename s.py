import itertools
# game=[[0, 0, 0],
#       [0, 0, 0],
#       [0, 0, 0]]

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False
def game_board(game_map,player=0,row=0,column=0,just_display=False):
	try:
		if game_map[row][column]!=0:
			print('This position is already occupied! choose another')
			return game_map,False
		print('   0  1  2')
		if not just_display:
			game_map[row][column]=player


		for count,row in enumerate(game):
			print(count,row)
		return game_map,True

	except IndexError as e:
		print('are you sure you chose the value from 0 or 1 or 2,',e)
		return game_map, False
        
    
	except Exception as e:
		print('are you sure you chose the value from 0 or 1 or 2,',e)
		return game_map, False

play=True
players=[1,2]
while play:

    game_size = int(input("What size game TicTacToe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won=False
    game,_=game_board(game,just_display=True)
    player_choice=itertools.cycle(players)
    while not game_won:
        current_player=next(player_choice)
        print (f'current_player: {current_player}')
        played=False
        while not played:
        

	        column_choice=int(input('What column do you want to play? (0,1,2):'))
	        row_choice=int(input('What row do you want to play? (0,1,2):'))
	        game,played=game_board(game,current_player,row_choice,column_choice)
        if win(game):
            game_won=True
            again=input('The game is over, Would you like to play again? (Y/N) ')
            if again.lower()=='y':
                print('Restarting')
            elif again.lower()=='n':
                print('Bye ,come back later!!')
                play=False
            else:
                print('Not a valid input,plese write( y or n) ')
                play=False

