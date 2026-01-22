class productData:
    id = 1
    title = None
    description= ""
    category = ""
    price = 100
    discountPrice = 10
    rating= ""
    stock = 1

    def __init__(self, id, title, description,category, price,discountPrice,rating, stock):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.price = price
        self.discountPrice = discountPrice
        self.rating = rating
        self.stock = stock

    # def __init__(self):
    #     print("The constructor print statement")
    #     print(self.description)

    

# productData1 = productData()
# productData1.title = "Laptop"
# print(productData1.title)    
productData2 = productData(2, "efasd", "adwadasd", "adsadsa", 1000, 10, "3.0", 100)
print(productData2.title)

