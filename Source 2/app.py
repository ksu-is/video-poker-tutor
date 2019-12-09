from flask import Flask
from flask import request
from flask import render_template
from card import Card
from score import score_hand
from analyze import analyze_hand

from deck import Deck
from hand import Hand

app = Flask(__name__)

@app.route('/pick_hand')
def pick_hand():
    rank_dict = {
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'T',
        11:'J',
        12:'Q',
        13:'K',
        14:'A',
    }

    suits = ['C', 'D', 'H', 'S']
    ranks = [rank_dict[num] for num in range(2,15)]

    context = {
        'suits':suits,
        'ranks':ranks,
    }
    return render_template('pick_hand.html', **context)

@app.route('/analyze/<hand_string>')
def analyze(hand_string):
    cards = hand_string.split('-')
    card_list = [Card(item) for item in cards]
    score = score_hand(card_list)
    ev_list = analyze_hand(card_list)
    # get the list of cards for the highest rated play in the expected value list
    hand_to_hold = ev_list[0][0]
    hold_cards = [str(card) for card in hand_to_hold]

    plays_context = [get_play_string(row[0]) for row in ev_list]
    ev_context = [row[1] for row in ev_list]

    if score != "Not a Winning Hand":
        winning_hand = True
    else:
        winning_hand = False

    context = {'cards':cards, 'score':score, 'hold_cards':hold_cards, 'winning_hand':winning_hand, \
            'plays':plays_context, 'ev':ev_context}
    return render_template('analyze.html', **context)
@app.route('/')
def home():
    return render_template('home.html')



#game variables

game_deck = Deck()
game_hand = Hand()
#edit later
cards = []
card_list = [Card(item) for item in cards]
ev_list = 0
plays_context = {}
ev_context = {}

def start_round():
        global game_deck
        global game_hand
        global cards
        global card_list
        global ev_list
        global plays_context
        global ev_context
        
        game_deck = Deck()
        game_hand = Hand()
        for i in range(0,5):
            game_hand.add_card(game_deck.draw_card())
        print(game_hand)
        cards = str(game_hand).split('  ')
        cards.pop() #To prevent errors
        card_list = [Card(item) for item in cards]
        ev_list = analyze_hand(card_list)
        plays_context = [get_play_string(row[0]) for row in ev_list]
        ev_context = [row[1] for row in ev_list]
        return False
#end edit

@app.route('/game')
def game():
    
    start_round()
    print("Export Cards\t", cards)
    context = {'cards':cards, 'plays':plays_context, 'ev':ev_context}
    return render_template('game.html', **context)
#end edit

def get_play_string(input_list):
    output_string = ''

    if len(input_list) == 0:
        return "None"
    else:
        for item in input_list:
            output_string = output_string + item + ' '

    return output_string

if __name__ == "__main__":
    app.run(debug=True)
