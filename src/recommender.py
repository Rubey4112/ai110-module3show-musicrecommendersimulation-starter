from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    """ 
    target_acousticness: float  # replaces likes_acoustic bool; use 0.0–1.0 range
    target_valence: float       # emotional brightness preference: 0.0 (dark) to 1.0 (euphoric)
    """

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    # Categorical matches
    if song.get("mood") == user_prefs.get("favorite_mood"):
        score += 3.0
        reasons.append(f"mood matches '{user_prefs['favorite_mood']}'")

    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append(f"genre matches '{user_prefs['favorite_genre']}'")

    # Energy proximity (0.0–1.0 → weighted ×2.0)
    target_energy = user_prefs.get("target_energy", 0.5)
    score += 2.0 * (1 - abs(song["energy"] - target_energy))
    if abs(song["energy"] - target_energy) <= 0.15:
        reasons.append(f"energy level is close to your target ({song['energy']:.2f})")

    # Acousticness proximity (0.0–1.0 → weighted ×1.5)
    acousticness_target = 0.8 if user_prefs.get("likes_acoustic", False) else 0.2
    score += 1.5 * (1 - abs(song["acousticness"] - acousticness_target))
    if abs(song["acousticness"] - acousticness_target) <= 0.2:
        reasons.append("acousticness fits your preference")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
