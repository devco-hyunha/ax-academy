import sys
from views import IntroViews, DisplaySavesViews
from services import CharacterServices

class SceneController():
  def __init__(self, store):
    self.characterServices = CharacterServices(store)
    self.introViews = IntroViews()
    self.displaySavesViews = DisplaySavesViews()

  def intro(self):
    while True:
      self.introViews.introTitle()
      menuChoice = self.introViews.introMenu()
      if menuChoice == 1:
        self.start()
        break
      if menuChoice == 2:
        self.displaySaves()
        continue
      if menuChoice == 3:
        self.exit()

  def start(self):
    print('new game!')

  def displaySaves(self):
    saves = self.characterServices.findAllCharacters()
    if len(saves) == 0:
      print('No saves found')

    self.displaySavesViews.displaySavesTitle()
    choice = self.displaySavesViews.displaySavesMenu(saves)
    if choice == len(saves):
      return
    else:
      self.characterServices.loadCharacter(choice)

  def exit(self):
    print()
    print('Bye!')
    print()
    sys.exit(0)

  def schduleSeletion():
    pass

  def viewStat():
    pass