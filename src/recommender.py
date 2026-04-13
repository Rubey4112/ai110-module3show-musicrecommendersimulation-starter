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
    target_valence: float = 0.5      # emotional brightness: 0.0 (dark) to 1.0 (euphoric)
    target_danceability: float = 0.5 # how dance-friendly: 0.0 (non-danceable) to 1.0
    target_tempo: float = 120.0      # preferred tempo in BPM

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Initialize the recommender with a list of songs."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs ranked by score against the given user profile."""
        from dataclasses import asdict
        user_prefs = asdict(user)
        scored = []
        for song in self.songs:
            song_dict = asdict(song)
            score, _ = score_song(user_prefs, song_dict)
            scored.append((song, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable explanation of why a song was recommended to the user."""
        from dataclasses import asdict
        user_prefs = asdict(user)
        song_dict = asdict(song)
        score, reasons = score_song(user_prefs, song_dict)
        if not reasons:
            return f"No strong preference matches found (score: {score:.2f})"
        return f"Score: {score:.2f} — " + "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv

    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

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
        reasons.append(f"mood matches '{user_prefs['favorite_mood']}' (+3.0 pts)")

    if song.get("genre") == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append(f"genre matches '{user_prefs['favorite_genre']}' (+1.0 pts)")

    # Energy proximity (0.0–1.0 → weighted ×4.0)
    target_energy = user_prefs.get("target_energy", 0.5)
    energy_points = 2.0 * (1 - abs(song["energy"] - target_energy))
    score += energy_points
    reasons.append(f"energy level ({song['energy']:.2f} vs target {target_energy:.2f}) (+{energy_points:.2f} pts)")

    # Acousticness proximity (0.0–1.0 → weighted ×1.5)
    acousticness_target = 0.8 if user_prefs.get("likes_acoustic", False) else 0.2
    acousticness_points = 1.5 * (1 - abs(song["acousticness"] - acousticness_target))
    score += acousticness_points
    reasons.append(f"acousticness ({song['acousticness']:.2f} vs target {acousticness_target:.2f}) (+{acousticness_points:.2f} pts)")

    # Valence proximity (0.0–1.0 → weighted ×1.5)
    target_valence = user_prefs.get("target_valence", 0.5)
    valence_points = 1.5 * (1 - abs(song["valence"] - target_valence))
    score += valence_points
    reasons.append(f"valence ({song['valence']:.2f} vs target {target_valence:.2f}) (+{valence_points:.2f} pts)")

    # Danceability proximity (0.0–1.0 → weighted ×1.5)
    target_danceability = user_prefs.get("target_danceability", 0.5)
    danceability_points = 1.5 * (1 - abs(song["danceability"] - target_danceability))
    score += danceability_points
    reasons.append(f"danceability ({song['danceability']:.2f} vs target {target_danceability:.2f}) (+{danceability_points:.2f} pts)")

    # Tempo proximity (BPM, normalized over ±120 BPM range → weighted ×1.5)
    target_tempo = user_prefs.get("target_tempo", 120.0)
    tempo_diff_norm = min(abs(song["tempo_bpm"] - target_tempo) / 120.0, 1.0)
    tempo_points = 1.5 * (1 - tempo_diff_norm)
    score += tempo_points
    reasons.append(f"tempo ({song['tempo_bpm']:.0f} BPM vs target {target_tempo:.0f} BPM) (+{tempo_points:.2f} pts)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No strong matches found"
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
