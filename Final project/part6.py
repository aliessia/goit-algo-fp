items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            selected_items.append(item)
            total_calories += info['calories']
            budget -= info['cost']
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_selection = [[] for _ in range(budget + 1)]

    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                item_selection[current_budget] = item_selection[current_budget - cost] + [item]
    
    return item_selection[budget], dp[budget]


budget = 100


selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Загальна калорійність:", total_calories_greedy)


selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", selected_items_dp)
print("Загальна калорійність:", total_calories_dp)
