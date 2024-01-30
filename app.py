<<<<<<< HEAD
# -*- coding: utf-8 -*-

import streamlit as st
import seaborn as sns

@data_cache
def load_data():
    data = sns.load_dataset("iris")
    return data
def main():
    st.title("Hello world on strealit.io")

if __name__ == "__main__":
=======
# -*- coding: utf-8 -*-

import streamlit as st
import seaborn as sns

@data_cache
def load_data():
    data = sns.load_dataset("iris")
    return data
def main():
    st.title("Hello world on strealit.io")

if __name__ == "__main__":
>>>>>>> f42a5da28ceb3dad3b0666ad59bc6a69587e2ee1
    main()