# Sample movie dataset
movies = [
    {'title': 'The Matrix', 'genres': ['Action', 'Sci-Fi']},
    {'title': 'Inception', 'genres': ['Action', 'Sci-Fi', 'Thriller']},
    {'title': 'Interstellar', 'genres': ['Adventure', 'Drama', 'Sci-Fi']},
    {'title': 'The Godfather', 'genres': ['Crime', 'Drama']},
    {'title': 'Pulp Fiction', 'genres': ['Crime', 'Drama']},
    {'title': 'The Dark Knight', 'genres': ['Action', 'Crime', 'Drama']},
    {'title': 'Forrest Gump', 'genres': ['Drama', 'Romance']},
]

# Function to get movie recommendations based on a specified genre
def genre_based_recommendations(genre):
    recommendations = []
    
    for movie in movies:
        if genre in movie['genres']:
            recommendations.append(movie['title'])
    
    return recommendations

# Main program to prompt the user for a genre and provide recommendations
if __name__ == "__main__":
    user_genre = input("Enter a genre: ").strip()
    recommendations = genre_based_recommendations(user_genre)
    
    if recommendations:
        print(f"Movies in the genre '{user_genre}':")
        for title in recommendations:
            print(f"- {title}")
    else:
        print(f"No movies found in the genre '{user_genre}'")
