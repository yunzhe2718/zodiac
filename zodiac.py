import streamlit as st
import datetime
from lunarcalendar import Converter, Solar
from PIL import Image

zoo = ["Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog"]

icons = []
for animal in zoo:
    icons.append(Image.open("img/" + animal + ".png"))

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
    max_value=datetime.date(2030, 12, 31))

if st.button("Calculate"):
    result = zodiac_calculator(birthdate)
    zodiac_name = zoo[result]
    st.write(f"Your Chinese zodiac sign is the **{zodiac_name}**. ")
    # make 2 columns to display a smaller icon
    col1, col2 = st.columns(2)
    with col1:
        st.image(icons[result], use_column_width=True)