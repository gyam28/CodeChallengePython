"""
3. ICE CREAM MACHINE CHALLENGE:

Implement the IceCreamMachine's scoops method so that it returns all combinations
of one ingredient and one topping. If there are no ingredients or toppings,
the method should return an empty list.

For example,

IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops()

should return

[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].
"""

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        # YOUR CODE GOES HERE
        list =[]
        for x in self.ingredients:
            if x not in self.ingredients:
                list =[]
            for y in self.toppings:
                l = [x+" "+y]
                list.append(l)
                if y not in self.toppings:
                    list = []
        return list


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())
#should print
# [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())
# this should print
#[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce'], ['vanilla','orange'], ['chocolate','orange']]
