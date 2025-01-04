# FridgeFriend

## Running the Application 
- manually put "recipe_ingredients_list.pkl" inside technova2024
- manually update images folder path in not_pages/results.py

## Inspiration
- We were discussing our lives recently and realized we were often too busy to cook meals for ourselves.
- Realized the importance of being able to cook meals out of ingredients we already have.

## What it does
- Users can upload an image of their fridge, and the detected items will be generated.
- The user can then edit the ingredients if any mistakes were made or add other ingredients they did not take pictures of.
- A list of the most closely related recipes will be recommended to the user, including images, ingredients, and instructions.

## How we built it
- **Python**
- **Streamlit** with CSS/HTML for the front-end and for image recognition.
- Recipe dataset from Kaggle, vectorizer trained using Scikit-learn.
- **PropelAuth** for user authentication system.
- **MongoDB Atlas** for storing user data.

## Challenges we ran into
- Found it difficult to use version control with our larger files, but found ways to make it work.
- Learning how to use Streamlit under tight time constraints.

## Accomplishments that we're proud of
- Creating a functional application!
- Login system.
- Using Streamlit to create an organized front-end.
- Recommendations algorithm.

## What we learned
- How to use Streamlit.
- A lot of things about Git.

## What's next for FridgeFriend
- Improvements on the image recognition model – it currently is not very precise at detecting images with many food items, which is important to the functionality of being able to take a picture of your fridge.
- We'd like to be able to make our recommendation system faster.
- Allow accounts to share pictures of their meals with each other.
- Gamify the process to provide incentives for users to make meals.
