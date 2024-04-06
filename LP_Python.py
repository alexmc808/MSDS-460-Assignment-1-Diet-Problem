# Import libraries
from pulp import LpVariable, LpProblem, LpMaximize, LpStatus, value, LpMinimize

# Define LP problem (minimization problem)
diet_prob = LpProblem("Diet_Problem", LpMinimize)

# Define variables
yogurt = LpVariable("yogurt", 0, None) # yogurt >= 0
bread = LpVariable("bread", 0, None) # bread >= 0
tuna = LpVariable("tuna", 0, None) # tuna >= 0
oatmilk = LpVariable("oatmilk", 0, None) # oatmilk >= 0
cheese = LpVariable("cheese", 0, None) # cheese >= 0

# Determine cost per serving for each food item
yogurt_cps = round((7.29 / 5), 2)
bread_cps = round((5.99 / 15), 2)
tuna_cps = 1.19
oatmilk_cps = round((5.99 / 8), 2)
cheese_cps = round((6.99 / 24), 2)

# Define objective function
diet_prob += (yogurt_cps * yogurt) + (bread_cps * bread) + (tuna_cps * tuna) + (oatmilk_cps * oatmilk) + (cheese_cps * cheese)

# Define constraints
diet_prob += (65 * yogurt) + (230 * bread) + (270 * tuna) + (100 * oatmilk) + (230 * cheese)    <= 35000    # Sodium
diet_prob += (90 * yogurt) + (120 * bread) + (80 * tuna) + (120 * oatmilk) + (50 * cheese)      >= 14000    # Energy
diet_prob += (18 * yogurt) + (3 * bread) + (18 * tuna) + (3 * oatmilk) + (3 * cheese)           >= 350      # Protein
diet_prob += (3.6 * oatmilk) + (0.9 * cheese)                                                   >= 140      # Vitamin D
diet_prob += (200 * yogurt) + (40 * bread) + (350 * oatmilk) + (290 * cheese)                   >= 9100     # Calcium
diet_prob += (1.3 * bread) + (1.1 * tuna) + (0.3 * oatmilk)                                     >= 126      # Iron
diet_prob += (260 * yogurt) + (30 * bread) + (188 * tuna) + (390 * oatmilk)                     >= 32900    # Potassium 

# Solve the problem
status = diet_prob.solve()
print(f"Problem")
print(f"status = {LpStatus[status]}")

# Print the results
for variable in diet_prob.variables():
    print(f"{variable.name} = {variable.varValue}")
print(f"Objective = ${round(value(diet_prob.objective), 2)}")
