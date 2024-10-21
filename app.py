import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    # Setting up the title and description with emojis for better visuals.
    st.title("🌡️ Temperature Converter")
    st.markdown("""
    Welcome to the **Temperature Converter** app! 
    Easily convert temperatures between Celsius and Fahrenheit with just a few clicks. 
    Select a conversion type, input your value, and get the result instantly! 🚀
    """)
    
    # Sidebar for selecting the conversion type for better separation.
    st.sidebar.header("Conversion Settings")
    option = st.sidebar.radio(
        "Choose the conversion type:",
        ("Celsius to Fahrenheit", "Fahrenheit to Celsius")
    )
    
    # Display appropriate input field based on the selected conversion type.
    if option == "Celsius to Fahrenheit":
        st.subheader("Convert Celsius to Fahrenheit")
        celsius = st.slider("Select temperature in Celsius:", min_value=-100.0, max_value=100.0, value=0.0, step=0.1)
        if st.button("🔄 Convert"):
            fahrenheit = celsius_to_fahrenheit(celsius)
            st.success(f"🎯 {celsius}°C is equal to {fahrenheit:.2f}°F")
            st.balloons()  # Adds a fun animation when conversion is successful.
    
    elif option == "Fahrenheit to Celsius":
        st.subheader("Convert Fahrenheit to Celsius")
        fahrenheit = st.slider("Select temperature in Fahrenheit:", min_value=-148.0, max_value=212.0, value=32.0, step=0.1)
        if st.button("🔄 Convert"):
            celsius = fahrenheit_to_celsius(fahrenheit)
            st.success(f"🎯 {fahrenheit}°F is equal to {celsius:.2f}°C")
            st.balloons()  # Adds a fun animation when conversion is successful.
    
    # Footer with additional info.
    st.markdown("""
    ---
    Created with ❤️ using [Streamlit](https://streamlit.io).
    """)

if __name__ == "__main__":
    main()
