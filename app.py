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

def get_recommendations(region='', festival='', tradition='', cosine_sim=cosine_sim):
    # Filter the dataframe based on user selections
    mask = (
        (df['Region'].str.contains(region, case=False, na=False) if region else True) &
        (df['Festival'].str.contains(festival, case=False, na=False) if festival else True) &
        (df['Tradition'].str.contains(tradition, case=False, na=False) if tradition else True)
    )
    filtered_df = df[mask]
    
    if filtered_df.empty:
        return []

    idx = filtered_df.sample().index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    item_indices = [i[0] for i in sim_scores]
    
    return df.iloc[item_indices][['Song Name', 'Author', 'Region', 'Festival', 'Tradition', 'URL']].to_dict('records')

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
