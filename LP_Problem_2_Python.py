# Revise the initial problem to include the constraint that there must be at least one serving of every food item each week.

# Import libraries
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Define LP problem (minimization problem)
diet_prob = LpProblem("Diet_Problem", LpMinimize)

# Define variables
oatmilk = LpVariable("oatmilk", 1, None) # oatmilk >= 1
bread = LpVariable("bread", 1, None) # bread >= 1
yogurt = LpVariable("yogurt", 1, None) # yogurt >= 1
tuna = LpVariable("tuna", 1, None) # tuna >= 1
cheese = LpVariable("cheese", 1, None) # cheese >= 1

# Determine cost per serving for each food item
oatmilk_cps = round((6.29 / 8), 2)
bread_cps = round((5.99 / 15), 2)
yogurt_cps = round((7.29 / 5), 2)
tuna_cps = 1.69
cheese_cps = round((5.29 / 16), 2)

# Define objective function
diet_prob += (oatmilk_cps * oatmilk) + (bread_cps * bread) + (yogurt_cps * yogurt) + (tuna_cps * tuna) + (cheese_cps * cheese)

# Define constraints
diet_prob += (100 * oatmilk) + (230 * bread) + (65 * yogurt) + (270 * tuna) + (230 * cheese)    <= 35000    # Sodium
diet_prob += (120 * oatmilk) + (110 * bread) + (90 * yogurt) + (110 * tuna) + (60 * cheese)     >= 14000    # Energy
diet_prob += (3 * oatmilk) + (3 * bread) + (18 * yogurt) + (24 * tuna) + (4 * cheese)           >= 350      # Protein
diet_prob += (3.6 * oatmilk) + (3 * tuna)                                                       >= 140      # Vitamin D
diet_prob += (350 * oatmilk) + (6 * bread) + (200 * yogurt) + (330 * cheese)                    >= 9100     # Calcium
diet_prob += (0.3 * oatmilk) + (1.4 * bread) + (1.08 * tuna)                                    >= 126      # Iron
diet_prob += (390 * oatmilk) + (30 * bread) + (260 * yogurt) + (188 * tuna) + (60 * cheese)     >= 32900    # Potassium 

# Solve the problem
status = diet_prob.solve()

# Open a file to write the output
with open('LP_Solution_2.txt', 'w') as file:
    file.write("Problem\n")
    file.write(f"status = {LpStatus[status]}\n")

    # Print and write the results
    file.write("Number of weekly servings of each food item:\n")
    for variable in diet_prob.variables():
        file.write(f"{variable.name} = {round(variable.varValue, 2)}\n")
    file.write(f"Minimum cost = ${round(value(diet_prob.objective), 2)}\n")
