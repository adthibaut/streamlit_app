import streamlit
import pandas

streamlit.title('Mon application streamlit')
streamlit.header('Elle est super chouette')
streamlit.text('Mais elle reste un peu basique')
streamlit.text('Poulet 🐔')

streamlit.header('Et maintenant une liste de fruits parce que pourquoi pas?')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#pick in the list
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#affichage
streamlit.dataframe(my_fruit_list.loc[fruit_selected])
