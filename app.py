import streamlit as st
import pandas as pd

st.set_page_config(page_title="C711 A/B Maintenance Bundle", layout="wide")

# Master Engineering Data for Dresser-Rand C711 A/B
c711_master = {
    "Stage": ["MU-1", "MU-1", "MU-2", "MU-2", "Recycle", "Recycle"],
    "Function": ["Suction", "Discharge", "Suction", "Discharge", "Suction", "Discharge"],
    "Valve_Model": ["174CKD", "174CKD", "154CJD", "154CJD", "174JD", "174CKD"],
    "Plate_PN": ["52-090574", "52-090574", "52-090552", "52-090552", "52-090569", "80-333665"],
    "Lift_mm": [1.6, 1.6, 1.4, 1.4, 1.4, 2.0],
    "Torque_Nm": ["178-215", "178-215", "178-215", "178-215", "178-215", "178-215"]
}

df = pd.DataFrame(c711_master)

st.title("⚙️ Dresser-Rand C711 A/B: Parts & Maintenance")

# Navigation Sidebar
menu = st.sidebar.radio("Main Menu", ["Overhaul Search", "Visual Part Matcher", "Torque & Lift Checks"])

if menu == "Overhaul Search":
    st.header("Search by Stage")
    stage = st.selectbox("Select Stage", df["Stage"].unique())
    st.dataframe(df[df["Stage"] == stage], use_container_width=True)

elif menu == "Visual Part Matcher":
    st.header("Camera Verify")
    col1, col2 = st.columns(2)
    with col1:
        st.camera_input("Scan part in workshop")
    with col2:
        pn = st.selectbox("Compare with Part Number:", df["Plate_PN"].unique())
        st.info(f"Target Specs: {df[df['Plate_PN'] == pn]['Lift_mm'].values[0]}mm Lift")

elif menu == "Torque & Lift Checks":
    st.header("Critical Technical Hard-Stops")
    st.warning("**Safety Check:** All Lock Nuts (M20x1.5) must hit 178-215 Nm torque.")
    st.write("---")
    for index, row in df.iterrows():
        st.write(f"**{row['Stage']} {row['Function']}**: {row['Lift_mm']}mm Lift Required.")
