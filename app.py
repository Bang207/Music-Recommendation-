import streamlit as st
import numpy as np
import Music_recommendation

st.title('Music Recommendation')
name = st.text_input('Enter your favorite song')
author = st.text_input("Enter the author(if there are more than one author, separate them with comma(e.g.  author1, "
                      "author2 ...)")
if name not in [None, ''] and author not in [None, '']:
	author = str([author.strip().title() for author in author.split(',')])
	recommendation = Music_recommendation.getSong_recommendations(name, author)
	recommendation.reset_index(drop=True, inplace=True)
	recommendation.index = np.arange(1, len(recommendation) + 1)
	st.dataframe(recommendation)
