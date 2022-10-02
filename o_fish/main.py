import math


today_is_day = 20

def on_start():
    print("1. Totals")
    print("2. Generic pacing stats")
    choice = input()
    if choice == "1":
        show_totals()
    if choice == "2":
        show_pacing_stats()


def show_totals():
    total = 0
    number_of_voyages = 0
    with open('read_values.txt') as f:
        for line in f:
            for i in line.split():
                number_of_voyages += 1
                value = int(i)
                total += value*1000
    print("Today is day ", today_is_day)
    print("total gained so far is ", total)
    remaining= 2000000-total
    days_left_at_current_rate = (math.ceil(remaining/50000))
    print("Days left at minimum pacing: ", days_left_at_current_rate)
    days_at_original_rate = 40-today_is_day
    days_left_at_sixty_rate = (math.ceil(remaining/60000))
    days_left_at_seventy_rate = (math.ceil(remaining/70000))
    days_left_at_eighty_rate = (math.ceil(remaining/80000))
    days_left_at_ninety_rate = (math.ceil(remaining/90000))
    days_left_at_not_happening_rate = (math.ceil(remaining/100000))
    print("Days left at 60k pace: ", days_left_at_sixty_rate)
    print("Days left at 70k pace: ", days_left_at_seventy_rate)
    print("Days left at 80k pace: ", days_left_at_eighty_rate)
    # print("Days left at... 90k pace: ", days_left_at_ninety_rate)
    # print("Days left at... 100k pace: ", days_left_at_not_happening_rate)
    print("Days I would have been left at original rate: ", days_at_original_rate)
    days_ahead = math.ceil(days_at_original_rate - days_left_at_current_rate)
    print("Days ahead: ", days_ahead)
    print("Total voyages: ", number_of_voyages)
    estimated_excess = number_of_voyages*300
    print("Total with estimated excess: ", estimated_excess+total)

def show_pacing_stats():
    goal = 2000000
    days_at_fifty = goal/50000
    print("Total days at ")

if __name__ == "__main__":
    on_start()