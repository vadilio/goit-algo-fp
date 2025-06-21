# Завдання 7. Використання методу Монте-Карло

import random
import matplotlib.pyplot as plt

# Аналітична (теоретична) ймовірність сум (випадки з 36 можливих)
theoretical_probs = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}


def simulate_dice_rolls(n_rolls=1_000_000):
    frequency = {i: 0 for i in range(2, 13)}

    for _ in range(n_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        frequency[total] += 1

    # Перетворення частот на ймовірності
    probabilities = {k: v / n_rolls for k, v in frequency.items()}
    return probabilities


# Симуляція
n = 1_000_000
monte_carlo_probs = simulate_dice_rolls(n)

# Виведення таблиці
print(f"{'Сума':>5} | {'Монте-Карло':>12} | {'Теоретична':>12}")
print("-" * 37)
for i in range(2, 13):
    print(
        f"{i:>5} | {monte_carlo_probs[i]:>12.5f} | {theoretical_probs[i]:>12.5f}")

# Побудова графіка
sums = list(range(2, 13))
monte_values = [monte_carlo_probs[i] for i in sums]
theoretical_values = [theoretical_probs[i] for i in sums]

plt.figure(figsize=(10, 6))
plt.bar(sums, monte_values, width=0.4, label="Монте-Карло",
        align='center', color='skyblue')
plt.bar([x + 0.4 for x in sums], theoretical_values, width=0.4,
        label="Теоретичні", align='center', color='orange')
plt.xlabel("Сума двох кубиків")
plt.ylabel("Ймовірність")
plt.title(f"Порівняння ймовірностей (N={n})")
plt.xticks([x + 0.2 for x in sums], sums)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
