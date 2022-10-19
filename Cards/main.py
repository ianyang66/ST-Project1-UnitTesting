
# Homework 2 - Python


from Card.cards import play_war_game

result = play_war_game()
print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
if result[0] != "Tie":
    print(result[0], "wins")
else:
    print("TIE!")