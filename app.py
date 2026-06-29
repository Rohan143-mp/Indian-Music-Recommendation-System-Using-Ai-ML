from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load preprocessed data and matrices
df = pd.read_csv('preprocessed_music_data.csv')
cosine_sim = joblib.load('cosine_sim_matrix.joblib')
categories = joblib.load('categories.joblib')

def get_recommendations(region=None, festival=None, tradition=None, top_n=10):
    # Start with all rows
    filtered_df = df

    # Apply filters only if values are provided
    if region:
        filtered_df = filtered_df[
            filtered_df["Region"].str.contains(region, case=False, na=False)
        ]

    if festival:
        filtered_df = filtered_df[
            filtered_df["Festival"].str.contains(festival, case=False, na=False)
        ]

    if tradition:
        filtered_df = filtered_df[
            filtered_df["Tradition"].str.contains(tradition, case=False, na=False)
        ]

    # No matching records
    if filtered_df.empty:
        return []

    # Select one matching song
    idx = filtered_df.sample(1).index[0]

    # Get similarity scores
    sim_scores = cosine_sim[idx]

    # Get indices of top similar songs (excluding itself)
    top_indices = sim_scores.argsort()[::-1][1:top_n + 1]

    # Return recommendations
    return (
        df.loc[top_indices,
               ["Song Name", "Author", "Region", "Festival", "Tradition", "URL"]]
        .to_dict("records")
    )

@app.route('/')

def home():
    return render_template('index.html')
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    recommendations = get_recommendations(
        region=data.get('region', ''),
        festival=data.get('festival', ''),
        tradition=data.get('tradition', '')
    )
    return jsonify(recommendations)

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

if __name__ == '__main__':
    app.run(debug=True)


