from .system_views import SystemViews

class ScheduleViews:
  """표시 전용. 조회는 하지 않고 컨트롤러가 넘긴 값만 사용."""

  def __init__(self):
    pass

  @staticmethod
  def title(name, month, currentSlot, monthlyActions):
    SystemViews.subtitle(
      f'{name}님의 {month}월 스케쥴 [{currentSlot}/{monthlyActions}]'
    )

  @staticmethod
  def slotLabel(item):
    if item is None:
      return '(미선택)'
    return item.get('name')

  def description(self, schedules, currentIndex):
    print()
    for index, item in enumerate(schedules):
      print(f'   {index + 1}. {self.slotLabel(item)}')
    print()
    SystemViews.lineBreak()

    print(f'  {currentIndex + 1}번째 스케줄을 선택해 주세요')

  def chooseSchedule(self, schedules, actions, currentIndex) -> int:
    self.description(schedules, currentIndex)
    print()

    menu = [item.get('name') for item in actions]
    menu.append('뒤로가기')
    SystemViews.menu(*menu)
    SystemViews.lineBreak()

    return SystemViews.choice(f'{currentIndex + 1} 번째 스케쥴', len(menu))

  def monthStart(self, month):
    print(f'{month}월 일정을 시작합니다')
    print()

  def monthEnd(self, month):
    SystemViews.lineBreak()
    SystemViews.subtitle(
      f'{month}월 일정이 종료되었습니다!',
      '캐릭터 정보를 확인해 주세요',
    )
    print()

  def nextMonth(self):
    SystemViews.input('엔터를 누르면, 다음 달로 넘어갑니다')

  def setCanceled(self):
    SystemViews.errorMessage('스케쥴 선택을 취소했습니다')
    print()