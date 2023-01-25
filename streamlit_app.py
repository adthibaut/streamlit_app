import streamlit
import pandas

streamlit.title('Mon application streamlit')
streamlit.header('Elle est super chouette')
streamlit.text('Mais elle reste un peu basique')
streamlit.text('Poulet 🐔')

streamlit.header('Et maintenant une liste de fruits parce que pourquoi pas?')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt", index = True)
streamlit.dataframe(my_fruit_list)

#pick in the list
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
