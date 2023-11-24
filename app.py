import pickle
from nltk.stem import WordNetLemmatizer
import streamlit as st
import nltk
from nltk.corpus import stopwords
nltk.download('wordnet')
stop_words = stopwords.words('english')

lemmatizer = WordNetLemmatizer()

def lemma(text):
    lemmatized = [lemmatizer.lemmatize(w,'v') for w in text.split()]
    return lemmatized

pipe = pickle.load(open("logistic_model.pkl","rb"))

st.title("Movie review  sentiments analysis")


st.markdown("""
            <style>
            .stDeployButton{
                visibility: hidden;
                
            }
            #MainMenu{
                visibility: hidden;
            }
            .stApp {
             background-image: url("https://wallpapers.com/images/hd/netflix-background-gs7hjuwvv2g0e9fj.jpg");
             background-attachment: fixed;
             background-size: cover;
             

            }
            #movie-review-sentiments-analysis{
             text-align: center;
             font-size: 50px;
             border: 8px solid rgb(255, 119, 255);
             border-radius: 5px;
             color: #00ff00;
             
            }
            p{
              
             color:#ffbf00;
             
            }
            </style>
            """,unsafe_allow_html=True)


user_input = st.text_input("Enter the review", "Type here")
st.write('<style>div.stButton > button:first-child {background-color: SlateBlue; color: white; border: none; border-radius: 5px; padding: 10px 20px; font-size: 16px; cursor: pointer; align: center;}</style>', unsafe_allow_html=True)
if st.button("Check the sentiments"):
    pred=pipe.predict([user_input])
    if(pred==1):
        css = """
        <style>
            .myclass {
            color: #40ff00;
            font-size: 34px;
            border: 4px solid Green;
            }
        </style>
        """

        text = "<p class='myclass'>Sentiment is Positive.</p>"

        st.markdown(css + text, unsafe_allow_html=True)
    elif(user_input=="" or user_input=="Type here"):
        st.write("Please enter the review")
    else:
        css = """
        <style>
            .myclass {
            color: red;
            font-size: 34px;
            border: 4px solid #ff4000;
            }
        </style>
        """

        text = "<p class='myclass'>Sentiment is negative.</p>"

        st.markdown(css + text, unsafe_allow_html=True)
    