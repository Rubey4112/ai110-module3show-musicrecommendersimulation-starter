# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Each song in the catalog is described by ten attributes: a unique ID, title, artist, genre, mood, energy level, tempo, valence, danceability, and acousticness. The system only uses four of those attributes when scoring — genre, mood, energy, and acousticness. The rest are stored but not yet factored in.

A user is represented by a taste profile that captures four preferences: their favorite genre, their favorite mood, a target energy level (on a 0.0–1.0 scale), and whether or not they enjoy acoustic music.

When a recommendation is requested, every song in the catalog is scored against that profile. The score is built up from four independent contributions:

- **Mood match** — if the song's mood matches the user's favorite, add 3 points
- **Genre match** — if the song's genre matches the user's favorite, add 2 points
- **Energy proximity** — add up to 2 points depending on how close the song's energy is to the user's target (songs further away earn fewer points)
- **Acousticness fit** — add up to 1.5 points depending on how well the song's acoustic quality matches whether the user likes acoustic music

The songs are then sorted from highest to lowest score and the top-k are returned as recommendations.

**Potential biases to be aware of:**

- Mood carries the most weight (3 pts), so a perfect mood match can push a song to the top even if genre, energy, and acousticness are all poor fits.
- Genre and mood are exact-match only — a "pop" fan scores 0 for "indie pop", even if those songs would be a great fit in practice.
- Tempo, valence, and danceability are collected but ignored entirely by the scorer, so two very different-sounding songs can receive identical scores.
- The acoustic preference is treated as a simple yes/no, which maps to fixed targets of 0.8 or 0.2. A user who only mildly likes acoustic music is treated the same as one who exclusively listens to it.

Real world recommendation systems in products like YouTube and Spotify primarily use two types of prediction:

- Contant-Based Filtering: Recommending songs based on similar song attributes like genre and tmepo
- Collaborative Filtering: Recommending songs that other users similar to you has liked. "Users like you also listened to..."

The current system for this ranker uses a simple algorithm with four parameter, if the song genre and mood matches the user favorite, how close the song is to the user energy level and whether the user like accoustic song
$$\text{score} = 0.50 \cdot M + 0.30 \cdot G + 0.15 \cdot E + 0.05 \cdot A$$


| Profile | Signals in conflict | Expected result | Actual result | Weakness exposed |
|---|---|---|---|---|
| Sad Banger | `favorite_mood: "sad"` vs `favorite_genre: "pop"` + `target_energy: 0.95` | Sad, slow song (Mississippi Low) | Energetic pop (Gym Hero) | Mood (+3.0) can be beaten by genre (+2.0) + strong energy proximity (~+2.0) combined |
| Classical Happy Fan | `favorite_genre: "classical"` vs `favorite_mood: "happy"` | Classical song (Autumn Sonata) | Pop/indie (Rooftop Lights) | When genre and mood never co-occur in the catalog, the higher-weighted attribute (mood +3.0 > genre +2.0) silently wins every time |
| Acoustic Raver | `favorite_genre: "edm"` + `target_energy: 0.9` vs `favorite_mood: "chill"` + `likes_acoustic: True` | High-energy EDM (Neon Apex) | Lofi/chill (Midnight Coding) | `likes_acoustic` and `favorite_mood` compound — both independently favor the same low-energy acoustic songs, overriding the numeric energy signal |

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tried to double the weight on the energy level to see what would happen but it didn't do anything to the top recommendation. Additionally, I tried adding tempo and valence to the scoring algorithm but it seem that the basic parameters that I first implemented outweigh the effects of tempo and valence. 

A summary of the what I tried (prior to add tempo, valence and dancibility to the score):

| Profile | Signals in conflict | Expected result | Actual result | Weakness exposed |
|---|---|---|---|---|
| Sad Banger | `favorite_mood: "sad"` vs `favorite_genre: "pop"` + `target_energy: 0.95` | Sad, slow song (Mississippi Low) | Energetic pop (Gym Hero) | Mood (+3.0) can be beaten by genre (+2.0) + strong energy proximity (~+2.0) combined |
| Classical Happy Fan | `favorite_genre: "classical"` vs `favorite_mood: "happy"` | Classical song (Autumn Sonata) | Pop/indie (Rooftop Lights) | When genre and mood never co-occur in the catalog, the higher-weighted attribute (mood +3.0 > genre +2.0) silently wins every time |
| Acoustic Raver | `favorite_genre: "edm"` + `target_energy: 0.9` vs `favorite_mood: "chill"` + `likes_acoustic: True` | High-energy EDM (Neon Apex) | Lofi/chill (Midnight Coding) | `likes_acoustic` and `favorite_mood` compound — both independently favor the same low-energy acoustic songs, overriding the numeric energy signal |

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

