import random

omikuji = ["大吉", "中吉", "笑吉"]

# idx = random.randint(0,2)

# result = omikuji[idx]
# result = random.randint(0, len(omikuji) - 1)
result = random.choice(omikuji)

print(f"今日の運勢は...{result}")

