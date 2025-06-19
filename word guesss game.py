import tkinter as tk
import random
import time
from tkinter import messagebox
import datetime

# Word-Clue pairs
WORD_CLUES = [
    ("WORDS", "🧩 A group of letters that carry meaning in language."),
    ("PLANT", "🌿 Something that grows in soil."),
    ("CHAIR", "🪑 You sit on it."),
    ("MOUSE", "🖱️ A computer accessory or a rodent."),
    ("LIGHT", "💡 You need it to see in the dark."),
    ("WATER", "💧 Clear liquid essential for life."),
    ("BRUSH", "🖌️ Used to paint or groom."),
    ("APPLE", "🍎 A red or green fruit, often associated with Newton."),
    ("CLOUD", "☁️ White and fluffy, floats in the sky."),
    ("STONE", "🪨 Hard and solid, found on the ground."),
    ("EARTH", "🌍 The planet we live on."),
    ("BRAIN", "🧠 Organ responsible for thinking."),
    ("PIZZA", "🍕 Italian food with cheese and toppings."),
    ("SUGAR", "🍬 Sweet substance used in desserts."),
    ("SHEET", "🛏️ A piece of cloth used on a bed."),
    ("CABLE", "🔌 Used to connect electronic devices."),
    ("SOUND", "🔊 What you hear."),
    ("PAPER", "📄 Used for writing or printing."),
    ("PLANE", "✈️ Flies in the sky."),
    ("CLEAN", "🧼 Opposite of dirty."),
    ("BLACK", "⚫ Opposite of white."),
    ("GREEN", "🌱 A color of leaves."),
    ("MONEY", "💰 Used to buy things."),
    ("CLOCK", "⏰ Tells you the time."),
    ("SMILE", "😊 Expression of happiness."),
    ("BREAD", "🍞 Common food made from flour."),
    ("HEART", "❤️ Pumps blood through your body."),
    ("BEACH", "🏖️ Sandy place near the ocean."),
    ("NOISE", "📢 Loud and unpleasant sound."),
    ("BLOOD", "🩸 Flows inside your body."),
    ("TIGER", "🐅 A big wild cat."),
    ("ROBOT", "🤖 A machine that can do tasks."),
    ("GRASS", "🌾 Covers the ground, green."),
    ("GLOVE", "🧤 You wear it on your hand."),
    ("TRAIN", "🚆 Moves on tracks, carries people."),
    ("HOUSE", "🏠 A place where people live."),
    ("ALARM", "🔔 It rings to wake you up."),
    ("FRUIT", "🍇 Edible and often sweet from trees or plants."),
    ("WHEEL", "🛞 A round object that helps things move."),
    ("SPOON", "🥄 Used to eat soup or cereal."),
    ("LUNCH", "🥪 Meal eaten around midday."),
    ("DANCE", "💃 Move rhythmically to music."),
    ("SLEEP", "😴 You do it at night."),
    ("ANGEL", "👼 A heavenly being with wings."),
    ("MANGO", "🥭 A tropical fruit, sweet and yellow inside."),
    ("ZEBRA", "🦓 Striped animal found in Africa."),
    ("FLAME", "🔥 A small, hot, glowing fire."),
    ("GHOST", "👻 Spirit often found in scary stories."),
    ("CANDY", "🍭 Sweet and sugary treat."),
    ("LEMON", "🍋 A sour yellow fruit."),
    ("FLOOD", "🌊 Overflowing water."),
    ("PEACH", "🍑 A juicy, fuzzy-skinned fruit."),
    ("NURSE", "💉 Cares for sick people."),
    ("SKATE", "⛸️ Glides on ice or concrete."),
    ("SNAKE", "🐍 A legless reptile."),
    ("SHIRT", "👕 A clothing item for the upper body."),
    ("BLANK", "⬜ Empty or unfilled."),
    ("MUSIC", "🎵 A pleasant sound or song."),
    ("RIVER", "🌊 A large natural flowing stream of water."),
    ("WOMAN", "👩 An adult female."),
    ("BIRTH", "👶 The act of being born."),
    ("CROWN", "👑 Worn by kings or queens."),
    ("FENCE", "🚧 Used to enclose an area."),
("STORM", "⛈️ Heavy rain with thunder."),
("BLADE", "🔪 Sharp edge for cutting."),
("DRINK", "🥤 Something you consume when thirsty."),
("CLOWN", "🤡 Funny performer with makeup."),
("JOKER", "🃏 A playing card or a prankster."),
("CANDY", "🍭 Sweet treat children love."),
("GRAPE", "🍇 A small purple or green fruit."),
("BERRY", "🍓 Small juicy fruit, often red or blue."),
("CYCLE", "🚴 Moves on two wheels."),
("FLOOR", "🪵 Surface you walk on indoors."),
("GRAIN", "🌾 Small edible seed."),
("CRANE", "🏗️ Tall machine for lifting."),
("SHEET", "🛏️ A piece of fabric for bedding."),
("PAINT", "🎨 Used to color walls or canvas."),
("SCARE", "😱 What horror movies do."),
("TIRED", "🥱 Feeling the need to sleep."),
("VIRUS", "🦠 Causes diseases."),
("EMAIL", "📧 Electronic message."),
("PLUGS", "🔌 Connects devices to power."),
("TIMER", "⏲️ Measures time duration."),
("FIELD", "🌾 Open land area."),
("TOWER", "🗼 Tall building or structure."),
("LEAFY", "🍃 Full of leaves."),
("SHEEP", "🐑 Wooly farm animal."),
("CRACK", "🪨 A split or break."),
("NIGHT", "🌃 Dark part of the day."),
("LAUGH", "😂 Expression of amusement."),
("ROCKS", "🪨 Solid mineral materials."),
("PLATE", "🍽️ Used to serve food."),
("CLOWN", "🤡 Wears makeup and performs."),
("SCOOP", "🍦 Tool for serving ice cream."),

]

