import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))


if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

st.markdown(
    """
    ---
    Made with ❤️ by [Constantin Mierlă](https://www.linkedin.com/in/constantinmierla/)  
    📂 [GitHub](https://github.com/constantinmierla) | 🔗 [LinkedIn](https://www.linkedin.com/in/constantinmierla/)
    """,
    unsafe_allow_html=True
)