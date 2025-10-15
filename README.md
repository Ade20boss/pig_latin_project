# 🐷✨ Pig Latin Translator  

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> 🧠 A simple yet smart Python program that converts English text into **Pig Latin** while handling **numbers**, **punctuation**, and **capitalization** — all with zero external dependencies!

---

## 🚀 Features  

✅ Handles **normal English words** → `hello → ellohay`  
✅ Preserves **punctuation** → `hello! → ellohay!`  
✅ Works with **numbers inside words** → `123test123 → 123esttay123`  
✅ Supports **vowel-starting words** → `apple → appleyay`  
✅ Keeps **capitalization intact** → `Dog → Ogday`  
✅ Detects **empty input** and returns a friendly message  

---

## 🧠 How It Works  

Pig Latin is a playful transformation of English based on the following rules:  

1️⃣ If a word begins with a **vowel (a, e, i, o, u)**  
→ Add `"yay"` to the end.  
> Example: `apple → appleyay`  

2️⃣ If a word begins with a **consonant**  
→ Move the first letter to the end and add `"ay"`.  
> Example: `banana → ananabay`  

3️⃣ If a word contains **numbers**, the numbers stay in place.  
> Example: `123test123 → 123esttay123`  

4️⃣ Punctuation marks stay at the **end of words**.  
> Example: `world! → orldway!`  

---

## 🧩 Example Usage  

```bash
$ python pig_latin.py
Enter the English message to translate to Pig latin: Hello world!
Ellohay orldway!
```
---

🗂️ Project Structure
```
pig-latin-translator/
├── pig_latin.py       # Main program file
└── README.md          # Project documentation
```
---

⚙️ Requirements
> 🐍 Python 3.7 or higher
> No external libraries — built entirely with the standard library 💪
---
🏗️ How to Run

1️⃣ Clone the repository
```
git clone https://github.com/Ade20boss/pig_latin_project
```

2️⃣ Move into the directory
```
cd pig_latin_project
```

3️⃣ Run the program
```
python pig_latin_program.py
```

---
👨‍💻 Author
Daniel Adeoluwa Ademoye
👨‍💻Software Engineer and Ethical Hacker
🌐[LinkedIn](www.linkedin.com/in/daniel-ademoye-a05a56305) • [GitHub](https://github.com/Ade20boss) • [Threads](https://www.threads.com/@danieladeoluwaademoye)

---
📜License
This project is licensed under the **MIT License** - you're free to use, modify and share
| Made with 💖 Daniel Adeoluwa Ademoye




