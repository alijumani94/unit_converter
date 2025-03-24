import streamlit as st

st.markdown(" ***Unit Converter*** ")

conversion_category = st.selectbox(
    "Select conversion category",
    ["weight", "length", "volume"]
)

if conversion_category == "length":
    from_unit = st.selectbox(
        "From unit",
        ["kilometer", "meter", "inches", "feet", "miles"]
    )
    to_unit = st.selectbox(
        "To unit",
        ["kilometer", "meter", "inches", "feet", "miles"]
    )

elif conversion_category == "weight":
    from_unit = st.selectbox(
        "From unit",
        ["gram", "kilogram", "pound", "ounce"]
    )
    to_unit = st.selectbox(
        "To unit",
        ["gram", "kilogram", "pound", "ounce"]
    )

elif conversion_category == "volume":
    from_unit = st.selectbox(
        "From unit",
        ["liter", "milliliter", "gallon", "cubic meter"]
    )
    to_unit = st.selectbox(
        "To unit",
        ["liter", "milliliter", "gallon", "cubic meter"]
    )

length_factors = {
    "kilometer": 1000,
    "meter": 1,
    "inches": 0.0254,
    "feet": 0.3048,
    "miles": 1609.34
}

weight_factors = {
    "gram": 1,
    "kilogram": 1000,
    "pound": 453.592,
    "ounce": 28.3495
}

volume_factors = {
    "liter": 1,
    "milliliter": 0.001,
    "gallon": 3.78541,
    "cubic meter": 1000
}

value = st.number_input("Enter value to convert", value=1.0)

def convert_units(value, from_unit, to_unit, factors):
    if from_unit in factors and to_unit in factors:
        from_factor = factors[from_unit]
        to_factor = factors[to_unit]
        return value * from_factor / to_factor
    else:
        st.error("Invalid unit selection.")
        return None

if st.button("Convert"):
    if conversion_category == "length":
        result = convert_units(value, from_unit, to_unit, length_factors)
        if result is not None:
            st.write(f"{value} {from_unit}s= {result}{to_unit}s")
    
    elif conversion_category == "weight":
        result = convert_units(value, from_unit, to_unit, weight_factors)
        if result is not None:
            st.write(f"{value} {from_unit}s= {result}{to_unit}s")
    
    elif conversion_category == "volume":
        result = convert_units(value, from_unit, to_unit, volume_factors)
        if result is not None:
            
            st.write(f"{value} {from_unit}s= {result}{to_unit}s")
