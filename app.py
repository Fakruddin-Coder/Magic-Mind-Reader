from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'magicmindkey'

# Card setup
SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
DECK = [f"{r}of{s}" for s in SUITS for r in RANKS]

# Helper to map card names to image codes (e.g. "10ofhearts" -> "0H")
@app.context_processor
def util():
    def img(c):
        r, s = c.split('of')
        suit = {'hearts': 'H', 'diamonds': 'D', 'clubs': 'C', 'spades': 'S'}
        return f"{r[0].upper() if r != '10' else '0'}{suit[s]}"
    return dict(card_image=img)

# Routes
@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/start')
def start():
    deck = random.sample(DECK, 21)  # Pick 21 random cards
    session['deck'] = deck
    session['round'] = 0
    return show(deck)

@app.route('/choose', methods=['POST'])
def pick():
    col = int(request.form['column'])  # chosen column (1,2,3)
    deck = session['deck']
    cols = [deck[i::3] for i in range(3)]  # split into 3 columns

    # Always put chosen column in the middle
    if col == 1:
        new = cols[1] + cols[0] + cols[2]
    elif col == 2:
        new = cols[0] + cols[1] + cols[2]
    else:
        new = cols[0] + cols[2] + cols[1]

    session['deck'] = new
    session['round'] += 1

    if session['round'] == 3:
        return render_template('result.html', card=new[10])  # middle card is the chosen one
    return show(new)

# Helper to display cards in 3 columns
def show(deck):
    cols = [deck[i::3] for i in range(3)]
    return render_template('game.html', columns=cols)


