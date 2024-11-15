class House:
    
    def __init__(self, name, number_of_floors):
        
        self.name = name
        
        self.number_of_floors = number_of_floors

    def __len__(self):
        
        return self.number_of_floors

    def __str__(self):
        
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, floor):
        
        if 1 <= floor <= self.number_of_floors:
            
            print(f"Переход на этаж {floor} в доме '{self.name}'.")
            
        else:
            
            print(f"Эта квартира имеет только {self.number_of_floors} этажей. Невозможно перейти на этаж {floor}.")



h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)


print(h1)

print(h2)


print(len(h1))

print(len(h2))


h1.go_to(5)

h2.go_to(21)
