from .system_views import SystemViews
from config import TOTAL_MONTHS
class DisplaySavesViews(SystemViews):
  def __init__(self):
    
    pass

  @staticmethod
  def displaySavesTitle():
    SystemViews.headline('저장 파일 목록')
    print()

  @staticmethod
  def displaySavesMenu(list) -> int:
    save_list = []
    for i, character in enumerate(list):
      if character is not None and i < 8:
        ending = character.get('ending')
        ending_text = f" / 엔딩: {ending}" if ending else ''
        name = character.get('name')
        saved_text = f"{name if name else 'unknown'} "
        saved_text += f"- {character.get('month')}월 "
        saved_text += f"(턴 {character.get('turn')}/{TOTAL_MONTHS}){ending_text}"
        save_list.append(saved_text)

    save_list.append('뒤로가기')
    SystemViews.menu(*save_list)
    return SystemViews.choice('저장 파일 선택', len(save_list))

