from random import randint

repeat_rolling = True
while repeat_rolling:
    print("Тебе выпало число:", randint(1, 6))
    print("хочешь бросить кубик еще раз?(y/n)")
    repeat_rolling = ("y" or "yes") in input().lower()
