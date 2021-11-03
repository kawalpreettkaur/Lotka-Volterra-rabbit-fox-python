# Rabbits and Foxes Population Simulator using Lotka-Volterra Equation in Python

rabbit-fox population calculator that determines the population size of foxes and rabbits who live within a certain area of land, as that number changes from year to year using Lotka Volterra Equation.

[ Chegg Question ]

It models the rabbits & foxes with 4 constants, and 2 data structures of year by year values. They are defined as follows:

1. r[y] # of rabbits in year y
2. f[y] # of foxes in year y
3. alpha - birth rate of rabbits
4. beta - death rate of rabbits, dependent on # of foxes
5. gamma - birth rate of foxes dependent on # of rabbits
6. delta - death rate of foxes caused naturally

The formulas we are using are:

Lotka Volterra Equation:

r(y) =r[y-1]+(r[y-1]*alpha)-(r[y-1]*f[y-1]*beta)
f(y) =f[y-1]+(f[y-1]*r[y-1]*gamma)-(f[y-1*delta)

However, negative values are not allowed! If either formula results in a negative value, you should use 0 instead.

You will start out by asking the user how many years of simulation he or she wants, and what the initial number of rabbits & foxes are. Each of these populations of animals needs to be held in it's own data structure. The first element of each data structure holds the initial populations & subsequent elements are calculated using the above formulas. (Remember that single letter names are usually horrible. Don't call your rabbit and fox data structures  r & f- those names are just for the equations above.)

Values of alpha,beta, gamma & delta:

birth_rate_of_rabbits=0.2    #alpha
death_rate_of_rabbits=0.005  #beta
birth_rate_of_foxes=0.001    #gamma
death_rate_of_foxes=0.2      #delta

You should print each year's population as you calculate them, and then give a final report at the end with all the calculations. Here, is how your program should appear. Note these values are not accurate:

Year 0: 50 rabbits, 10 foxes
Year 1: 200 rabbits, 4 foxes
Year 2: 133 rabbits, 6 foxes

Rabbit populations: [50,200,133]
Fox populations: [10,4,6]

Some hints:

1. The values of alpha,beta & gamma should all be varibales, with proper names.
2. Since the fox & rabbit populations are whole numbers, you will have to round them for the program to work. The easisest way to do this is to use the round() method.
3. Be sure that your program doesn't allow for negative populations. If you start with 1 rabbit & 1000 foxes, the next year there should be 0 rabbits instead of -3 rabbits.( Or is that anti rabbits? What is an anti rabbit? )
4. You can use str() method to make a nice readable output of a data structure. This takes an array as its argument, and returns an human readable string.
5. Note that the length of the data structures should be 1 or more than the requested years of simulation!

While your code should work for any number of years simulated and initial populations of rabbits & foxes , please use 15 years, 44 rabbits and 2 foxes in your output file.

Sample Output:

==> Rabbits and Foxes Population Simulator <==

Enter Number of Years to Simulate: 3

--- Initial Population ---       
Enter Initial Rabbit Population: 1
Enter Initial Fox Population: 1000

--- Model Parameters --- 
Rabbits birth rate: 0.2  
Rabbits death rate: 0.005
Foxes birth rate: 0.001  
Foxes death rate: 0.2    


--- Per Year Populations ---
Year 0: 1 rabbits, 1000 foxes
Year 1: 0 rabbits, 801 foxes
Year 2: 0 rabbits, 640 foxes
Year 3: 0 rabbits, 512 foxes

Rabbit populations: [1, 0, 0, 0]
Fox populations: [1000, 801, 640, 512]

