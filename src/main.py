"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs from the dataset.")

    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop Recommendations")
    print("=" * 52)
    for i, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        reasons = explanation.split("; ")

        print(f"\n#{i}  {song['title']}  —  {song['artist']}")
        print(f"    Score: {score:.2f}")
        print(f"    Why this song:")
        for reason in reasons:
            print(f"      • {reason}")
    print("\n" + "=" * 52)


if __name__ == "__main__":
    main()
