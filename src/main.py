"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs
from tabulate import tabulate, SEPARATING_LINE


def print_profile_table(name: str, profile: dict) -> None:
    rows = [
        ["Favorite Genre",     profile["favorite_genre"].title()],
        ["Favorite Mood",      profile["favorite_mood"].title()],
        ["Target Energy",      f"{profile['target_energy']:.2f}"],
        ["Likes Acoustic",     "Yes" if profile["likes_acoustic"] else "No"],
        ["Target Valence",     f"{profile['target_valence']:.2f}"],
        ["Target Danceability",f"{profile['target_danceability']:.2f}"],
        ["Target Tempo",       f"{profile['target_tempo']:.0f} BPM"],
    ]
    print(f"\n  Profile: {name}")
    print(tabulate(rows, headers=["Attribute", "Value"], tablefmt="outline"))


def print_recommendations_table(recommendations: list) -> None:
    rows = []
    for i, (song, score, _) in enumerate(recommendations, 1):
        rows.append([
            f"#{i}",
            song["title"],
            song["artist"],
            song["genre"].title(),
            song["mood"].title(),
            f"{score:.2f}",
        ])
    print("\n  Top Recommendations")
    print(tabulate(
        rows,
        headers=["Rank", "Title", "Artist", "Genre", "Mood", "Score"],
        tablefmt="outline",
        colalign=("center", "left", "left", "left", "left", "right"),
    ))


def print_breakdown_table(recommendations: list) -> None:
    rows = []
    for i, (_, _, explanation) in enumerate(recommendations, 1):
        reasons = explanation.split("; ")
        for j, reason in enumerate(reasons):
            rank_label = f"#{i}" if j == 0 else ""
            rows.append([rank_label, reason])
        if i < len(recommendations):
            rows.append(SEPARATING_LINE)
    print("\n  Scoring Breakdown")
    print(tabulate(rows, headers=["Rank", "Factor & Points"], tablefmt="outline"))


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"\nLoaded {len(songs)} songs from the dataset.")

    # Profile 1 — The Sad Banger
    sad_banger = {
        "favorite_genre": "pop",
        "favorite_mood": "sad",
        "target_energy": 0.95,
        "likes_acoustic": False,
        "target_valence": 0.3,
        "target_danceability": 0.9,
        "target_tempo": 140.0,
    }

    # Profile 2 — The Classical Happy Fan
    classical_happy = {
        "favorite_genre": "classical",
        "favorite_mood": "happy",
        "target_energy": 0.5,
        "likes_acoustic": True,
        "target_valence": 0.8,
        "target_danceability": 0.3,
        "target_tempo": 80.0,
    }

    # Profile 3 — The Acoustic Raver
    acoustic_raver = {
        "favorite_genre": "edm",
        "favorite_mood": "chill",
        "target_energy": 0.9,
        "likes_acoustic": True,
        "target_valence": 0.6,
        "target_danceability": 0.95,
        "target_tempo": 128.0,
    }

    profile_names = ["The Sad Banger", "The Classical Happy Fan", "The Acoustic Raver"]
    adversarial_profiles = [sad_banger, classical_happy, acoustic_raver]

    for name, profile in zip(profile_names, adversarial_profiles):
        recommendations = recommend_songs(profile, songs, k=5)
        print("\n" + "=" * 62)
        print_profile_table(name, profile)
        print_recommendations_table(recommendations)
        print_breakdown_table(recommendations)

    print("\n" + "=" * 62 + "\n")


if __name__ == "__main__":
    main()
