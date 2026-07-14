from system.initialization_system.load_game_content import LoadGameContent
from system.entity_system.player_system.create_player import CharacterCreation
from system.progression_system.direction_point import DirectionPoint

LoadGameContent.start()

creation = CharacterCreation()
player = creation.start()

def start_game():

    direction = DirectionPoint(player)
    direction.run()
start_game()