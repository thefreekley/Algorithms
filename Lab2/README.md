# Algorithms part 3 Lab 2 HAMSTERS 

Task
---

## io_data.py

### def input_data
1.Функція введення елементів в LinkedList та іншої інформації із файла:
```python
	def input_data(file_name):
    with open(file_name, 'r') as file:
        S=int(file.readline())
        C= int(file.readline())
        humster_bst = BST(lambda x: (x.daily_norm,x.greed))
        for line in file.readlines():
            line_1,line_2 = line.split()
            humster_bst.add(Hamster(int(line_1),int(line_2)))

    return S,C,humster_bst
```
### def output_data
2. Функція виведення інформації в файл:
```python
	def output_data(file_name,value_to_write):
    with open(file_name,'w') as file:
        file.write(value_to_write)
```

## linked_list.py

### def append
1.Функція додавання нового елемента (характеристики хом'яка) 
```python
          def append(self, new_value):

        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node
```

### def get_element
2.Функція знаходження елемента по індексу
```python
    def limit_element(self,key):
        if self.root is not None:
            current = self.root
            while key(current) is not None:
                current = key(current)
            return current
```
### def sorted_merge,def merge_sort,get_middle
3. Сортування злиттям
```python
    def sorted_merge(self, left_part, right_part):
        result = None

        if left_part == None:
            return right_part
        if right_part == None:
            return left_part

        if self.key(left_part.data) <= self.key(right_part.data):
            result = left_part
            result.next = self.sorted_merge(left_part.next, right_part)
        else:
            result = right_part
            result.next = self.sorted_merge(left_part, right_part.next)

        return result

    def merge_sort(self, head):

        if head == None or head.next == None:
            return head

        middle = self.get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head)

        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if (head == None):
            return head
```


## main.py

1.Денний запас їжі,кількість хом'яків і бінарне дерево пошуку 
з денною нормою та жадібністю кожного хом`яка з функції введення
```python
	daily_food,number_hamsters,hamsters=input_data('IO/hamstr.in')
```
2. Цикл для знаходження кількості хом`яків з найменшими запитами
   на їжу які зможуть жити на денний запас їжі
> available_food - залишок їжі
> total_greed - загальна кількість жадібності
> total_daily_norm - загальна потреба в їжі вибраних  хом'яків
> checked_humster - кількість вибраних хом'яків

```python 
for i in range(number_hamsters):

    current = hamsters.get_element(i)

    total_greed += current.greed

    total_daily_norm += current.daily_norm

    checked_humster += 1

    available_food = daily_food - (total_daily_norm + (checked_humster - 1) * (total_greed))

    if available_food < 0:
        checked_humster -= 1
        break
```
3. Виведення кількості можливих хом'яків
```python
	print(checked_humster)
	output_data('IO/hamstr.out', str(checked_humster))
```

---

# Іnstalation
## Для реквестів:git clone https://github.com/thefreekley/Lab2-Algo3.git
## Для запуску: python main.py
