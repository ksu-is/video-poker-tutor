from flask import Flask
from flask import request
from flask import render_template
from card import Card
from score import score_hand
from analyze import analyze_hand

app = Flask(__name__)

@app.route('/')
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
