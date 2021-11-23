import streamlit as st
import numpy as np
import Music_recommendation

st.title('Music Recommendation')
st.write('Only songs from 1920 to 2020')
name = st.text_input('Enter your favorite song')
author = st.text_input("Enter the author(if there are more than one author, separate them with comma(e.g.  author1, "
                      "author2 ...)")
if name not in [None, ''] and author not in [None, '']:
	author = str([author.strip().title() for author in author.split(',')])
	try:
		recommendation = Music_recommendation.getSong_recommendations(name, author)
		recommendation.reset_index(drop=True, inplace=True)
		recommendation.index = np.arange(1, len(recommendation) + 1)
		st.write('Here is 10 songs we recommend to you, thank you for using our service, enjoy <3')
		st.dataframe(recommendation)
	except:
		st.write("""
		This song is not exist. 
		Please consider the followings
		+ Choose songs from 1920 to 2020
		+ Enter the authors in correct syntax
		+ Try swapping the order of the authors
		""")
