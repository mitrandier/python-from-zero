import math

height_in = int(input("height of the wall is: "))
width_in = int(input("width of the wall is: "))

def paint_calc(width , height):
    area = (width * height)
    number_of_cans = math.ceil(area / 5)
    print(f"The number ogf can that you need is : {number_of_cans} ")
    
paint_calc(width = width_in , height = height_in)
    

