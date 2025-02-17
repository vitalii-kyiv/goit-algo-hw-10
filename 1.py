from pulp import LpMaximize, LpProblem, LpVariable

def optimize_production():
    """
    Оптимізує виробництво напоїв "Лимонад" та "Фруктовий сік", 
    щоб максимізувати загальну кількість вироблених одиниць, враховуючи обмежені ресурси.
    
    Обмеження ресурсів:
    - Вода: 100 одиниць
    - Цукор: 50 одиниць
    - Лимонний сік: 30 одиниць
    - Фруктове пюре: 40 одиниць

    Витрати ресурсів:
    - 1 одиниця "Лимонаду" вимагає: 2 од. води, 1 од. цукру, 1 од. лимонного соку.
    - 1 одиниця "Фруктового соку" вимагає: 2 од. фруктового пюре, 1 од. води.

    Використовує бібліотеку PuLP для розв'язання задачі лінійного програмування.

    Повертає:
        tuple: Оптимальна кількість виробництва ("Лимонад", "Фруктовий сік").
    """
    
    # Створення моделі
    model = LpProblem(name="maximize_production", sense=LpMaximize)

    # Змінні рішення: кількість вироблених одиниць "Лимонаду" та "Фруктового соку"
    lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
    fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

    # Функція цілі: максимізація загальної кількості вироблених продуктів
    model += lemonade + fruit_juice, "Total_Products"

    # Обмеження ресурсів
    model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
    model += (1 * lemonade <= 50), "Sugar_Constraint"
    model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
    model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

    # Розв'язання моделі
    model.solve()

    # Отримання результатів
    lemonade_produced = lemonade.varValue
    fruit_juice_produced = fruit_juice.varValue

    return lemonade_produced, fruit_juice_produced

# Виконання функції та вивід результату
optimal_lemonade, optimal_fruit_juice = optimize_production()
print(f"Лимонад: {optimal_lemonade}, Фруктовий сік: {optimal_fruit_juice}")
