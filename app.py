from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# ------------------ Load Data ------------------

df = pd.read_csv("preprocessed_music_data.csv")
cosine_sim = joblib.load("cosine_sim_matrix.joblib")
categories = joblib.load("categories.joblib")

FILTERS = {
    "region": "Region",
    "festival": "Festival",
    "tradition": "Tradition",
}

RESULT_COLUMNS = [
    "Song Name",
    "Author",
    "Region",
    "Festival",
    "Tradition",
    "URL",
]

# ---------------- Recommendation Function ----------------

def get_recommendations(top_n=10, **filters):
    filtered = df

    for key, column in FILTERS.items():
        value = filters.get(key)
        if value:
            filtered = filtered[
                filtered[column].str.contains(value, case=False, na=False)
            ]

    if filtered.empty:
        return []

    idx = filtered.sample().index[0]

    similar = (
        cosine_sim[idx]
        .argsort()[::-1][1:top_n + 1]
    )

    return df.loc[similar, RESULT_COLUMNS].to_dict("records")


# -------------------- Routes --------------------

@app.get("/")
def home():
    return render_template("index.html")


@app.post("/recommend")
def recommend():
    data = request.get_json(silent=True) or {}

    filters = {
        key: data.get(key, "")
        for key in FILTERS
    }

    return jsonify(get_recommendations(**filters)), 200


@app.get("/categories")
def get_categories():
    return jsonify(categories), 200


# -------------------- Main --------------------

if __name__ == "__main__":
    app.run(debug=True)

