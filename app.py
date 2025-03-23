from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

def get_destiny_card(birthdate):
    destiny_cards = [
        "Ace of Hearts", "Two of Hearts", "Three of Hearts", "Four of Hearts", "Five of Hearts", "Six of Hearts", "Seven of Hearts", "Eight of Hearts", "Nine of Hearts", "Ten of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts",
        "Ace of Diamonds", "Two of Diamonds", "Three of Diamonds", "Four of Diamonds", "Five of Diamonds", "Six of Diamonds", "Seven of Diamonds", "Eight of Diamonds", "Nine of Diamonds", "Ten of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",
        "Ace of Clubs", "Two of Clubs", "Three of Clubs", "Four of Clubs", "Five of Clubs", "Six of Clubs", "Seven of Clubs", "Eight of Clubs", "Nine of Clubs", "Ten of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs",
        "Ace of Spades", "Two of Spades", "Three of Spades", "Four of Spades", "Five of Spades", "Six of Spades", "Seven of Spades", "Eight of Spades", "Nine of Spades", "Ten of Spades", "Jack of Spades", "Queen of Spades", "King of Spades"
    ]
    index = sum(map(int, birthdate.replace("/", ""))) % 52
    return destiny_cards[index]

def oracle_ai(question_category):
    responses = {
        "Love": [
            "Your heart seeks clarity—trust your intuition, it knows the way.",
            "Love is a mirror; what you seek is already within you.",
            "A new connection will bring warmth and understanding into your life."
        ],
        "Career": [
            "The path ahead holds unexpected opportunities—stay open.",
            "Your purpose is unfolding—take the next step with confidence.",
            "A shift in perspective will bring the clarity you need for success."
        ],
        "Spiritual Growth": [
            "The universe speaks in whispers—listen closely to your inner wisdom.",
            "Your energy is shifting—embrace the transformation ahead.",
            "Synchronicities will guide you—trust the signs."
        ],
        "Personal Insight": [
            "You are more powerful than you realize—own your truth.",
            "A revelation will soon bring clarity—stay patient.",
            "Release old patterns to invite new blessings into your life."
        ],
        "Life Path": [
            "Your journey is unique—embrace each twist and turn with confidence.",
            "A crossroads approaches—trust your soul’s wisdom to guide you.",
            "Destiny unfolds in unexpected ways—stay present and aware."
        ],
        "Health": [
            "Your body is your temple—nurture it with love and care.",
            "Healing comes when you align mind, body, and spirit.",
            "Listen to your body—it whispers what your soul already knows."
        ],
        "Past Life": [
            "Glimpses of past lives reveal wisdom for your current journey.",
            "An old soul connection is resurfacing—be mindful of its lessons.",
            "Your past experiences shape your present—honor their influence."
        ],
        "Relationship Compatibility": [
            "The energy between you two is shifting—trust the flow.",
            "Your connection holds karmic ties—reflect on its purpose.",
            "Open communication will strengthen your bond and clear confusion."
        ]
    }
    return random.choice(responses.get(question_category, ["The Oracle senses uncertainty—please select a valid category."]))

@app.route('/', methods=['GET', 'POST'])
def index():
    reading = None
    destiny_card = None
    if request.method == 'POST':
        birthdate = request.form['birthdate']
        reading_type = request.form['reading_type']
        try:
            datetime.strptime(birthdate, "%Y-%m-%d")
            destiny_card = get_destiny_card(birthdate.replace("-", "/"))
            reading = oracle_ai(reading_type)
        except ValueError:
            reading = "Invalid birthdate format. Please use MM/DD/YYYY."
    return render_template('index.html', destiny_card=destiny_card, reading=reading)
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


