from io_data import *



def checking(file_name,coef,display):
    daily_food,number_hamsters,hamsters=input_data(file_name,coef)
    checked_humster=0
    total_greed = 0
    total_daily_norm = 0
    available_food=daily_food

    hamsters.head = hamsters.merge_sort(hamsters.head)
    last_available_food=0
    for i in range(number_hamsters):

        current = hamsters.get_element(i)

        total_greed += current.greed

        total_daily_norm += current.daily_norm

        checked_humster += 1
        last_available_food=available_food
        available_food = daily_food - (total_daily_norm + (checked_humster - 1) * (total_greed))
        if display: print(current)

        if available_food < 0:
            checked_humster -= 1
            return checked_humster


prev_checked_humster = checking('IO/hamstr.in',1,False)
checked_humster = checking('IO/hamstr.in',(prev_checked_humster-1),True)

print(checked_humster)


output_data('IO/hamstr.out', str(checked_humster))












