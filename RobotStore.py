class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self, count):
        if self.quantity >= count:
            return True
        return False

    def totalCost(self, amt):
        return self.price * amt

    def rmQuantity(self, amt):
        self.quantity -= amt
        return self.quantity

products = [("Ultrasonic range finder", 2.50, 4,'p1'), ("Servo motor            ",14.99,10,'p2'),
        ("Servo controller       ",44.95,5,'p3'),("Microcontroller Board  ",34.95,7,'p4'),
        ("Laser range finder     ",149.99,2,'p5'),("Lithium polymer battery",8.99,8,'p6')]
p1,p2 = Product(products[0][0],products[0][1],products[0][2]),Product(products[1][0],products[1][1],products[1][2])
p3,p4 = Product(products[2][0],products[2][1],products[2][2]),Product(products[3][0],products[3][1],products[3][2])
p5,p6 = Product(products[4][0],products[4][1],products[4][2]),Product(products[5][0],products[5][1],products[5][2])
    
def printStock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(len(products)):
        if eval(products[i][3]).quantity > 0:
            print(str(i)+")",eval(products[i][3]).name, "${0}".format(eval(products[i][3]).price))
    print()
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        try: prodId,count = products[int(vals[0])][3],int(vals[1])
        except: continue
        if eval(prodId).inStock(count):
            if cash >= eval(prodId).totalCost(count):
                eval(prodId).rmQuantity(count)
                cash -= eval(prodId).totalCost(count)
                print("You purchased", count, eval(prodId).name)
                print("You have", "${0:.2f}".format(cash), "remaining.")
            else: print("Sorry, you cannot afford that product.")
        else: print("Sorry, we are sold out of", eval(prodId).name)
main()
