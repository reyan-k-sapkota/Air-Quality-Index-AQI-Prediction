import streamlit as st
from datetime import datetime

about = st.Page(
    page = "pages_new/about_new.py",
    title = '👉Air Pollution Portal: Kathmandu Metro_Version New',
    default = True,
)

forecast_data = st.Page(
    page = "pages_new/Forecast_data_new.py",
    title = '⏲️7-Day Hourly Forecasting',
)

data_visualization = st.Page(
    page = "pages_new/AQI_Visualization_new.py",
    title = '📈AQI Data Visualization',
)

alert_message = st.Page(
    page = "pages_new/Alert_message_new.py",
    title = '🍁Alert Message/Recommendation Generation',
)

info_circulation = st.Page(
    page = "pages_new/info_circulation_new.py",
    title = '🗺️Kathmandu Map Visualization',
)

user_entry = st.Page(
    page = "pages_new/user_entry_new.py",
    title = '🔨Predict Yourself',
)



st.set_page_config(layout="wide")


algorithms = ["GBM", "CatBoost", "RFRegressor"]

formatted_date = datetime.now().strftime("%Y-%m-%d")  # Example format: YYYY-MM-DD
date_obj = datetime.strptime(formatted_date, "%Y-%m-%d")
year = date_obj.year
month = date_obj.month
day = date_obj.day

pg = st.navigation(
    {
        "🎯INSTRUCTION MANUAL": [about],
        "🎯DATA ANALYTICS" : [forecast_data, data_visualization, user_entry],
        "🎯ALERT MESSAGE AND REPORTING SYSTEM": [alert_message],
        "🎯MAPPING PORTAL": [info_circulation]
        
    }
    )

pg.run()





