# Software Developer Salary Prediction

This project is a web application built using **Streamlit** that allows users to predict the annual salary of a software developer based on factors such as location, education level, and years of professional experience. The app utilizes machine learning models (Decision Trees, Random Forest, and Linear Regression) to make predictions based on a dataset of salaries in the tech industry.

## Technologies Used
- **Streamlit**: Framework for building the interactive web application.
- **Python**: Backend development and data manipulation.
- **Scikit-learn**: For training machine learning models (Decision Trees, Random Forest, and Linear Regression).
- **Pandas**: For data cleaning and manipulation.
- **Matplotlib**: For data visualization.
- **Pickle**: For saving and loading trained models.

## Project Flow
1. **Data Cleaning & Exploration**:
   - Cleaned the dataset by handling missing values, encoding categorical variables, and filtering relevant data.
2. **Model Building**:
   - Trained machine learning models (DecisionTreeRegressor, RandomForestRegressor, LinearRegression) to predict salaries based on input features.
3. **Model Evaluation**:
   - Evaluated models using metrics such as Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) to select the best performing model.
4. **Streamlit Interface**:
   - Built an easy-to-use interface where users can input their country, education level, and years of experience to get a salary prediction.

## Features
- **Data Exploration**: Visualizes the average salary based on factors like country, years of experience, and education level.
- **Salary Prediction**: Users can input their details (country, education, experience) to receive a salary prediction.
- **Model Saving & Loading**: The trained model is saved using **pickle**, allowing for easy reuse and deployment.


## Dataset Source

The dataset used in this project is sourced from the [Stack Overflow Developer Survey 2024](https://survey.stackoverflow.co/2024). This survey collects insights from thousands of software developers across the globe, providing valuable data on salaries, education, experience, and more in the tech industry. The data has been preprocessed to clean and filter the relevant fields for use in salary prediction.

