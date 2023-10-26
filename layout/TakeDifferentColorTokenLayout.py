from layout.GameLayout import GameLayout


def take_different_color_token_cli(board_stock, active_player):
    
    #initalize lists
    list_choice_player = []
    list_stock = []
    for x in board_stock:
        if board_stock[x] > 0:
            list_stock.append(x)

    #ask player choice
    while len(list_stock) > 0 and len(list_choice_player) < 3:
        for i in range(len(list_stock)):
            print(i + 1, " : ", list_stock[i])

        try:
            choice = int(input("enter the number of the desired color :"))
            if choice < 1:
                raise ValueError("no negative value")
            list_choice_player.append(list_stock[choice - 1])
            del list_stock[choice - 1]

        except:
            print("Enter a valid value")

    #pass player choice to called method parameters
    token_param = {
        "blue": False,
        "red": False,
        "green": False,
        "black": False,
        "white": False
    }

    for x in list_choice_player:
        token_param[x] = True

    game.take_different_color_token.execute(active_player,
                                       token_param["blue"],
                                       token_param["green"],
                                       token_param["red"],
                                       token_param["black"],
                                       token_param["white"])

game = GameLayout()

#launch and get game
game.game_start.execute(2)
game_state = game.query.show_game_state()


#test take different tokens function
take_different_color_token_cli(game_state.board.stock.__dict__, 0)
game_state = game.query.show_game_state()
print(game_state.board.stock)
print(game_state.player_list[0].stock)
