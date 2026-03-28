print("게임에 오신 것을 환영합니다!")
weapon_level = 0
rate={
        "up":70,
        "keep":20,
        "down":7,
        "break":3,
    }
while True:
    choice = input("숫자를 입력하세요 (0을 입력하면 종료): ")
    if choice == "0":
        print("게임을 종료합니다.")
        break
    elif choice == "1":
        print("강화를 실행합니다!")
        weapon_level = weapon_level + 1
    else:
        print("잘못된 입력입니다.")
    upgrade_rates = [
        {"up": 70, "keep": 20, "down": 5, "break": 5},  # 레벨 0
        {"up": 60, "keep": 25, "down": 10, "break": 5},  # 레벨 1
        {"up": 50, "keep": 30, "down": 15, "break": 5},  # 레벨 2
        {"up": 40, "keep": 30, "down": 20, "break": 10},  # 레벨 3
        {"up": 30, "keep": 30, "down": 25, "break": 15},  # 레벨 4
    ]
import random






