from config import ACTIONS, MONTHLY_ACTIONS
from .system_views import SystemViews

class ScheduleViews:
  def __init__(self):
    pass

  @staticmethod
  def title(character, schedules):
    name = character.get('name')
    month = character.get('month')
    SystemViews.subtitle(f'{name}님의 {month}월 스케쥴 [{len(schedules)}/{MONTHLY_ACTIONS}]')

  @staticmethod
  def description(schedules):
    if len(schedules) > 0 :
      print()
      for index, actionId in enumerate(schedules):
        print(f'   {index + 1}. {ACTIONS[actionId].get("name")}')
      print()
      SystemViews.lineBreak()
    print(f'  이 달의 할 일 {MONTHLY_ACTIONS}개를 선택해 주세요')

  def chooseSchedule(self, schedules) -> int:
    self.description(schedules)
    print()

    menu = [item.get('name') for item in ACTIONS]
    menu.append('뒤로가기')
    SystemViews.menu(*menu)
    SystemViews.lineBreak()

    return SystemViews.choice(f'{len(schedules) + 1} 번째 스케쥴', len(menu))