# Colors
COLOR_CORRECT = "#6aaa64"
COLOR_PRESENT = "#c9b458"
COLOR_WRONG = "#787c7e"
COLOR_EMPTY = "#ddd"
WORD_LENGTH = 5

# Stats
score = 0
start_time = time.time()
used_words = []
streak = 0
longest_streak = 0
correct_attempts = 0
wrong_attempts = 0
hint_used = False
time_remaining = 30
dark_mode = False
leaderboard = []

# GUI Init
root = tk.Tk()
root.title("WORDLOOK - Clue Game")
root.configure(bg="white")

tk.Label(root, text="WORD GUESS GAME", font=("Helvetica", 32, "bold"), bg="white").pack(pady=10)
clue_label = tk.Label(root, text="", font=("Helvetica", 16, "italic"), bg="blue", fg="white", pady=10, padx=20)
clue_label.pack(fill="x")
timer_label = tk.Label(root, text="Time: 0s", font=("Helvetica", 12), bg="white", fg="gray")
timer_label.pack()
score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12), bg="white", fg="blue")
score_label.pack()
streak_label = tk.Label(root, text="🔥 Streak: 0 | 🏆 Longest: 0", font=("Helvetica", 12), bg="white", fg="orange")
streak_label.pack()
attempt_label = tk.Label(root, text="✅ 0 | ❌ 0", font=("Helvetica", 12), bg="white", fg="black")
attempt_label.pack()

# Game timer
def update_timer():
    elapsed = int(time.time() - start_time)
    timer_label.config(text=f"Time: {elapsed}s")
    root.after(1000, update_timer)
update_timer()

# Grid setup
grid_frame = tk.Frame(root, bg="white")
grid_frame.pack()
tiles = []
for col in range(WORD_LENGTH):
    lbl = tk.Label(grid_frame, text=" ", width=2, height=1,
                   font=("Helvetica", 18, "bold"), bg=COLOR_EMPTY, fg="black",
                   borderwidth=2, relief="solid", padx=5, pady=5)
    lbl.grid(row=0, column=col, padx=2, pady=2, ipadx=5, ipady=5)
    tiles.append(lbl)

# Entry
entry_frame = tk.Frame(root, bg="white")
entry_frame.pack(pady=10)
entry = tk.Entry(entry_frame, font=("Helvetica", 18), width=10, justify="center")
entry.pack(side="left", padx=5)
entry.focus()
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white")
result_label.pack(pady=5)

# Countdown
def countdown():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        result_label.config(text=f"⏳ {time_remaining}s left", fg="gray")
        root.after(1000, countdown)
    else:
        result_label.config(text=f"❌ Time up! Word was: {TARGET_WORD}", fg="red")
        update_streak(False)
        increment_attempt(False)
        messagebox.showinfo("⏰ Time's up!", f"The correct word was: {TARGET_WORD}")
        root.after(1000, load_next_word)

def update_streak(success):
    global streak, longest_streak
    if success:
        streak += 1
        longest_streak = max(streak, longest_streak)
    else:
        streak = 0
    streak_label.config(text=f"🔥 Streak: {streak} | 🏆 Longest: {longest_streak}")

def increment_attempt(success):
    global correct_attempts, wrong_attempts
    if success:
        correct_attempts += 1
    else:
        wrong_attempts += 1
    attempt_label.config(text=f"✅ {correct_attempts} | ❌ {wrong_attempts}")

