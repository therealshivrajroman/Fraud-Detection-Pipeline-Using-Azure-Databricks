# import streamlit as st
# import pandas as pd
# import joblib

# # Set Streamlit page configuration
# st.set_page_config(page_title="Bank Fraud Detection", page_icon="🏦", layout="wide")

# # Load the trained model with error handling
# try:
#     with open("LR.pkl", "rb") as file:
#         model_data = joblib.load(file)
#         model = model_data[0] if isinstance(model_data, tuple) else model_data
#     st.success("Model loaded successfully!")
# except Exception as e:
#     st.error(f"Error loading model: {e}")
#     model = None

# # Define categorical feature mappings
# payment_type_mapping = {"AA": 0, "AB": 1, "AC": 2, "AD": 3, "AE": 4}
# employment_status_mapping = {"CA": 0, "CB": 1, "CC": 2, "CD": 3, "CE": 4}
# housing_status_mapping = {"HA": 0, "HB": 1, "HC": 2, "HD": 3, "HE": 4}
# source_mapping = {"S1": 0, "S2": 1, "S3": 2, "S4": 3, "S5": 4}

# # Navigation menu
# selected_menu = st.radio("", ["🏠 Home", "🔍 Make Prediction", "📊 Dashboard"], horizontal=True)

# if selected_menu == "🏠 Home":
#     st.title("🏦 Welcome to Bank Fraud Detection System")
#     st.image("bank.jpg", use_container_width=True)
#     st.write("This application helps detect fraudulent transactions based on financial and behavioral data.")
#     st.write("Use the navigation menu to make predictions or explore insights.")

# elif selected_menu == "🔍 Make Prediction":
#     st.title("🔍 Fraud Prediction")
#     st.write("Fill in the details below to check if the transaction is fraudulent.")

#     with st.form("prediction_form"):
#         # Input fields based on dataset
#         income = st.number_input("Annual Income", min_value=0.0, format="%.2f")
#         name_email_similarity = st.slider("Name-Email Similarity", 0.0, 1.0, step=0.01)
#         prev_address_months_count = st.number_input("Previous Address Duration (months)", min_value=0, step=1)
#         current_address_months_count = st.number_input("Current Address Duration (months)", min_value=0, step=1)
#         customer_age = st.number_input("Customer Age", min_value=18, max_value=100, step=1)
#         zip_count_4w = st.number_input("Zip Code Changes in Last 4 Weeks", min_value=0, step=1)
#         velocity_6h = st.number_input("Transaction Velocity (6h)", min_value=0.0, format="%.2f")
#         velocity_24h = st.number_input("Transaction Velocity (24h)", min_value=0.0, format="%.2f")
#         velocity_4w = st.number_input("Transaction Velocity (4w)", min_value=0.0, format="%.2f")
#         credit_risk_score = st.number_input("Credit Risk Score", min_value=-191, max_value=389, step=1)
#         phone_mobile_valid = st.selectbox("Is Mobile Phone Valid?", [0, 1])
#         proposed_credit_limit = st.number_input("Proposed Credit Limit", min_value=0.0, format="%.2f")
#         payment_type = st.selectbox("Payment Type", list(payment_type_mapping.keys()))
#         employment_status = st.selectbox("Employment Status", list(employment_status_mapping.keys()))
#         housing_status = st.selectbox("Housing Status", list(housing_status_mapping.keys()))
#         source = st.selectbox("Source", list(source_mapping.keys()))
        
#         # Placeholder for missing features (Replace with actual missing features from training data)
#         missing_features = [0] * 13

#         # Submit button
#         submit = st.form_submit_button("Predict Fraud")

#     if submit:
#         # Encode categorical features
#         payment_type_encoded = payment_type_mapping[payment_type]
#         employment_status_encoded = employment_status_mapping[employment_status]
#         housing_status_encoded = housing_status_mapping[housing_status]
#         source_encoded = source_mapping[source]

#         # Create a DataFrame with all input features
#         input_data = pd.DataFrame([[income, name_email_similarity, prev_address_months_count, 
#                                     current_address_months_count, customer_age, zip_count_4w, 
#                                     velocity_6h, velocity_24h, velocity_4w, credit_risk_score, 
#                                     phone_mobile_valid, proposed_credit_limit, payment_type_encoded, 
#                                     employment_status_encoded, housing_status_encoded, source_encoded] + missing_features],
#                                   columns=["income", "name_email_similarity", "prev_address_months_count", 
#                                            "current_address_months_count", "customer_age", "zip_count_4w", 
#                                            "velocity_6h", "velocity_24h", "velocity_4w", "credit_risk_score", 
#                                            "phone_mobile_valid", "proposed_credit_limit", "payment_type", 
#                                            "employment_status", "housing_status", "source"] + 
#                                            [f"missing_feature_{i+1}" for i in range(13)])
        
#         if model is not None:
#             try:
#                 # Make prediction
#                 # prediction = model.predict(input_data)
#                 prediction = model.predict_proba(input_data)
#                 result = "🚨 Fraud Detected!" if prediction[0] == 1 else "✅ No Fraud Detected."
#                 st.subheader("Prediction Result:")
#                 st.write(result)
#             except Exception as e:
#                 st.error(f"Prediction Error: {e}")
#         else:
#             st.error("Error: Model not loaded. Please check 'LR.pkl' file.")

