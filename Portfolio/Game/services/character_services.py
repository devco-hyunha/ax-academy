from copy import deepcopy
from config import DEFAULT_DATA

class CharacterServices:
  def __init__(self, store):
    self.store = store

  def createCharacter(self):
    return deepcopy(DEFAULT_DATA['character'])

  def loadCharacter(self, id):
    # 샘플
    print(f'loadCharacter: {id}')
    return deepcopy(DEFAULT_DATA['character'])

  def saveCharacter(self, character):
    pass

  def findAllCharacters(self):
    # 샘플
    sample_character = deepcopy(DEFAULT_DATA['character'])
    sample_character_list = [sample_character for _ in range(20)]

    return sample_character_list[:8]