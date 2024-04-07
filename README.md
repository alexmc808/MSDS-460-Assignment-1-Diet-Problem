# MSDS 460 Assignment 1: Linear Programming - The Diet Problem Revisited

## Introduction
This repository contains Python code files, solution text files, food nutrition label images, a ChatGPT conversation text file, and a PDF report for MSDS 460 Assignment #1, which focuses on applying linear programming to the diet problem. The diet problem involves optimizing food selection to meet nutritional requirements while minimizing cost, making it a classic problem in operations research.

## Problem Description
The problem revolves around selecting packaged food items from Ralph’s to create a weekly diet plan. The objective is to minimize total expenditure while ensuring nutritional requirements are met. Five food items are considered: Oatly Original Oatmilk, San Louis Sourdough Bread, Fage Total Plain 0% Milkfat Nonfat Greek Yogurt Tub, Chicken of the Sea Chunk Light Tuna in Water, and Kraft Singles American Sliced Cheese. The cost per serving for each item is as follows:
- Oatmilk: $0.79
- Sourdough bread: $0.40
- Greek yogurt: $1.46
- Tuna: $1.69
- Cheese: $0.33

## Linear Programming Problem
The code and solution for the linear programming problem can be found in the repository labeled as "Problem_1". The linear programming problem is formulated as follows:

- **Decision Variables:**
  - oatmilk = number of servings of Oatly Original Oatmilk
  - bread = number of servings of San Louis Sourdough Bread
  - yogurt = number of servings of Fage Total Plain 0% Milkfat Nonfat Greek Yogurt Tub
  - tuna = number of servings of Chicken of the Sea Chunk Light Tuna in Water
  - cheese = number of servings of Kraft Singles American Sliced Cheese
- **Objective Function:**
  - Minimize Z = 0.79 * oatmilk + 0.40 * bread + 1.46 * yogurt + 1.69 * tuna + 0.33 * cheese
- **Constraints:**
  - 100 * oatmilk + 230 * bread + 65 * yogurt + 270 * tuna + 230 * cheese <= 35000
  - 120 * oatmilk + 110 * bread + 90 * yogurt + 110 * tuna + 60 * cheese >= 14000
  - 3 * oatmilk + 3 * bread + 18 * yogurt + 24 * tuna + 4 * cheese >= 350
  - 3.6 * oatmilk + 0.3 * tuna >= 140
  - 350 * oatmilk + 6 * bread + 200 * yogurt + 330 * cheese >= 9100
  - 0.3 * oatmilk + 1.4 * bread + 1.08 * tuna >= 126
  - 390 * oatmilk + 30 * bread + 260 * yogurt + 188 * tuna + 60 * cheese >= 32900
  - oatmilk, bread, yogurt, tuna, cheese >= 0
- **Optimal Solution:**
  - Minimum cost = $91.45
  - Oatmilk: 78.73 servings
  - Sourdough bread: 73.13 servings
  - Greek Yogurt: 0 servings
  - Tuna: 0 servings
  - Cheese: 0 servings
    
## Revised Linear Programming Problem
In response to the lack of variety in the initial solution, an additional constraint is introduced to require at least one serving of each food item per week. This adjustment aims to enhance the diversity of food selection while still minimizing cost and adhering to nutritional requirements. The code and solution for this revised problem can be found in the repository labeled as "Problem_2".

## Large Language Model Diet Problem Creation and Solution
In addition to manually modeling the problem and finding the solution, the application of ChatGPT 3.5, a large language model, to model and solve the diet problem is explored. The full conversation with ChatGPT can be found in the repository labeled as "ChatGPT_Conversation.txt".