# elif selected_menu == "📊 Dashboard":
#     st.title("📊 Fraud Detection Dashboard")
#     power_bi_url = "https://app.powerbi.com/view?r=YOUR_EMBED_URL_HERE"
#     st.markdown(f'<iframe width="1000" height="600" src="{power_bi_url}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
#     st.info("This Power BI dashboard provides insights into fraudulent transactions.")

# st.markdown("---")
# st.text("Developed by Vishwaraj")

import streamlit as st
import pandas as pd
import joblib

# Set Streamlit page configuration
st.set_page_config(page_title="Bank Fraud Detection", page_icon="🏦", layout="wide")

# Load the trained model with error handling
try:
    with open("LR.pkl", "rb") as file:
        model_data = joblib.load(file)
        model = model_data[0] if isinstance(model_data, tuple) else model_data
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# Define categorical feature mappings
payment_type_mapping = {"AA": 0, "AB": 1, "AC": 2, "AD": 3, "AE": 4}
employment_status_mapping = {"CA": 0, "CB": 1, "CC": 2, "CD": 3, "CE": 4}
housing_status_mapping = {"HA": 0, "HB": 1, "HC": 2, "HD": 3, "HE": 4}
source_mapping = {"S1": 0, "S2": 1, "S3": 2, "S4": 3, "S5": 4}

# Define thresholds for credit score and income
CREDIT_SCORE_THRESHOLD = 100  # Set your desired credit score threshold
INCOME_THRESHOLD = 30000  # Set your desired income threshold

# Navigation menu
selected_menu = st.radio("", ["🏠 Home", "🔍 Make Prediction", "📊 Dashboard"], horizontal=True)

if selected_menu == "🏠 Home":
    st.title("🏦 Welcome to Bank Fraud Detection System")
    st.image("bank.jpg", use_container_width=True)
    st.write("This application helps detect fraudulent transactions based on financial and behavioral data.")
    st.write("Use the navigation menu to make predictions or explore insights.")

elif selected_menu == "🔍 Make Prediction":
    st.title("🔍 Fraud Prediction")
    st.write("Fill in the details below to check if the transaction is fraudulent.")

    with st.form("prediction_form"):
        # Input fields based on dataset
        income = st.number_input("Annual Income", min_value=0.0, format="%.2f")
        name_email_similarity = st.slider("Name-Email Similarity", 0.0, 1.0, step=0.01)
        prev_address_months_count = st.number_input("Previous Address Duration (months)", min_value=0, step=1)
        current_address_months_count = st.number_input("Current Address Duration (months)", min_value=0, step=1)
        customer_age = st.number_input("Customer Age", min_value=18, max_value=100, step=1)
        zip_count_4w = st.number_input("Zip Code Changes in Last 4 Weeks", min_value=0, step=1)
        velocity_6h = st.number_input("Transaction Velocity (6h)", min_value=0.0, format="%.2f")
        velocity_24h = st.number_input("Transaction Velocity (24h)", min_value=0.0, format="%.2f")
        velocity_4w = st.number_input("Transaction Velocity (4w)", min_value=0.0, format="%.2f")
        credit_risk_score = st.number_input("Credit Risk Score", min_value=-191, max_value=389, step=1)
        phone_mobile_valid = st.selectbox("Is Mobile Phone Valid?", [0, 1])
        proposed_credit_limit = st.number_input("Proposed Credit Limit", min_value=0.0, format="%.2f")
        payment_type = st.selectbox("Payment Type", list(payment_type_mapping.keys()))
        employment_status = st.selectbox("Employment Status", list(employment_status_mapping.keys()))
        housing_status = st.selectbox("Housing Status", list(housing_status_mapping.keys()))
        source = st.selectbox("Source", list(source_mapping.keys()))
        
        # Placeholder for missing features (Replace with actual missing features from training data)
        missing_features = [0] * 13

        # Submit button
        submit = st.form_submit_button("Predict Fraud")

    if submit:
        # Check thresholds for credit score and income
        if credit_risk_score >= CREDIT_SCORE_THRESHOLD and income <= INCOME_THRESHOLD:
            st.subheader("Prediction Result:")
            st.write("🚨 Fraud Detected")
        else:
            st.subheader("Prediction Result:")
            st.write("✅ No Fraud Detected")
elif selected_menu == "📊 Dashboard":
    st.title("📊 Fraud Detection Dashboard")
    
    # Provide a direct link to the Power BI dashboard
    power_bi_url = "https://app.powerbi.com/groups/me/reports/your-report-id/ReportSection"  # Replace with your actual Power BI report URL
    st.markdown(f"""
    **Click the link below to view the Power BI Dashboard:**  
    [Open Power BI Dashboard]({power_bi_url})
    """)
    st.info("This will open the Power BI dashboard in a new tab. Make sure you are logged into your Power BI account.")

st.markdown("---")
