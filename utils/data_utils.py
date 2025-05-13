import csv

from models.movie import Movie


def is_duplicate_movie(movie_name: str, seen_names: set) -> bool:
    return movie_name in seen_names


def is_complete_movie(movie: dict, required_keys: list) -> bool:
    return all(key in movie for key in required_keys)


def save_movie_to_csv(movies: list, filename: str):
    if not movies:
        print("No venues to save.")
        return

    # Use field names from the Venue model
    fieldnames = Movie.model_fields.keys()

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(movies)
    print(f"Saved {len(movies)} venues to '{filename}'.")
