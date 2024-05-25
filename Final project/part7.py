import random
import matplotlib.pyplot as plt

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def monte_carlo_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice1, dice2 = roll_dice()
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1

    probabilities = {sum_: count / num_rolls * 100 for sum_, count in sums_count.items()}
    return probabilities

def theoretical_probabilities():
    probabilities = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
    return {sum_: prob * 100 for sum_, prob in probabilities.items()}

def plot_probabilities(monte_carlo_probs, theoretical_probs):
    sums = list(range(2, 13))
    monte_carlo_vals = [monte_carlo_probs[sum_] for sum_ in sums]
    theoretical_vals = [theoretical_probs[sum_] for sum_ in sums]

    plt.figure(figsize=(10, 6))
    plt.bar(sums, monte_carlo_vals, alpha=0.6, label='Monte Carlo')
    plt.plot(sums, theoretical_vals, color='red', marker='o', label='Theoretical')

    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability (%)')
    plt.title('Probability of Sums from Rolling Two Dice')
    plt.legend()
    plt.grid(True)
    plt.show()


num_rolls = 100000
monte_carlo_probs = monte_carlo_simulation(num_rolls)
theoretical_probs = theoretical_probabilities()


print("Монте-Карло ймовірності:")
for sum_, prob in monte_carlo_probs.items():
    print(f"{sum_}: {prob:.2f}%")

print("\nТеоретичні ймовірності:")
for sum_, prob in theoretical_probs.items():
    print(f"{sum_}: {prob:.2f}%")


plot_probabilities(monte_carlo_probs, theoretical_probs)
