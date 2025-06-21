# Завдання 6. Жадібні алгоритми та динамічне програмування

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм:


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    selected = {}

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            selected[name] = info
            total_cost += info["cost"]
            total_calories += info["calories"]

    return selected, total_cost, total_calories

# Динамічне програмування (аналог задачі про рюкзак):


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    # dp[i][w] — максимальна калорійність при i перших предметах і бюджеті w
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення вибору
    w = budget
    selected = {}
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, info = item_list[i - 1]
            selected[name] = info
            w -= info["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(info["cost"] for info in selected.values())
    return selected, total_cost, total_calories


budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Страви:", greedy_result[0])
print("Вартість:", greedy_result[1], "Калорійність:", greedy_result[2])

print("\nДинамічне програмування:")
print("Страви:", dp_result[0])
print("Вартість:", dp_result[1], "Калорійність:", dp_result[2])
