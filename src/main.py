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
        "target_valence": 0.8,
        "target_danceability": 0.7,
        "target_tempo": 120.0,
    }

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

    adversarial_profiles = [sad_banger, classical_happy, acoustic_raver]

    for profile in adversarial_profiles:
        recommendations = recommend_songs(profile, songs, k=5)

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
