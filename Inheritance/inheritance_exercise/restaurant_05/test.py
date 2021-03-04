from Inheritance.inheritance_exercise.restaurant_05.project.product import Product
from Inheritance.inheritance_exercise.restaurant_05.project.beverage.beverage import Beverage
from Inheritance.inheritance_exercise.restaurant_05.project.beverage.hot_beverage import HotBeverage
from Inheritance.inheritance_exercise.restaurant_05.project.beverage.cold_beverage import ColdBeverage
from Inheritance.inheritance_exercise.restaurant_05.project.beverage.coffee import Coffee
from Inheritance.inheritance_exercise.restaurant_05.project.beverage.tea import Tea
from Inheritance.inheritance_exercise.restaurant_05.project.food.food import Food
from Inheritance.inheritance_exercise.restaurant_05.project.food.starter import Starter
from Inheritance.inheritance_exercise.restaurant_05.project.food.main_dish import MainDish
from Inheritance.inheritance_exercise.restaurant_05.project.food.dessert import Dessert
from Inheritance.inheritance_exercise.restaurant_05.project.food.soup import Soup
from Inheritance.inheritance_exercise.restaurant_05.project.food.salmon import Salmon
from Inheritance.inheritance_exercise.restaurant_05.project.food.cake import Cake

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
