import sys
from views import IntroViews, CharacterViews
from services import CharacterServices
from .schedule_controller import ScheduleController

class SceneController():
  def __init__(self, store):
    self.scheduleController = ScheduleController(store)
    self.characterServices = CharacterServices(store)

    self.introViews = IntroViews()
    self.characterViews = CharacterViews()

  def intro(self):
    while True:
      self.introViews.introTitle()
      menuChoice = self.introViews.introMenu()
      if menuChoice == 1:
        self.start()
      if menuChoice == 2:
        self.chooseSave()
      if menuChoice == 3:
        self.exit()

  def start(self):
    character = self.characterServices.createCharacter()
    if character:
      self.lobby(character)

  def chooseSave(self):
    saves = self.characterServices.findAllCharacters()

    self.characterViews.chooseSaveFileTitle()
    choice = self.characterViews.chooseSaveFile(saves) - 1
    if choice == len(saves):
      return
    else:
      character = self.characterServices.loadCharacter(choice)
      if character:
        self.lobby(character)

  def exit(self):
    print()
    print('Bye!')
    print()
    sys.exit(0)

  def lobby(self, character):
    while True:
      self.characterViews.title(character)
      self.characterViews.stats(character.get('stats'))

      if character.get('ending') is not None:
        print('end!')
        break

      choice = self.characterViews.menu()
      if choice == 1:
        self.scheduleController.scheduleSelection(character)
      if choice == 2:
        break