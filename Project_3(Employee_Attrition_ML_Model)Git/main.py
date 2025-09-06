import streamlit as st
import pandas as pd
import joblib

# Load your trained pipeline
model = joblib.load("Data-Science-learning-path\Project_3(Employee_Attrition_ML_Model)Git\pickle_files\logreg_pipeline_smote.pkl")

st.title("Employee Attrition Prediction")

# Collect input from user
user_input = {
    'Age': st.number_input("Age", 18, 60, 30),
    # 'DistanceFromHome': st.number_input("Distance From Home", 0, 30, 5),
    'Education': st.selectbox("Education", [1,2,3,4,5]),
    'EnvironmentSatisfaction': st.selectbox("Environment Satisfaction", [1,2,3,4]),
    # 'JobInvolvement': st.selectbox("Job Involvement", [1,2,3,4]),
    'JobLevel': st.selectbox("Job Level", [1,2,3,4,5]),
    'JobSatisfaction': st.selectbox("Job Satisfaction", [1,2,3,4]),
    'MonthlyIncome': st.number_input("Monthly Income", 1000, 200000, 30000),
    # 'NumCompaniesWorked': st.number_input("Num Companies Worked", 0, 10, 1),
    'PercentSalaryHike': st.number_input("Percent Salary Hike", 0, 50, 10),
    'PerformanceRating': st.selectbox("Performance Rating", [1,2,3,4]),
    # 'RelationshipSatisfaction': st.selectbox("Relationship Satisfaction", [1,2,3,4]),
    'TotalWorkingYears': st.number_input("Total Working Years", 0, 40, 5),
    # 'TrainingTimesLastYear': st.number_input("Training Times Last Year", 0, 10, 2),
    'WorkLifeBalance': st.selectbox("Work Life Balance", [1,2,3,4]),
    'YearsAtCompany': st.number_input("Years At Company", 0, 40, 5),
    # 'YearsInCurrentRole': st.number_input("Years In Current Role", 0, 20, 2),
    'YearsSinceLastPromotion': st.number_input("Years Since Last Promotion", 0, 20, 1),
    'YearsWithCurrManager': st.number_input("Years With Current Manager", 0, 20, 3),
    # 'BusinessTravel': st.selectbox("Business Travel", ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently']),
    'Department': st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources']),
    # 'EducationField': st.selectbox("Education Field", ['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Other']),
    'Gender': st.selectbox("Gender", ['Male', 'Female']),
    'JobRole': st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                         'Manufacturing Director', 'Healthcare Representative',
                                         'Manager', 'Sales Representative', 'Human Resources', 'Other']),
    'MaritalStatus': st.selectbox("Marital Status", ['Single', 'Married', 'Divorced']),
    'OverTime': st.selectbox("OverTime", ['Yes', 'No'])
}

# Convert to DataFrame
input_df = pd.DataFrame([user_input])

# Prediction
pred_class = model.predict(input_df)[0]   # "Yes" or "No"
pred_proba = model.predict_proba(input_df)[0]

# Map probability with labels
class_labels = model.classes_   # e.g. array(['No','Yes'])
probability_dict = {class_labels[i]: round(pred_proba[i], 3) for i in range(len(class_labels))}

st.subheader("Prediction Result")
st.write(f"**Predicted Attrition:** {pred_class}")

st.subheader("Prediction Probabilities")
st.write(probability_dict)
