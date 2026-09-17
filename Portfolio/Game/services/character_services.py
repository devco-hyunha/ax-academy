from copy import deepcopy
from config import DEFAULT_DATA

class CharacterServices:
  def __init__(self, store):
    self.store = store
    self.playCharacter = None

  def createCharacter(self):
    self.playCharacter = deepcopy(DEFAULT_DATA['character'])
    return self.playCharacter

  def loadCharacter(self, id):
    # 샘플
    print(f'loadCharacter: {id}')
    self.playCharacter = deepcopy(DEFAULT_DATA['character'])
    return self.playCharacter

  def saveCharacter(self):
    pass

  def findAllCharacters(self):
    # 샘플
    sample_character = deepcopy(DEFAULT_DATA['character'])
    sample_character_list = [sample_character for _ in range(20)]
    return sample_character_list