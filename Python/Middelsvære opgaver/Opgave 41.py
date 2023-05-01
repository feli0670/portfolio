import streamlit as st

firstName = st.text_input("Fornavn", "Skriv det her...")
lastName = st.text_input("Efternavn", "Skriv det her...")
firstNameResult = firstName.title()
lastNameResult = lastName.title()
name = (f'{firstNameResult } {lastNameResult}')
if(st.button('OK')):
    st.text(f'Hej {name} 😉')


def perMilleCalculator():
    if(st.button('Beregn Promille')):
        perMille = round((12*int(item))/(factor*int(weight)),2)
        if(perMille>3):
            st.text(f'{name}, din promille er: {perMille} - risiko for at dø')
        elif(perMille>1):
            st.text(f'{name}, din promille er: {perMille} - mindre kontrol over balance, risiko for bevidstløshed samt opkast')

def bmiCalculator():
    height = st.text_input("Højde i meter", "Skriv din højde i meter her...")
    if(st.button('Beregn BMI')):
        bmi = round(float(weight)/(float(height)*float(height)),2)
        if(bmi>30):
            st.text(f'Din BMI er; {bmi} - svært overvægtig')
        elif(bmi>25):
            st.text(f'Din BMI er; {bmi} - overvægtig')
        elif(bmi>18.5):
            st.text(f'Din BMI er; {bmi} - normalvægtig')
        else:
            st.text(f'Din BMI er; {bmi} - undervægtig')


Male = st.checkbox("Male")
Female = st.checkbox("Female")

if(Male):
    item = st.text_input("Genstand - Mand", "Skriv antal genstande drukket..")
    weight = st.text_input("Vægt - Mand", "Skriv din vægt i kg...")
    factor=0.68
    perMilleCalculator()
    bmiCalculator()


if(Female):
    item = st.text_input("Genstand - Kvinde", "Skriv antal genstande drukket..")
    weight = st.text_input("Vægt - Kvinde", "Skriv din vægt i kg...")
    factor = 0.55
    perMilleCalculator()
    bmiCalculator()
