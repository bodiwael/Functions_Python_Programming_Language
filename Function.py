
def one_to_ten () :
    
    for i in range(1 , 11) :
        
        print(i)


one_to_ten()

#-----------------------------------------------------------------------------

print("\n--------------------------------\n")

def find_average ( * numbers ) :
    
    sum = 0
    
    for i in numbers :
        
        sum += i
        
    print("average is : " , sum/(len(numbers)))
    

find_average(3 , 5 , 5 , 8)

#-----------------------------------------------------------------------------

print("\n--------------------------------\n")

def print_values ( ** values ) :
    
    print(values)

print_values(one = 1 , two = 2 , three = 3)

#-----------------------------------------------------------------------------

print("\n--------------------------------\n")

def powers(m , n = 4) :
    
    print( m ** n )
    
powers( 3 , 5 )

powers(2)

#-----------------------------------------------------------------------------

print("\n--------------------------------\n")


def power ( x , y ) :
    
    c = x ** y
    
    return c

print(power(5,3))
