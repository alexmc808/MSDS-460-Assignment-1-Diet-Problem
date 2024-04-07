# MSDS 460 Assignment 1: Linear Programming - The Diet Problem Revisited

## Introduction
This repository contains the code, code solutions, food nutrion label images, ChatGPT conversation, and report for the MSDS 460 assignment focusing on linear programming, particularly the diet problem. The diet problem involves optimizing food selection to meet nutritional requirements while minimizing cost, making it a classic problem in operations research.

## Problem Description
The problem revolves around selecting packaged food items from Ralph’s to create a weekly diet plan. The objective is to minimize total expenditure while ensuring nutritional requirements are met. Five food items are considered: Oatly Original Oatmilk, San Louis Sourdough Bread, Fage Total Plain 0% Milkfat Nonfat Greek Yogurt Tub, Chicken of the Sea Chunk Light Tuna in Water, and Kraft Singles American Sliced Cheese. The cost per serving for each item is as follows:
- Oatmilk: $0.79
- Sourdough bread: $0.40
- Greek yogurt: $1.46
- Tuna: $1.69
- Cheese: $0.33

## Linear Programming Problem
The code and solution for the linear programming problem can be found in the repository labeled as "Problem 1". The linear programming problem is formulated as follows:

**Decision Variables:**
- \( \text{oatmilk} \): Number of servings of Oatly Original Oatmilk
- \( \text{bread} \): Number of servings of San Louis Sourdough Bread
- \( \text{yogurt} \): Number of servings of Fage Total Plain 0% Milkfat Nonfat Greek Yogurt Tub
- \( \text{tuna} \): Number of servings of Chicken of the Sea Chunk Light Tuna in Water
- \( \text{cheese} \): Number of servings of Kraft Singles American Sliced Cheese

**Objective Function:**
Minimize \( Z = 0.79 \times \text{oatmilk} + 0.40 \times \text{bread} + 1.46 \times \text{yogurt} + 1.69 \times \text{tuna} + 0.33 \times \text{cheese} \)

**Constraints:**
1. \( 100 \times \text{oatmilk} + 230 \times \text{bread} + 65 \times \text{yogurt} + 270 \times \text{tuna} + 230 \times \text{cheese} \leq 35000 \)
2. \( 120 \times \text{oatmilk} + 110 \times \text{bread} + 90 \times \text{yogurt} + 110 \times \text{tuna} + 60 \times \text{cheese} \geq 14000 \)
3. \( 3 \times \text{oatmilk} + 3 \times \text{bread} + 18 \times \text{yogurt} + 24 \times \text{tuna} + 4 \times \text{cheese} \geq 350 \)
4. \( 3.6 \times \text{oatmilk} + 0.3 \times \text{tuna} \geq 140 \)
5. \( 350 \times \text{oatmilk} + 6 \times \text{bread} + 200 \times \text{yogurt} + 330 \times \text{cheese} \geq 9100 \)
6. \( 0.3 \times \text{oatmilk} + 1.4 \times \text{bread} + 1.08 \times \text{tuna} \geq 126 \)
7. \( 390 \times \text{oatmilk} + 30 \times \text{bread} + 260 \times \text{yogurt} + 188 \times \text{tuna} + 60 \times \text{cheese} \geq 32900 \)

**Optimal Solution:**
- Minimum cost = $91.45
- Oatmilk: 78.73 servings
- Sourdough bread: 73.13 servings
- Greek Yogurt: 0 servings
- Tuna: 0 servings
- Cheese: 0 servings

## Revised Linear Programming Problem
In response to the lack of variety in the initial solution, an additional constraint is introduced to require at least one serving of each food item per week. This adjustment aims to enhance the diversity of food selection while still minimizing cost and adhering to nutritional requirements. The code and solution for this revised problem can be found in the repository labeled as "Problem 2".

## Large Language Model Diet Problem Creation and Solution
In addition to manually modeling the problem and finding the solution, the application of ChatGPT 3.5, a large language model, to model and solve the diet problem was explored. The full conversation with ChatGPT can be found in the repository labeled as "ChatGPT_Conversation.txt".
