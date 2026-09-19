from config import (
  ACTIONS,
  DAYS_PER_ACTION,
  SCHEDULE_KIND_ACTION,
  SCHEDULE_KIND_FIXED_EVENT,
  STATUS,
  CODE,
)

class ActionsServices:
  def __init__(self, store):
    self.store = store

  def findAllActions(self):
    return [
      { 'id': action.get('id'), 'name': action.get('name') }
      for action in ACTIONS
    ]

  def buildDayQueue(self, schedules):
    """
    스케줄 슬롯({ kind, id })을 일자 큐로 펼침.
    각 슬롯 = DAYS_PER_ACTION일.
    """
    dayQueue = []
    for item in schedules:
      if item is None:
        continue
      kind = item.get('kind')
      itemId = item.get('id')
      if kind not in (SCHEDULE_KIND_ACTION, SCHEDULE_KIND_FIXED_EVENT):
        continue
      dayQueue.extend([
        { 'kind': kind, 'id': itemId }
        for _ in range(DAYS_PER_ACTION)
      ])
    return dayQueue

  def applyDay(self, character, actionId, day=None):
    """
    액션 1일분만 반영. 이벤트 조회/저장은 하지 않음.
    (Phase 1에서 outcome·delta 계산 구현)
    """
    # TODO: getAction → rollOutcome → calcDayDelta → applyDelta
    return {
      'status': STATUS['SUCCESS'],
      'code': CODE['DATA_FETCHED'],
      'data': {
        'character': character,
        'day_log': {
          'type': 'action',
          'day': day,
          'action_id': actionId,
          'outcome': None,
          'delta': {},
        },
      },
    }
