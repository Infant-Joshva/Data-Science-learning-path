import streamlit as st
import pandas as pd
import joblib

# Load your 3 models
model1 = joblib.load("Data-Science-learning-path\Project_4(Multiple_Disease_Prediction)\models\kidney.pkl")  
model2 = joblib.load("Data-Science-learning-path\Project_4(Multiple_Disease_Prediction)\models\liver_model.pkl") 
model3 = joblib.load("Data-Science-learning-path\Project_4(Multiple_Disease_Prediction)\models\parkinsons.pkl")  

# --- Page Config ---
st.set_page_config(page_title="Multiple Disease Prediction",page_icon="🏥")


# --- Main Heading ---
st.markdown(
    "<h2 style='text-align: center; color: #FF5733;'> Multiple Disease Prediction</h2>",
    unsafe_allow_html=True
)


# --- Space before form ---
st.markdown("<hr>", unsafe_allow_html=True)

# Sidebar for navigation
choice = st.sidebar.selectbox(
    "Choose Disease Prediction",
    ["Kidney Disease", "Liver Disease", "Parkinsons Disease"]
)

if choice == "Kidney Disease":
    st.header("Kidney Disease Prediction")
    st.title("Disease Prediction App")

        # --- Collect inputs directly ---
    inputs = {
        "age": st.number_input("Age", min_value=1, max_value=120, value=48),
        "bp": st.number_input("Blood Pressure", min_value=50, max_value=200, value=80),
        "sg": st.number_input("Specific Gravity", min_value=1.0, max_value=1.05, step=0.001, format="%.3f", value=1.020),
        "al": st.number_input("Albumin", min_value=0, max_value=5, value=1),
        "su": st.number_input("Sugar", min_value=0, max_value=5, value=0),

        "rbc": st.selectbox("RBC", ["normal", "abnormal"]),
        "pc": st.selectbox("Pus Cell", ["normal", "abnormal"]),
        "pcc": st.selectbox("Pus Cell Clumps", ["present", "notpresent"]),
        "ba": st.selectbox("Bacteria", ["present", "notpresent"]),

        "bgr": st.number_input("Blood Glucose Random", value=121),
        "bu": st.number_input("Blood Urea", value=36),
        "sc": st.number_input("Serum Creatinine", value=1.2, format="%.2f"),
        "sod": st.number_input("Sodium", value=138),
        "pot": st.number_input("Potassium", value=4.35, format="%.2f"),
        "hemo": st.number_input("Hemoglobin", value=15.4, format="%.1f"),
        "pcv": st.number_input("Packed Cell Volume", value=44),
        "wc": st.number_input("WBC Count", value=7800),
        "rc": st.number_input("RBC Count", value=5.2, format="%.1f"),

        "htn": st.selectbox("Hypertension", ["yes", "no"]),
        "dm": st.selectbox("Diabetes Mellitus", ["yes", "no"]),
        "cad": st.selectbox("Coronary Artery Disease", ["yes", "no"]),
        "appet": st.selectbox("Appetite", ["good", "poor"]),
        "pe": st.selectbox("Pedal Edema", ["yes", "no"]),
        "ane": st.selectbox("Anemia", ["yes", "no"]),
    }

    # --- Predict Button ---
    if st.button("🔍 Predict"):
        # Convert dict → DataFrame
        input_df = pd.DataFrame([inputs])

        # Prediction
        pred_class = model1.predict(input_df)[0]
        pred_proba = model1.predict_proba(input_df)[0]
        class_labels = model1.classes_

        st.markdown("""---""")
        st.subheader("🎯 Prediction Result")
        st.write(f"**Predicted Result:** {pred_class}")

        if pred_class == "ckd":
            st.error("⚠️ Positive case detected.")
        else:
            st.success("✅ Negative case detected.")

        # Show probabilities
        no_prob = pred_proba[class_labels.tolist().index("notckd")]
        yes_prob = pred_proba[class_labels.tolist().index("ckd")]

        progress_html = f"""
        <div style="display: flex; width: 100%; height: 20px; border-radius: 10px; overflow: hidden; font-weight: bold; color: white;">
            <div style="width: {no_prob*100}%; background-color: #2ECC40; display: flex; align-items: center; justify-content: center; font-size: 12px;">
                {no_prob*100:.0f}%
            </div>
            <div style="width: {yes_prob*100}%; background-color: #FF4136; display: flex; align-items: center; justify-content: center; font-size: 12px;">
                {yes_prob*100:.0f}%
            </div>
        </div>
        """
        st.markdown(progress_html, unsafe_allow_html=True)


elif choice == "Liver Disease":
    st.header("Liver Disease Prediction")
    # take inputs
    # run model2.predict(...)

elif choice == "Parkinsons Disease":
    st.header("Parkinsons Disease Prediction")
    # take inputs
    # run model3.predict(...)
