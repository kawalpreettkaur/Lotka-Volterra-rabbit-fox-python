import math

#Lotka Volterra Equation 
#r(y) =r[y-1]+(r[y-1]*alpha)-(r[y-1]*f[y-1]*beta)
#f(y) =f[y-1]+(f[y-1]*r[y-1]*gamma)-(f[y-1]*delta)


yearly_rabbits=[]
yearly_foxes=[]

birth_rate_of_rabbits=0.2    #alpha
death_rate_of_rabbits=0.005  #beta
birth_rate_of_foxes=0.001    #gamma
death_rate_of_foxes=0.2      #delta

year_iterator=0

def population(rabbits, foxes, years):

    global yearly_rabbits
    global yearly_foxes

    global birth_rate_of_rabbits   #alpha
    global death_rate_of_rabbits   #beta
    global birth_rate_of_foxes     #gamma
    global death_rate_of_foxes     #delta

    global year_iterator
    

    if years <0:
        return 
        
    else:
        rabbits_population, foxes_population = rabbits, foxes

        yearly_rabbits.append(rabbits)
        yearly_foxes.append(foxes)

        print(f"Year {year_iterator}: {rabbits} rabbits, {foxes} foxes")

        #r(y) =r[y-1]+(r[y-1]*alpha)-(r[y-1]*f[y-1]*beta)
        rabbits = math.floor(rabbits_population + (rabbits_population *birth_rate_of_rabbits) -(rabbits_population*foxes_population*death_rate_of_rabbits))
        #f(y) =f[y-1]+(f[y-1]*r[y-1]*gamma)-(f[y-1]*delta)
        foxes = math.floor(foxes_population +(foxes_population *rabbits_population* birth_rate_of_foxes)- (foxes_population*death_rate_of_foxes))
        
        

        if rabbits < 0:
            rabbits=0
            
        
        if foxes < 0:
            foxes=0
        
        
    
    
    year_iterator+=1

    return population(rabbits,foxes,years-1)

        
            

        


if __name__ == '__main__':

    print("==> Rabbits and Foxes Population Simulator <==\n")
    years = int(input('Enter Number of Years to Simulate: '))

    print("\n--- Initial Population ---")
    rabbits = int(input("Enter Initial Rabbit Population: "))
    foxes = int(input("Enter Initial Fox Population: "))
    
    

    print("\n--- Model Parameters ---")
    print(f"Rabbits birth rate: {birth_rate_of_rabbits}")
    print(f"Rabbits death rate: {death_rate_of_rabbits}")
    print(f"Foxes birth rate: {birth_rate_of_foxes}")
    print(f"Foxes death rate: {death_rate_of_foxes}\n")

    print("\n--- Per Year Populations ---")
    population(rabbits, foxes, years)
        

    print(f"\nRabbit populations: {yearly_rabbits}")   
    print(f"Fox populations: {yearly_foxes}\n")   
