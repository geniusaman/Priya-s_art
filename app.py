import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS for clickable images
st.markdown("""
<style>
.clickable-image {
    cursor: pointer;
    transition: transform 0.3s;
}
.clickable-image:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("pihulogo.png", use_column_width=True)
with col2:
    st.text_input("Search...")
with col3:
    st.button("Cart")
    st.button("Login")

# Banner (make it clickable)
banner_clicked = st.image("pihubanner.jpeg", use_column_width=True)
if banner_clicked:
    st.write("Banner clicked! Add your action here.")

st.write("Sustainably Handmade with Love")

# Promotional bar
st.info("Get a complimentary Octopus Plushie worth Rs 200 when you make a purchase of Rs 1000 or more")

# New In section
st.header("New In")
col1, col2, col3, col4 = st.columns(4)

def clickable_image(image_path, caption=""):
    st.image(image_path, use_column_width=True)
    clicked = st.button(caption, key=image_path)
    if clicked:
        st.write(f"You clicked on {caption}")
    return clicked

with col1:
    clickable_image("pihu2.jpeg", "Product 1")
with col2:
    clickable_image("pihu3.jpeg", "Product 2")
with col3:
    clickable_image("pihu5.jpeg", "Product 3")
with col4:
    clickable_image("pihu1.jpeg", "Product 4")