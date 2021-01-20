
def input_data(file_name):
    with open(file_name, 'r') as file:
        count=int(file.readline())
        couple = []
        for line in file.readlines():
            line_1,line_2 = line.split()
            couple.append(list((int(line_1),int(line_2))))

    return {'couple':couple,'count':count}

def output_data(file_name,value_to_write):
    with open(file_name,'w') as file:
        file.write(value_to_write)