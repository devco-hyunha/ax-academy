# 추후 schedule 루프에 연결할 이벤트 샘플 (mock)
# trigger: 발생 조건 / days_lost: 남은 행동 일수 감소 / effects: 스탯 보정

EVENTS = {
  'illness': {
    'id': 'illness',
    'name': '아픔',
    'message': '몸이 너무 아파 며칠을 누워 지내야 했다.',
    'trigger': {
      'stat': 'stress',
      'op': 'gte',
      'value': 100,
    },
    'days_lost': 5,
    'effects': {
      'stress': -30,
      'stamina': -5,
    },
  },
  'burnout': {
    'id': 'burnout',
    'name': '번아웃',
    'message': '멘탈이 한계에 달해 아무것도 손에 잡히지 않는다.',
    'trigger': {
      'stat': 'stress',
      'op': 'gte',
      'value': 100,
    },
    'days_lost': 3,
    'effects': {
      'stress': -20,
      'intelligence': -2,
    },
  },
}
