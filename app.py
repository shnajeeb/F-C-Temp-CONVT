import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    st.title("🌡️ Temperature Converter")
    st.write("Easily convert temperatures between Celsius and Fahrenheit.")

    option = st.selectbox(
        "Choose the conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )
    
    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:", value=0.0, step=0.1)
        if st.button("Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0, step=0.1)
        if st.button("Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    main()
