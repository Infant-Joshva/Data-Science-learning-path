import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, inspect

db_url="postgresql://infant:5kV8T4PGM0C3pHexclSBZU80ijwqBMxn@dpg-d0mmus3e5dus738lfkgg-a.singapore-postgres.render.com/traffic" #Database Connection, Host Name, Password, Database Name
engine=create_engine(db_url)

# Connect to your database
#engine = create_engine('sqlite:///your_database.db')  # Replace with your actual DB path

# Define your queries
queries = {
    "Top 10 vehicles involved in drug-related stops":
        """
        SELECT vehicle_number, COUNT(drugs_related_stop) AS drug_related_stop_count
        FROM traffic_stop
        WHERE drugs_related_stop = TRUE
        GROUP BY vehicle_number
        ORDER BY drug_related_stop_count DESC
        LIMIT 10;
        """,

    "Most frequently searched violations":
        """
        SELECT violation_raw, COUNT(violation_raw) AS search_count
        FROM traffic_stop
        WHERE search_conducted = 'TRUE'
        GROUP BY violation_raw
        ORDER BY search_count DESC
        LIMIT 10;
        """,

    "Driver age groups with highest arrest rates":
        """
        SELECT driver_age_raw, COUNT(is_arrested) AS arrest_count
        FROM traffic_stop
        WHERE is_arrested = TRUE
        GROUP BY driver_age_raw
        ORDER BY arrest_count DESC
        LIMIT 10;
        """,

    "Gender distribution of drivers stopped in each country":
        """
        SELECT country_name, driver_gender, COUNT(driver_gender) AS gender_count
        FROM traffic_stop
        GROUP BY country_name, driver_gender
        ORDER BY country_name, gender_count DESC;
        """
}

# Streamlit UI
st.title("Advanced Insights")

# Dropdown to select query
#selected_query = st.selectbox("Select a query to run:", list(queries.keys()))

# Run and display the selected query
#if selected_query:
    #query = queries[selected_query]
    #result_df = pd.read_sql(query, engine)
    #st.dataframe(result_df)

# Add a placeholder option
#options = ["-- Select a query --"] + list(queries.keys())
options = ["-- Select a query --"] + list(queries)

# Create dropdown with default index 0 (placeholder)
selected_query = st.selectbox("Select a query to run:", options, index=0)

# Only run query if real selection is made
if selected_query != "-- Select a query --":
    query = queries[selected_query]
    result_df = pd.read_sql(query, engine)
    st.dataframe(result_df)

#test commit