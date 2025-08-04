# Indian-Music-Recommendation-System-Using-Ai-ML
# Indian Music Recommendation System

## Overview
This project is a music recommendation system built using AI and machine learning concepts. The system analyzes user preferences and recommends Indian music tracks based on a similarity measure. The core of the recommendation engine is powered by a content-based filtering approach using a cosine similarity matrix.

## Features
- **Music Recommendation**: Provides personalized music recommendations based on user preferences.
- **Web Interface**: A user-friendly web application for interacting with the system.
- **Data Preprocessing**: Prepares the raw dataset for recommendation by cleaning and organizing the data.
- **Efficient Similarity Calculation**: Uses a precomputed cosine similarity matrix for fast recommendations.

## File Structure

```
Indian Music Recommendation/
|-- app.py                       # Main application script
|-- categories.joblib            # Serialized category data
|-- cosine_sim_matrix.joblib     # Precomputed cosine similarity matrix
|-- data_Music.ipynb             # Jupyter Notebook for data preprocessing
|-- home.html                    # Homepage for the web application
|-- music_indian.csv             # Raw dataset
|-- preprocessed_music_data.csv  # Processed dataset
|-- static/                      # Static assets (CSS, JS, images)
|-- templates/                   # HTML templates
```

## Requirements

- Python 3.x
- Libraries:
  - Flask
  - Pandas
  - Scikit-learn
  - Joblib
  - Numpy

Install the dependencies using:

```bash
pip install -r requirements.txt
```
## How to Run

1. **Clone the Repository**:

   ```bash
   git clone <repository_url>
   cd Indian Music Recommendation
   ```

2. **Prepare the Data**:

   - Open the `data_Music.ipynb` notebook.
   - Run all cells to preprocess the dataset and generate necessary files.

3. **Start the Application**:

   ```bash
   python app.py
   ```

4. **Access the Web App**:

   - Open your browser and navigate to `http://127.0.0.1:5000`.

## Dataset

- **Raw Data**: `music_indian.csv` contains metadata about Indian music tracks, including genres, artists, and features.
- **Preprocessed Data**: `preprocessed_music_data.csv` is the cleaned and organized version of the dataset.

## Technical Details

- **Recommendation Engine**:
  - The system uses content-based filtering.
  - A cosine similarity matrix (`cosine_sim_matrix.joblib`) is precomputed to determine the similarity between music tracks.
- **Web Framework**: Flask is used to create the web interface.

## Future Improvements

- Add collaborative filtering to enhance recommendations.
- Include real-time user feedback for dynamic recommendations.
- Expand the dataset with more diverse music genres and languages.
- Deploy the application to a cloud platform for public access.

## License

This project is open-source and developed by Team Logic Lords

## Acknowledgments
Special thanks to the contributors and the open-source community for their support. 
