from play.game import GameService

game = GameService()
n_players = 7

# Setting up the table
game.set_table(n_players)

game.deal_cards()

for player in game.players:
    assert len(player.dealt_set) == int(2*52 / n_players)
