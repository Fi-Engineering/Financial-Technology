def print_triangle(size):
    """
    prints a triangle of a specific height and width
    
    args:
    size(int): height and width of the triangle
 
    returns:
    number of asterisks printed 
    """
     
    for i in range(0, size):
     
        for j in range(0, i+1):
         
            
            print("*",end="")
      
        
        print("\r")


size = 4
num_stars = size * (size + 1) // 2
print("Here is a triangle with height 4")
print_triangle(4)
print("That triangle had {:d} total stars".format(num_stars));

print("Here is a triangle with height 7")
print_triangle(7)
size = 7
num_stars = size * (size + 1) // 2
print("That triangle had {:d} total stars".format(num_stars));

