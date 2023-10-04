

class FruitStore:
    def __init__(self, name, fruitPrices):
        self.fruitPrices = fruitPrices
        self.name = name
        print('Welcome to ' + name + ' fruit store!')
    
    def getCostPerKg(self, fruit):
        if fruit not in self.fruitPrices:
            return None
        return self.fruitPrices[fruit]
    def getPrecoCompras(self,shoppingList):
        totalCost = 0.0
        for fruit, numKgs in shoppingList:
            costPerKg = self.getCostPerKg(fruit)
        if costPerKg != None:
            totalCost += numKgs * costPerKg
            return totalCost
    def getNome(self):
        return self.nome


fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}

def buyFruit(fruit, weight):
    if fruit not in fruitPrices:
        print('We dont have ' + fruit + ' available')
    else:
        cost = fruitPrices[fruit] * weight
        print(str(weight) + 'kg of ' + fruit + ' cost ' + str(cost) + ' euros.')

def main():
    fruits = ['apples', 'oranges', 'pears', 'bananas']

    # for loops
    for fruit in fruits:
        print(fruit + ' for sale')

    for fruit, price in fruitPrices.items():
        if price < 2.00:
            print('%s cost %f' %(fruit, price))
        else:
            print(fruit + ' are too expensive!')

    # functions
    buyFruit('pears', 5)
    buyFruit('not_a_fruit', 10)
    buyFruit('apples', 3)

    # classes
    myStore = FruitStore('My Store', fruitPrices)
    print("Price of apples: " + str(myStore.getCostPerKg('apples')))
    print("Price of shopping list: " + str(myStore.getPrecoCompras([('apples', 3), ('pears', 5)])))
    

if __name__ == '__main__':
    main()