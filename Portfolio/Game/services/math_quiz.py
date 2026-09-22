# author: 오효정
"""임시 math_quiz stub.

팀원 math_quiz 구현이 오기 전까지 ImportError를 막고
중간/기말 이벤트가 동작하도록 간단한 산수 퀴즈를 제공합니다.
시그니처: runMathQuiz(difficulty, time_limit) -> int (맞힌 개수, 0~10)
"""
import random
import time

from views.system_views import SystemViews

QUESTION_COUNT = 10


def runMathQuiz(difficulty, time_limit):
    SystemViews.headline('수학 퀴즈')
    print(f'난이도: {difficulty} / 제한시간: {time_limit}초 (문항당)')
    print(f'{QUESTION_COUNT}문제를 풉니다.\n')

    score = 0
    for index in range(1, QUESTION_COUNT + 1):
        a, b, answer = _makeQuestion(difficulty)
        prompt = f'Q{index}. {a} + {b} = ?'
        started_at = time.time()
        raw = SystemViews.input(prompt)
        elapsed = time.time() - started_at

        if elapsed > time_limit:
            print(f'시간 초과! (정답: {answer})\n')
            continue

        try:
            user_answer = int(raw)
        except (TypeError, ValueError):
            print(f'오답! (정답: {answer})\n')
            continue

        if user_answer == answer:
            score += 1
            print('정답!\n')
        else:
            print(f'오답! (정답: {answer})\n')

    print(f'결과: {score}/{QUESTION_COUNT}점\n')
    return score


def _makeQuestion(difficulty):
    if difficulty == 'hard':
        a = random.randint(10, 99)
        b = random.randint(10, 99)
    else:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
    return a, b, a + b
