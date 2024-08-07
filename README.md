# Content-Based Movie Recommendation System

This project is a content-based movie recommendation system built using Streamlit. The app takes a movie title as input and suggests 5 similar movies along with their posters. The recommendation is achieved using cosine similarity.

## Features

- **User Input**: Enter a movie title to get recommendations.
- **Recommendations**: Displays 5 similar movies based on content similarity.
- **Posters**: Shows movie posters for each recommended movie fetched from the TMDB API.
- **Live Hosting**: The app is hosted on a live server in Streamlit.

## How It Works

1. **Input**: User provides a movie title.
2. **Processing**: 
   - The system calculates the cosine similarity between the input movie and all other movies in the dataset.
   - It then selects the top 5 movies with the highest similarity scores.
3. **Output**: The app displays the titles and posters of the recommended movies fetched from the TMDB API.
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

## Similarity Score (Main concept of this Project) :
How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of 
zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity 
score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the 
cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even 
if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be
oriented closer together. The smaller the angle, higher the cosine similarity.

![cosinepng](https://github.com/user-attachments/assets/aaa30104-e357-44a1-a200-1aed35a6daef)
#### More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/) 

## Technologies Used

- **Streamlit**: For building the web application.
- **Cosine Similarity**: For calculating content similarity between movies.
- **TMDB API**: For fetching movie posters.
- **Python**: For the backend logic and calculations.
- **Pandas**: For data manipulation.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/movie-recommender.git
    cd movie-recommender
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## File Structure

- `app.py`: The main Streamlit application file.
- `requirements.txt`: The list of required Python packages.
- `movie_recommender_system_prt1.ipynb`: Notebook containing data processing and similarity calculation.
- `movie_recommender_system_prt2.ipynb`: Notebook containing additional analysis or visualization (if applicable).

## How to Use

1. Open the app by running the command `streamlit run app.py`.
2. Enter the title of a movie in the input box.
3. Click on the 'Recommend' button.
4. View the recommended movies along with their posters.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


