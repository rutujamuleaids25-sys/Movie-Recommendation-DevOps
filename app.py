import streamlit as st
from recommender import MovieRecommender


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies similar to your favorite movie."
)


@st.cache_resource
def load_model():
    return MovieRecommender("data/movies.csv")


recommender = load_model()


movie = st.text_input(
    "Enter a movie name"
)

number = st.slider(
    "Number of recommendations",
    1,
    10,
    5
)


if st.button("Recommend Movies"):

    if movie.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        recommendations = recommender.recommend(
            movie,
            number
        )

        if recommendations:

            st.subheader("Recommended Movies")

            for i, recommendation in enumerate(
                recommendations,
                start=1
            ):
                st.write(
                    f"{i}. {recommendation}"
                )

        else:

            st.error(
                "Movie not found. Try another movie."
            )