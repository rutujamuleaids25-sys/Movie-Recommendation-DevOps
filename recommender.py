import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:

    def __init__(self, file_path):
        self.movies = pd.read_csv(file_path)

        self.movies["genres"] = self.movies["genres"].fillna("")

        self.vectorizer = TfidfVectorizer(
            token_pattern=r"(?u)\b\w+\b"
        )

        self.movie_matrix = self.vectorizer.fit_transform(
            self.movies["genres"]
        )

        self.similarity = cosine_similarity(
            self.movie_matrix
        )

    def recommend(self, movie_name, number=5):

        matches = self.movies[
            self.movies["title"].str.contains(
                movie_name,
                case=False,
                na=False
            )
        ]

        if matches.empty:
            return []

        index = matches.index[0]

        similarity_scores = list(
            enumerate(self.similarity[index])
        )

        similarity_scores = sorted(
            similarity_scores,
            key=lambda x: x[1],
            reverse=True
        )

        recommendations = []

        for movie_index, score in similarity_scores[1:number + 1]:

            recommendations.append(
                self.movies.iloc[movie_index]["title"]
            )

        return recommendations