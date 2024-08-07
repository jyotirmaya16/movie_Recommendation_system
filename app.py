import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=bc4eb15169a481ca444b8342939febee&language=en-US')
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/original" + poster_path
        else:
            # st.error("Poster path not found.")
            return None
    except requests.RequestException as e:
        # st.error(f"Error fetching poster: {e}")
        return None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
   
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        poster_url = fetch_poster(movie_id)
        if poster_url:
            recommended_movies_posters.append(poster_url)
        else:
            # Fallback to a default image if poster is not available
            recommended_movies_posters.append("https://via.placeholder.com/500x750?text=No+Poster+Available")
    return recommended_movies, recommended_movies_posters

# Load movie data
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)  # Assuming movies_dict is a dictionary with a 'title' key

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

#_____________________banner image__________
st.markdown(
    """
    <style>
    .banner {
        position: relative;
        background-image: url('https://github.com/Mega987/fsdf/blob/main/postor%20.png?raw=true');
        background-size: cover;
        background-position: center;
        height: 112px; /* Adjust the height as needed */
        width: 700px; /* Ensure the banner spans the full width */
        text-align: center;
        color: white;
        font-size: 2em;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    <div class="banner">
        Movie Recommender System
    </div>
    """,
    unsafe_allow_html=True
)
#_________________end____________________

selected_movie_name = st.selectbox('Choose your movie', sorted(movies['title'].values, key=lambda x: (not x[0].isalpha(), x)))

if st.button('Recommend'):
    with st.spinner('Wait, let me find similar Movies for you...'):
        names, posters = recommend(selected_movie_name)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        for idx, (name, poster) in enumerate(zip(names, posters)):
            if idx == 0:
                with col1:
                    st.text(name)
                    st.image(poster)
            elif idx == 1:
                with col2:
                    st.text(name)
                    st.image(poster)
            elif idx == 2:
                with col3:
                    st.text(name)
                    st.image(poster)
            elif idx == 3:
                with col4:
                    st.text(name)
                    st.image(poster)
            elif idx == 4:
                with col5:
                    st.text(name)
                    st.image(poster)
                    
#__________________________footer________________
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background:linear-gradient(to right, #28313B, #485461);
        color: white;
        text-align: center;
        padding: 10px;
    }
    .footer a {
        color: white;
        margin: 0 2px;
        text-decoration: none;
    }
    .footer img {
        width: 28px;
        height: auto;
        vertical-align: middle;
        margin-right: 5px;
    }

    </style>
    <div class="footer">
        Content Based MRS. Trained with 11k+ Movies. by Jyotirmaya
        <a href="https://www.linkedin.com/in/jyotirmaya-maharana-a32333299/" target="_blank">
            <img src="https://github.com/jyotirmaya16/jyotirmaya16/assets/146333462/ba826ab4-7b04-4aa3-85bf-6e8806c59950" alt="LinkedIn" > 
        </a>
        <a href="https://public.tableau.com/app/profile/jyotirmaya.maharana/vizzes" target="_blank">
            <img src="https://github.com/jyotirmaya16/jyotirmaya16/assets/146333462/475e5f4d-aaba-42e1-9a7e-b5f21d925f87" alt="Tableau" >
        </a>
        <a href="https://jyotirmaya16.github.io/portfolio.github.io/" target="_blank" >
            <img src="https://github.com/jyotirmaya16/jyotirmaya16/assets/146333462/4ed4c65b-144f-4d94-a662-286dc8cb0347" alt="Portfolio" >
        </a>
        <a href="https://www.instagram.com/jyotirmayamaharana/?hl=en" target="_blank">
            <img src="https://github.com/jyotirmaya16/jyotirmaya16/assets/146333462/654bd059-f6aa-4ed1-a203-08e406d78798" alt="Instagram" >
        </a>
    """,
    unsafe_allow_html=True
)
#____________________end________________________