
import random
from datetime import datetime, timezone

quotes = [
    "First, solve the problem. Then, write the code. — John Johnson",
    "Talk is cheap. Show me the code. — Linus Torvalds",
    "Code is like humor. When you have to explain it, it's bad. — Cory House",
    "The only way to learn a new programming language is by writing programs in it. — Dennis Ritchie",
    "Clean code always looks like it was written by someone who cares. — Robert C. Martin",
    "Simplicity is the soul of efficiency. — Austin Freeman",
    "Programming isn't about what you know; it's about what you can figure out. — Chris Pine",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. — Martin Fowler",
    "Code never lies, comments sometimes do. — Ron Jeffries",
    "The best error message is the one that never shows up. — Thomas Fuchs",
    "Today's code is tomorrow's innovation!",
    "The most important property of a program is whether it accomplishes the intention of its user. — C. A. R. Hoare",
]

motivations = [
    "Keep coding, keep growing! 🚀",
    "Every line of code brings you closer to mastery! 💪",
    "Stay curious, stay coding! 🎯",
    "Building the future, one commit at a time! 🔥",
    "Consistency is the key to success! 🌟",
    "Debug today, deploy tomorrow! 💻",
    "Learn something new every day! 📚",
]

now = datetime.now(timezone.utc)
quote = random.choice(quotes)
motivation = random.choice(motivations)
day_of_year = now.timetuple().tm_yday

content = f"""# 📅 Daily Coding Update — {now:%B %d, %Y}

---

## 💡 Quote of the Day

> {quote}

---

## 🔥 Daily Motivation

**{motivation}**

---

## 📊 Quick Stats

| Metric | Value |
|---|---|
| 📆 Day of Year | {day_of_year} |
| 📅 Date | {now:%Y-%m-%d} |
| ⏰ Time | {now:%H:%M:%S} UTC |
| 🎯 Coding Streak | Keep it going! |

---

## 🎯 Today's Challenge

- [ ] Solve one DSA problem.
- [ ] Write at least 50 lines of meaningful code.
- [ ] Review and improve old code.
- [ ] Learn one new concept.
- [ ] Push your progress to GitHub.

---

## 🌟 Fun Fact

The first widely known computer bug was a moth found trapped in a Harvard Mark II computer in 1947.

---

*Automatically generated using Python and GitHub Actions.*

⭐ Keep pushing! Your consistency is your superpower!
"""

with open("DAILY.md", "w", encoding="utf-8") as file:
    file.write(content)

print(f"Daily update generated: {now:%Y-%m-%d}")
