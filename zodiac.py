import streamlit as st
import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

zodiac_list = ["Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog"]

def zodiac_calculator(birthdate):
    solar = Solar.from_date(birthdate)
    lunar = Converter.Solar2Lunar(solar)
    zodiac_index = (lunar.year - 2019 ) % 12
    return zodiac_index

st.title("Chinese Zodiac Calculator")
st.write("Enter your date of birth to calculate your Chinese zodiac sign.")

birthdate = st.date_input("Enter your date of birth", 
    value=datetime.date(2000, 1, 1),     
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today())

if st.button("Calculate"):
    result = zodiac_list[zodiac_calculator(birthdate)]
    st.write(f"Your Chinese zodiac sign is the **{result}**. ")
