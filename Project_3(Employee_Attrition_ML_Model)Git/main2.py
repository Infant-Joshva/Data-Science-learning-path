import streamlit as st
import pandas as pd
import joblib

# Load your trained pipeline
model = joblib.load("Data-Science-learning-path\Project_3(Employee_Attrition_ML_Model)Git\pickle_files\logreg_pipeline_smote.pkl")

st.markdown("<h2 style='color: #FF5733;'>Employee Attrition Prediction</h2>", unsafe_allow_html=True)

# --- Features groups ---
median_features = {
    'Age': 30,
    'DistanceFromHome': 5,
    'MonthlyIncome': 30000,
    'NumCompaniesWorked': 1,
    'PercentSalaryHike': 10,
    'TotalWorkingYears': 5,
    'TrainingTimesLastYear': 2,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 2,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 3
}

mode_features = {
    'Education': 3,
    'EnvironmentSatisfaction': 3,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'JobSatisfaction': 3,
    'RelationshipSatisfaction': 3,
    'WorkLifeBalance': 3,
    'PerformanceRating': 3,
    'BusinessTravel': 'Travel_Rarely',
    'Department': 'Sales',
    'Gender': 'Male',
    'MaritalStatus': 'Single',
    'OverTime': 'No',
    'EducationField': 'Life Sciences',
    'JobRole': 'Sales Executive'
}

# --- User Inputs (only selected subset) ---
user_input = {
    'Age': st.number_input("Age", 18, 60, 30),
    'Education': st.selectbox("Education", [1,2,3,4,5]),
    'EnvironmentSatisfaction': st.selectbox("Environment Satisfaction", [1,2,3,4]),
    'JobLevel': st.selectbox("Job Level", [1,2,3,4,5]),
    'JobSatisfaction': st.selectbox("Job Satisfaction", [1,2,3,4]),
    'MonthlyIncome': st.number_input("Monthly Income", 1000, 200000, 30000),
    'PercentSalaryHike': st.number_input("Percent Salary Hike", 0, 50, 10),
    'PerformanceRating': st.selectbox("Performance Rating", [1,2,3,4]),
    'TotalWorkingYears': st.number_input("Total Working Years", 0, 40, 5),
    'WorkLifeBalance': st.selectbox("Work Life Balance", [1,2,3,4]),
    'YearsAtCompany': st.number_input("Years At Company", 0, 40, 5),
    'YearsSinceLastPromotion': st.number_input("Years Since Last Promotion", 0, 20, 1),
    'YearsWithCurrManager': st.number_input("Years With Current Manager", 0, 20, 3),
    'Department': st.selectbox("Department", ['Sales', 'Research & Development', 'Human Resources']),
    'Gender': st.selectbox("Gender", ['Male', 'Female']),
    'JobRole': st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                         'Manufacturing Director', 'Healthcare Representative',
                                         'Manager', 'Sales Representative', 'Human Resources', 'Other']),
    'MaritalStatus': st.selectbox("Marital Status", ['Single', 'Married', 'Divorced']),
    'OverTime': st.selectbox("OverTime", ['Yes', 'No'])
}

# --- Fill missing features with defaults ---
full_input = {**median_features, **mode_features, **user_input}

# Convert to DataFrame
input_df = pd.DataFrame([full_input])

# Ensure column order matches model training
expected_features = list(median_features.keys()) + list(mode_features.keys())
input_df = input_df[expected_features]

# Prediction
pred_class = model.predict(input_df)[0]
pred_proba = model.predict_proba(input_df)[0]

# Map probability with labels
class_labels = model.classes_
probability_dict = {class_labels[i]: round(pred_proba[i], 3) for i in range(len(class_labels))}

# --- Display Results ---
st.subheader("Prediction Result")
st.write(f"**Predicted Attrition:** {pred_class}")

if pred_class == "Yes":
    st.error("⚠️ Employee is likely to leave.")
else:
    st.success("✅ Employee is likely to stay.")


st.subheader("Prediction Probabilities")

no_prob = pred_proba[class_labels.tolist().index("No")]
yes_prob = pred_proba[class_labels.tolist().index("Yes")]

no_prob = pred_proba[class_labels.tolist().index("No")]
yes_prob = pred_proba[class_labels.tolist().index("Yes")]

progress_html = f"""
<div style="display: flex; width: 100%; height: 20px; border-radius: 10px; overflow: hidden; font-weight: bold; color: white;">
    <!-- No Probability -->
    <div style="width: {no_prob*100}%; background-color: #2ECC40; display: flex; align-items: center; justify-content: center; font-size: 12px;">
        {no_prob*100:.0f}%
    </div>
    <!-- Yes Probability -->
    <div style="width: {yes_prob*100}%; background-color: #FF4136; display: flex; align-items: center; justify-content: center; font-size: 12px;">
        {yes_prob*100:.0f}%
    </div>
</div>
"""

st.markdown(progress_html, unsafe_allow_html=True)




# Footer
st.markdown("""
    <hr>
    <div style="text-align: center;">
        <p style="font-size: 18px;">👨🏻‍💻<span style="color:#FF5733;">Employee Attrition Prediction</span> | Built by <strong>Infant Joshva</strong></p>
        <a href="https://github.com/Infant-Joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🐙 GitHub</a>
        <a href="https://www.linkedin.com/in/infant-joshva" target="_blank" style="text-decoration: none; margin: 0 10px;">🔗 LinkedIn</a>
        <a href="mailto:infantjoshva46@gmail.com" style="text-decoration: none; margin: 0 10px;">📩 Contact</a>
    </div>
""", unsafe_allow_html=True)
