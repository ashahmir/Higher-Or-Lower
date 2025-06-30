# Higher Lower Followers Game 🆚

A fun Python console game where you guess who has more Instagram followers!

## 🎮 How to Play

- Two random celebrities are shown.
- Each has their name, profession, and country revealed.
- You guess which one has **more followers** by typing `A` or `B`.
- If you're right, your score increases and the next round begins.
- If you're wrong, it's Game Over and your final score is displayed.

## 🛠️ Requirements

- Python 3.x

## 🧱 Project Structure

```
├── main.py          # The main game logic
├── art.py           # Contains ASCII art for logo and 'vs'
└── dataset.py       # Contains a list of dictionaries with celebrity data
```

## 📦 Example of `dataset.py`

```python
data = [
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 600,
        'description': 'footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 380,
        'description': 'musician and actress',
        'country': 'United States'
    },
    ...
]
```

## 🧠 Features

- Random selection of celebrities
- Score tracking across rounds
- Input validation (ends game on invalid input)
- Auto-clears console between rounds (via printing 100 newlines)

## 🚀 How to Run

Make sure you have all files (`main.py`, `art.py`, `dataset.py`) in the same folder.

Then run:
```bash
python main.py
```

## 📸 Example Output

```
Compare A: Cristiano Ronaldo, a footballer, from Portugal
vs
Against B: Ariana Grande, a musician and actress, from United States
Who has more followers? Type 'A' or 'B':
```

## 💡 Tip

Customize the dataset to add your favorite influencers, athletes, or public figures!

---

Created with ❤️ by ashahmir
