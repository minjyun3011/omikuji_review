# import random
# import time

# omikuji = ["大吉", "中吉", "笑吉"]

# print("今日の運勢は", end="",flush=True)

# for i in range(3):
#     time.sleep(1)
#     print(".", end="", flush=True)

# time.sleep(1)

# result = random.choice(omikuji)
# print(f"{result}")

# time.sleep(1)


# #ここからは『もう一度引く」と確認する処理をつくる
# retry = input("もう一度引く(y/n) > ")
# if retry == "y":
#     print("今日の運勢は", end="",flush=True)

#     for i in range(3):
#         time.sleep(1)
#         print(".", end="", flush=True)

#     time.sleep(1)

#     result = random.choice(omikuji)
#     print(f"{result}")

#     time.sleep(1)
#     retry = input("もう一度引く(y/n) > ")

# elif retry == "n":
#     print("ありがとうございました")

import random
import time

omikuji = ["大吉", "中吉", "笑吉"]

while True:
    print("今日の運勢は", end="", flush=True)

    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    time.sleep(1)

    result = random.choice(omikuji)
    print(f"{result}")

    time.sleep(1)

    while True:
        retry = input("もう一度引く(y/n) > ").lower()

        if retry == "n":
            print("ありがとうございました")
            exit()  # プログラムを終了する
        elif retry == "y":
            break  # もう一度運勢を表示するループに入り直す
        else:
            print("yかnを選択してください")
            continue


