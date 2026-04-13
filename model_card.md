# Model Card: Music Recommender Simulation

## 1. Model Name  

SpottyFind 

---

## 2. Intended Use  

SpottyFind recommends songs that match a user's music preferences.  
It is designed for classroom exploration of how recommendation algorithms work.  
It assumes the user can describe their taste using genre, mood, energy level, and similar attributes.  
It is not intended for real music streaming services or production use.

---

## 3. How the Model Works  

Every song in the catalog gets a score based on how well it matches the user's preferences.  
If a song's genre matches the user's favorite genre, it earns 2 bonus points.  
If a song's mood matches the user's favorite mood, it earns 3 bonus points.  
For numeric features — energy, acousticness, valence, danceability, and tempo — the closer the song's value is to the user's target, the more points it earns.  
All the points are added together. The five highest-scoring songs are returned as recommendations.

---

## 4. Data  

The catalog contains 17 songs.  
Songs span 13 genres: pop, lofi, rock, ambient, jazz, synthwave, indie pop, hip-hop, r&b, country, metal, edm, folk, blues, and classical.  
Each song has 7 attributes: genre, mood, energy, tempo (BPM), valence, danceability, and acousticness.  
The dataset is very small. Most genres are represented by only one song.  
The catalog skews toward high-energy tracks, so low-energy listeners have fewer close matches.  
Moods like "focused," "nostalgic," and "peaceful" each appear only once.

---

## 5. Strengths  

The system works reasonably well for users who prefer high-energy music, since most songs lean energetic.  
Genre and mood bonuses make the scoring easy to understand and explain.  
Every score is fully transparent — each point can be traced back to a specific preference match.  
Users with common preferences (pop, happy, high energy) tend to get intuitive results.

---

## 6. Limitations and Bias 

Energy is the most influential feature. A jazz fan who prefers high energy will likely receive EDM before jazz.  
Acousticness is treated as a yes/no preference, which erases nuance for users who fall somewhere in between.  
Mood matching is all-or-nothing. There is no credit for similar moods like "chill" and "relaxed."  
The small catalog means some genres and moods have no close matches at all.  
Low-energy listeners are structurally disadvantaged because the catalog has fewer low-energy songs.  
Rare moods like "nostalgic" or "peaceful" are nearly impossible to satisfy with only one matching song.

---

## 7. Evaluation  

Three adversarial user profiles were tested: the Sad Banger, the Classical Happy Fan, and the Acoustic Raver.  
Each profile was designed to create a conflict between preferences (e.g., high energy but acoustic).  
The top recommendations rarely changed even after making significant changes to the scoring weights.  
This showed that certain feature combinations dominate the score regardless of how the weights shift.  
It also showed that no single set of weights works well for every type of user.

---

## 8. Future Work  

Add per-user weight tuning so that energy does not always dominate over genre or mood.  
Use soft mood similarity so that adjacent moods (e.g., "chill" and "relaxed") can earn partial credit.  
Expand the catalog to include more songs per genre and mood so rare preferences can actually be satisfied.
Add some penalties for recommending too many similar songs.

---

## 9. Personal Reflection  

This allow me to put into perspective how hard music recommendations algorithm is to write. I like to bash on Spotify and YouTube Music for having iffy music recommender. But compared to mine, they're magnitude ahead through better algorithm and a significantly bigger catalog. Adjancently, I find the YouTube videos recommendation system to be really good, which shows how much works (and user datas) that Google has put into the YouTube algorithm.

Certainly, if a user were to have music preferences that matches most of the music in the dataset, this simple algorithm can still recommend song very well. It is like finding a linear line of best fit but in more then two dimensions.

I was able to use AI to explain to me at a basic level how a music recommendation system works. It also made connection with each topic and how it correlate to the functions provided in the base project. This allowed me to get a quick understanding of the materials and start designing the logic and coding. I found that for simple project like these, I can pretty easily check the AI work by looking at the logic flow. I don't think I can verify an AI works in a large project though.

A list of future improvement is listed above in section 8.