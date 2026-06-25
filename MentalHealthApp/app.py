import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Mental Health Stress Detection")

age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["select", "Male", "Female", "Other"])
country = st.selectbox("Country",['select', 'United States',                 'Canada',         'United Kingdom',
               'Bulgaria',                 'France',               'Portugal',
            'Netherlands',            'Switzerland',                 'Poland',
              'Australia',                'Germany',                 'Russia',
                 'Mexico',                 'Brazil',               'Slovenia',
             'Costa Rica',                'Austria',                'Ireland',
                  'India',           'South Africa',                  'Italy',
                 'Sweden',               'Colombia',                 'Latvia',
                'Romania',                'Belgium',            'New Zealand',
                  'Spain',                'Finland',                'Uruguay',
                 'Israel', 'Bosnia and Herzegovina',                'Hungary',
              'Singapore',                  'Japan',                'Nigeria',
                'Croatia',                 'Norway',               'Thailand',
                'Denmark',                 'Greece',                'Moldova',])
self_employed = st.selectbox("Are you self-employed?",['select','Unknown', 'Yes', 'No'])
family_history = st.selectbox("Do you have a family history of mental illness?", ['select', 'Yes', 'No'])
work_interfere = st.selectbox("If you have a mental health condition, do you feel that it interferes with your work?",['select','Often', 'Rarely', 'Never', 'Sometimes', 'Unknown'])
no_employees = st.selectbox("How many employees does your company or organization have?",['select','6-25', 'More than 1000', '26-100', '100-500', '1-5', '500-1000'])
remote_work = st.selectbox("Do you work remotely (outside of an office) at least half of the time?",['select','No', 'Yes'])
tech_company = st.selectbox("Is your employer primarily a tech company/organization?",['select','Yes', 'No'])
benefits = st.selectbox("Does your employer provide mental health benefits?",["select","Yes", "Don't know", "No"])
care_options = st.selectbox("Do you know the options for mental health care your employer provides?",['select','Not sure', 'No', 'Yes'])
wellness_program = st.selectbox("Has your employer ever discussed mental health as part of an employee wellness program?",["select","No", "Don't know", "Yes"])
seek_help = st.selectbox("Does your employer provide resources to learn more about mental health issues and how to seek help?",['select','Yes', "Don't know", 'No'])
anonymity = st.selectbox("Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?",['select','Yes', "Don't know", 'No'])
leave = st.selectbox("How easy is it for you to take medical leave for a mental health condition?",['select','Somewhat easy',"Don't know", 'Somewhat difficult','Very difficult','Very easy'])
mental_health_consequence = st.selectbox("Do you think that discussing a mental health issue with your employer would have negative consequences?",['select','No', 'Maybe', 'Yes'])
phys_health_consequence = st.selectbox("Do you think that discussing a physical health issue with your employer would have negative consequences?",['select','No', 'Yes', 'Maybe'])
coworkers = st.selectbox("Would you be willing to discuss a mental health issue with your coworkers?",['select','Some of them', 'No', 'Yes'])
supervisor = st.selectbox("Would you be willing to discuss a mental health issue with your direct supervisor(s)?",['select','Yes', 'No', 'Some of them'])
mental_health_interview = st.selectbox("Would you bring up a mental health issue with a potential employer in an interview?",['select','No', 'Yes', 'Maybe'])
phys_health_interview = st.selectbox("Would you bring up a physical health issue with a potential employer in an interview?",['select','Maybe', 'No', 'Yes'])
mental_vs_physical = st.selectbox("Do you feel that your employer takes mental health as seriously as physical health?",['select','Yes', "Don't know", 'No'])
obs_consequence = st.selectbox("Have you heard of or observed negative consequences for coworkers with mental health conditions in your workplace?",['select','No', 'Yes'])




if st.button("Predict"):
    data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Country": [country],
        "self_employed":[self_employed],
        "family_history":[family_history],
        "work_interfere":[work_interfere],
        "no_employees":[no_employees],
        "remote_work":[remote_work],
        "tech_company":[tech_company],
        "benefits":[benefits],
        "care_options":[care_options],
        "wellness_program":[wellness_program],
        "seek_help":[seek_help],
        "anonymity":[anonymity],
        "leave":[leave],
        "mental_health_consequence":[mental_health_consequence],
        "phys_health_consequence":[phys_health_consequence],
        "coworkers":[coworkers],
        "supervisor":[supervisor],
        "mental_health_interview":[mental_health_interview],
        "phys_health_interview":[phys_health_interview],
        "mental_vs_physical":[mental_vs_physical],
        "obs_consequence":[obs_consequence]
    })
    inputs=["Age", "Gender", "Country", "self_employed", 
            "family_history", "work_interfere", "no_employees", 
            "remote_work", "tech_company", "benefits", "care_options",
            "wellness_program","seek_help", "anonymity", "leave",
            "mental_health_consequence","phys_health_consequence",
            "coworkers", "supervisor", "mental_health_interview",
            "phys_health_interview", "mental_vs_physical","obs_consequence"]
    for i in inputs:
        if data[i][0] == "select":
            st.warning(f"Please select a valid option for {i}.")
            st.stop()
        else:
            pass
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Potential Mental Stress Detected")
    else:
        st.success("No Significant Mental Stress Detected")