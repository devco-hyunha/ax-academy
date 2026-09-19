from time import sleep

from config import (
  TOTAL_MONTHS,
  MONTHLY_ACTIONS,
  DAY_PAUSE_SECONDS,
  SCHEDULE_KIND_ACTION,
  SCHEDULE_KIND_FIXED_EVENT,
  STATUS,
)
from views import ScheduleViews, CharacterViews
from services import ActionsServices, CharacterServices, EventServices


class ScheduleController:
  def __init__(self, store):
    self.actionsServices = ActionsServices()
    self.characterServices = CharacterServices(store)
    self.eventServices = EventServices(store)
    self.scheduleViews = ScheduleViews()
    self.characterViews = CharacterViews()
    self.isCancel = False

  def scheduleSelection(self, character):
    self.isCancel = False
    actions = self.actionsServices.findAllActions()

    while not self.isCancel and character.get('ending') is None:
      month = character.get('month')
      schedules = self.initializeSchedules(month)

      while None in schedules:
        currentIndex = schedules.index(None)
        self.scheduleViews.title(
          character.get('name'),
          month,
          currentIndex + 1,
          MONTHLY_ACTIONS,
        )
        menuIndex = self.scheduleViews.chooseSchedule(
          schedules, actions, currentIndex,
        ) - 1

        if menuIndex == len(actions):
          self.setCanceled()
          break

        selectedAction = actions[menuIndex]
        schedules[currentIndex] = {
          'kind': SCHEDULE_KIND_ACTION,
          'id': selectedAction.get('id'),
          'name': selectedAction.get('name'),
        }

      if self.isCancel:
        break

      self.runMonth(character, schedules)

      if month < TOTAL_MONTHS:
        self.nextMonth(character)
      else:
        self.endGame(character, 'ending')
        break

  def initializeSchedules(self, month):
    schedules = [None] * MONTHLY_ACTIONS
    result = self.eventServices.getCalendarEvents(month)
    fixedEvents = result.get('data') or [] if result.get('status') != STATUS['ERROR'] else []

    for fixed in fixedEvents:
      slot = int(fixed.get('slot', 0)) - 1
      if slot < 0 or slot >= MONTHLY_ACTIONS:
        continue
      schedules[slot] = {
        'kind': SCHEDULE_KIND_FIXED_EVENT,
        'id': fixed.get('id'),
        'name': fixed.get('name'),
      }
    return schedules

  def setCanceled(self):
    self.isCancel = True
    self.scheduleViews.setCanceled()
    print()

  def runMonth(self, character, schedules):
    dayQueue = self.actionsServices.buildDayQueue(schedules)
    self.scheduleViews.monthStart(character.get('month'))
    self.runDayQueue(character, dayQueue)

  def runDayQueue(self, character, dayQueue):
    """
    컨트롤러 오케스트레이션:
    - pending 있으면 EventService만 (재조회 없음)
    - fixed_event면 고정 일정 1일
    - action이면 Actions → Event 발생 판정 → pending 세팅
    - 매일 Character 저장 (saveCharacter)
    """
    for day, item in enumerate(dayQueue, start=1):
      dayLog = None

      if character.get('pending_event'):
        eventResult = self.eventServices.applyEventDay(character)
        if eventResult.get('status') == STATUS['ERROR']:
          break
        payload = eventResult.get('data') or {}
        character = payload.get('character') or character
        dayLog = payload.get('day_log')
      elif item.get('kind') == SCHEDULE_KIND_FIXED_EVENT:
        fixedResult = self.eventServices.applyFixedEventDay(
          character, item.get('id'), day,
        )
        if fixedResult.get('status') == STATUS['ERROR']:
          break
        payload = fixedResult.get('data') or {}
        character = payload.get('character') or character
        dayLog = payload.get('day_log')
      else:
        actionResult = self.actionsServices.applyDay(
          character, item.get('id'), day,
        )
        if actionResult.get('status') == STATUS['ERROR']:
          break
        payload = actionResult.get('data') or {}
        character = payload.get('character') or character
        dayLog = payload.get('day_log')

        foundResult = self.eventServices.findTriggeredEvent(character)
        found = (foundResult.get('data')
                 if foundResult.get('status') != STATUS['ERROR']
                 else None)
        if found:
          character['pending_event'] = self.eventServices.toPendingEvent(found)

      # 팀원 CharacterService 구현 대기 — 호출 자리만 유지
      self.saveCharacter(character)

      if dayLog:
        print(dayLog)
      sleep(DAY_PAUSE_SECONDS)

  def nextMonth(self, character):
    self.scheduleViews.monthEnd(character.get('month'))
    self.characterViews.stats(character.get('stats'))
    
    character['month'] += 1
    self.saveCharacter(character)
    self.scheduleViews.nextMonth()

  def endGame(self, character, ending):
    # todo: 엔딩 뷰
    print('엔딩을 맞이합니다!')
    print()

    character['ending'] = ending
    self.saveCharacter(character)

  def saveCharacter(self, character):
    self.characterServices.saveCharacter(character)
