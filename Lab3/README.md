# Algorithms part 3 Lab 3 wedd
## Task
![task image](https://github.com/thefreekley/Lab3-Algo3/blob/dev/task.png)

---

## io_data.py

### def input_data
1.Функція введення елементів:
```python
	def input_data(file_name):
    with open(file_name, 'r') as file:
        count=int(file.readline())
        couple = []
        for line in file.readlines():
            line_1,line_2 = line.split()
            couple.append(list((int(line_1),int(line_2))))

    return {'couple':couple,'count':count}
```
### def output_data
2. Функція виведення інформації в файл:
```python
	def output_data(file_name,value_to_write):
    with open(file_name,'w') as file:
        file.write(value_to_write)
```
		
## wedding.py

### def group_by_tribes
1. Групування списка людей на племена

```python
    def group_by_tribes(self):
        tribes = []
        for person in self.couple:
            for tribe in tribes:
                if person[1] in tribe:
                    tribe.add(person[0])
                    break
                if person[0] in tribe:
                    tribe.add(person[1])
                    break
            else:
                tribes.append(set((person[0], person[1])))

        return tribes
```
### def count_gender
2. Підрахунок кількості осіб чоловічого та жіночої статі в кожному племені
```python
    def count_gender(self,key):
        gender_in_tribe = []
        for tribe in self.tribes:
            index=0
            for person in tribe:
                if  key(person % 2): index+=1

            gender_in_tribe.append(index)

        return gender_in_tribe
```

### def count_combinations_pairs
3. Рахує всі можливі комбінації пар в племенах
```python
    def count_combinations_pairs(self):
        combinations = 0
        leftover_male = self.num_male_in_tribe

        for i in range(len(self.num_male_in_tribe)):
            for j in range(len(self.num_female_in_tribe)):
                if i == j: continue
                combinations += self.num_male_in_tribe[i]*self.num_female_in_tribe[j]

        return combinations
```

---
# Іnstalation
## Для реквестів:git clone https://github.com/thefreekley/Lab3-Algo3.git
## Для запуску: python main.py
