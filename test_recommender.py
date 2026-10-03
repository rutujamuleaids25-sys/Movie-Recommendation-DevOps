from recommender import MovieRecommender


def test_model_loads():

    model = MovieRecommender(
        "data/movies.csv"
    )

    assert len(model.movies) > 0


def test_recommendation():

    model = MovieRecommender(
        "data/movies.csv"
    )

    result = model.recommend(
        "Toy Story",
        5
    )

    assert len(result) > 0