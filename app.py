import streamlit as st
import pandas as pd
import pickle

Quote_list=pd.read_pickle(open('Anime.pkl', 'rb'))
Quotes_list_=Quote_list['Quote'].values

similarity=pd.read_pickle(open('similarity.pkl', 'rb'))

def recommend(Quote):
    Quote_index = Quote_list[Quote_list['Quote'] == Quote].index[0]
    distances = similarity[Quote_index]
    quote_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:4]
    recommended_Quote = []
    Character_Name=[]
    Anime_Name=[]
    for i in quote_list:
        recommended_Quote.append(Quote_list.iloc[i[0]].Quote)
        Character_Name.append(Quote_list.iloc[i[0]].Character)
        Anime_Name.append(Quote_list.iloc[i[0]].Anime)


    return recommended_Quote,Character_Name,Anime_Name

st.title('Anime Quotes')

selected_quote_name= st.selectbox(
    "How would you like to be contacted?",
    Quotes_list_
)

if st.button("Recommend", type="primary"):
    recommended_Quote,Character_Name,Anime_Name=recommend(selected_quote_name)
    tab1, tab2, tab3  = st.tabs([Character_Name[0], Character_Name[1], Character_Name[2]])
    with tab1:
        st.header('Quote:')
        st.title(recommended_Quote[0])

    with tab2:
        st.header('Quote:')
        st.title(recommended_Quote[1])

    with tab3:
        st.header('Quote:')
        st.title(recommended_Quote[2])