# 단어를 맞추는 게임 / 글자 하나씩 추측해서 맞추면 공개 / 틀리면 남은 목숨,시도가 줄어드는 방식
import random

def initiate_game(game_level: str) -> tuple[int, str, str, str, str]:
    answer_list = [
        {'hint': 'fruit', 'answer': 'banana'},
        {'hint': 'fruit', 'answer': 'apple'},
        {'hint': 'fruit', 'answer': 'mango'},
        {'hint': 'fruit', 'answer': 'orange'},
        {'hint': 'fruit', 'answer': 'pineapple'},

        {'hint': 'animal', 'answer': 'elephant'},
        {'hint': 'animal', 'answer': 'kangaroo'},
        {'hint': 'animal', 'answer': 'lion'},
        {'hint': 'animal', 'answer': 'tiger'},
        {'hint': 'animal', 'answer': 'bear'},

        {'hint': 'country', 'answer': 'korea'},
        {'hint': 'country', 'answer': 'america'},
        {'hint': 'country', 'answer': 'japan'},
        {'hint': 'country', 'answer': 'australia'},
        {'hint': 'country', 'answer': 'china'},

        {'hint': 'computer-language', 'answer': 'python'},
        {'hint': 'computer-language', 'answer': 'java'},
        {'hint': 'computer-language', 'answer': 'javascript'},
        {'hint': 'computer-language', 'answer': 'kotlin'},
        {'hint': 'computer-language', 'answer': 'ruby'},
    ]
    rand = random.randint(0, len(answer_list) - 1)
    hint = answer_list[rand].get('hint')
    answer = answer_list[rand].get('answer')
    opened_answer = '_' * len(answer)
    levels = {
        '1': (10, 'easy',hint,answer,opened_answer),
        '2': (5, 'normal',hint,answer,opened_answer),
        '3': (3, 'hard',hint,answer,opened_answer),
    }
    try:
        return levels[game_level]

    except KeyError:
        raise ValueError('Invalid game level')
def not_in_answer(guess : str,answer : str) -> bool:
    if guess not in answer :
        return True
    else :
        return False
def check_answer(guess : str, opened_answer : str, answer : str, tries : int) -> tuple[str,str,int] :
    tries -= 1
    updated_opened_answer = ''
    if not_in_answer(guess, answer) :
        return f'{guess} is not in ANSWER, Try again', opened_answer, tries
    else :
        for i in range(len(answer)) :
            if guess == answer[i]:
                updated_opened_answer += guess
            else :
                updated_opened_answer += opened_answer[i]
        return f'{guess} is in ANSWER!',updated_opened_answer, tries


game_trials = 0
while True :
    game_trials += 1
    if game_trials >= 2:
        start_yn= input('Do you want to play again? (y/n) : ')
    else :
        start_yn = input('Do you want to play the game? (y/n) : ')

    if start_yn.lower() != 'y' :
        break
    else :
        selected_game_level = input('Choose a game level [1 - easy / 2 - normal / 3 - hard] : ')
        left_trials, selected_game_mode, hint, answer, opened_answer = initiate_game(selected_game_level)
        print(f"Start {game_trials}th game. - level : {selected_game_mode}")

    while True:
        print(f"HINT: {hint} , ANSWER : {opened_answer}, LEFT_TRIALS : {left_trials}")
        guess = input('GUESS : ')
        result, opened_answer, left_trials = check_answer(guess, opened_answer, answer, left_trials)
        print(f"RESULT: {result}")
        if left_trials == 0 and opened_answer == answer :
            print('======YOU LOSE!======')
            print(f'======SUMMARY======')
            print(f'left_trials : {left_trials}, opened_answer : {opened_answer}')
            print(f'======ANSWER======')
            print(f'answer : {answer}')
            print('========================')
            break
        elif opened_answer == answer :
            print('======YOU WIN!======')
            print(f'======SUMMARY======')
            print(f'left_trials : {left_trials}, opened_answer : {opened_answer}')
            print(f'======ANSWER======')
            print(f'answer : {answer}')
            print('========================')
            break