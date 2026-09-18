from config import ACTIONS, TOTAL_MONTHS
from views import ScheduleViews
from services import CharacterServices

class ScheduleController():
  def __init__(self, store):
    self.characterServices = CharacterServices(store)
    self.scheduleViews = ScheduleViews()

  def scheduleSelection(self, character):
    cancel = False
    while not cancel and character.get('ending') is None:
      schedules = []
      while len(schedules) < 1:
      # while len(schedules) < MONTHLY_ACTIONS:
        self.scheduleViews.title(character, schedules)
        actionId = self.scheduleViews.chooseSchedule(schedules) - 1
        if actionId == len(ACTIONS):
          cancel = True
          break
        else:
          schedules.append(actionId)

      if cancel:
        break

      if character.get('month') < TOTAL_MONTHS:
        self.nextMonth(character)
        # todo: 이번달 스케쥴 종료 뷰
        print('할 일 종료!')
        print('다음 달로 넘어갑니다.')
      else:
        self.endGame(character, 'ending')
        # todo: 엔딩 뷰
        print('엔딩을 맞이합니다!')
        print()
        break

  def nextMonth(self, character):
    character['month'] += 1
    self.characterServices.saveCharacter(character)

  def endGame(self, character, ending):
    character['ending'] = ending
    self.characterServices.saveCharacter(character)