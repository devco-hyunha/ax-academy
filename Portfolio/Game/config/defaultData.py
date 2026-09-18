from copy import deepcopy

from .constants import DEFAULT_STATS

# 데이터 생성을 위한 기본 row 스키마
DEFAULT_DATA = {
  'character': {
    'name': 'unknown',
    'turn': 0,
    'month': 1,
    'stats': deepcopy(DEFAULT_STATS),
    'history': [],
    'action_counts': {},
    'events_triggered': [],
    'ending': None,
  }
}
