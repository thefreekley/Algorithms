from wedding import Wedding
from io_data import *
data = input_data('IO/wedding.in')
couple = data.get('couple')
count = data.get('count')

wedding_1 = Wedding(couple,count)

print(wedding_1)
result = wedding_1.__str__()

output_data('IO/wedding.out', result)