def load_next_word():
    global TARGET_WORD, CLUE, hint_used, time_remaining
    if len(used_words) == len(WORD_CLUES):
        result_label.config(text="🏁 All words completed!", fg="blue")
        leaderboard.append((score, datetime.datetime.now().strftime("%H:%M:%S")))
        return
    while True:
        TARGET_WORD, CLUE = random.choice(WORD_CLUES)
        if TARGET_WORD not in used_words:
            used_words.append(TARGET_WORD)
            break
    clue_label.config(text=f"💡 {CLUE}")
    entry.delete(0, tk.END)
    result_label.config(text="")
    for tile in tiles:
        tile.config(text=" ", bg=COLOR_EMPTY, fg="black")
    hint_used = False
    time_remaining = 30
    countdown()

def check_word(event=None):
    global score, hint_used
    guess = entry.get().upper()
    if len(guess) != WORD_LENGTH or not guess.isalpha():
        result_label.config(text="⚠️ Enter a valid 5-letter word.", fg="red")
        return
    entry.delete(0, tk.END)
    target_chars = list(TARGET_WORD)
    used_indices = []
    for i in range(WORD_LENGTH):
        letter = guess[i]
        tiles[i].config(text=letter)
        if letter == TARGET_WORD[i]:
            tiles[i].config(bg=COLOR_CORRECT, fg="white")
            used_indices.append(i)
            target_chars[i] = None
    for i in range(WORD_LENGTH):
        letter = guess[i]
        if tiles[i].cget("bg") != COLOR_CORRECT:
            if letter in target_chars:
                idx = target_chars.index(letter)
                if idx not in used_indices:
                    tiles[i].config(bg=COLOR_PRESENT, fg="white")
                    used_indices.append(idx)
                    target_chars[idx] = None
                else:
                    tiles[i].config(bg=COLOR_WRONG, fg="white")
            else:
                tiles[i].config(bg=COLOR_WRONG, fg="white")
    if guess == TARGET_WORD:
        score += 10 if not hint_used else 5
        score_label.config(text=f"Score: {score}")
        result_label.config(text=random.choice(["🎉 Great!", "✅ Correct!", "🌟 Well done!"]), fg="green")
        update_streak(True)
        increment_attempt(True)
        root.after(1000, load_next_word)
    else:
        update_streak(False)
        increment_attempt(False)
        result_label.config(text="❌ Try again!", fg="red")

def give_hint(event=None):
    global hint_used
    if hint_used:
        result_label.config(text="💡 Hint already used.", fg="blue")
        return
    hint_letter = TARGET_WORD[random.randint(0, WORD_LENGTH - 1)]
    result_label.config(text=f"💡 Hint: The word contains '{hint_letter}'", fg="blue")
    hint_used = True

def restart_game():
    global score, used_words, streak, longest_streak, start_time, correct_attempts, wrong_attempts
    score = 0
    used_words.clear()
    streak = 0
    longest_streak = 0
    correct_attempts = 0
    wrong_attempts = 0
    score_label.config(text="Score: 0")
    streak_label.config(text="🔥 Streak: 0 | 🏆 Longest: 0")
    attempt_label.config(text="✅ 0 | ❌ 0")
    start_time = time.time()
    load_next_word()

def fill_correct_word(event=None):
    entry.delete(0, tk.END)
    entry.insert(0, TARGET_WORD)
    check_word()

def toggle_dark_mode(event=None):
    global dark_mode
    bg = "#1e1e1e" if not dark_mode else "white"
    fg = "white" if not dark_mode else "black"
    dark_mode = not dark_mode
    for widget in root.winfo_children():
        widget.config(bg=bg, fg=fg if hasattr(widget, "cget") and widget.cget("fg") != "blue" else "blue")

def show_leaderboard(event=None):
    if not leaderboard:
        messagebox.showinfo("Leaderboard", "No scores yet.")
    else:
        top = sorted(leaderboard, reverse=True)[:3]
        msg = "\n".join([f"{i+1}. Score: {s} at {t}" for i, (s, t) in enumerate(top)])
        messagebox.showinfo("🏆 Leaderboard", msg)

def show_definition(event=None):
    messagebox.showinfo("🧠 Definition", f"{TARGET_WORD.title()}: {CLUE}")

# Buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)
tk.Button(button_frame, text="Submit", font=("Helvetica", 14), command=check_word).pack(side="left", padx=5)
tk.Button(button_frame, text="Hint 💡", font=("Helvetica", 14), command=give_hint).pack(side="left", padx=5)
tk.Button(button_frame, text="Auto Fill 🧠", font=("Helvetica", 14), command=fill_correct_word).pack(side="left", padx=5)
tk.Button(button_frame, text="🔁 Restart", font=("Helvetica", 14), command=restart_game).pack(side="left", padx=5)
tk.Button(button_frame, text="📖 Define", font=("Helvetica", 14), command=show_definition).pack(side="left", padx=5)

entry.bind("<Return>", check_word)
root.bind("h", give_hint)
root.bind("c", fill_correct_word)
root.bind("l", show_leaderboard)
root.bind("d", toggle_dark_mode)
root.bind("w", show_definition)

load_next_word()
root.mainloop()
