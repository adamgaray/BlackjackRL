import numpy as np

CARDS = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,\
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

class BlackjackEnv():
    
    def __init__(self):
        
        self.shuffle_card = np.random.choice(range(30, 80))
        self.deck = self.make_deck()
        self.player_hand = []
        self.dealer_hand = []


    def play(self):
        self.deal()

        return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], 0, False


    def step(self, action):

        if action == 0:
            self.player_hand.append(self.draw())

            if self.eval_hand(self.player_hand) > 21:
                return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], -1, True

            else:
                return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], 0, False
       
        # if stood:
        while self.eval_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw())

        if self.eval_hand(self.dealer_hand) > 21:
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], 1, True
        
        if self.eval_hand(self.player_hand) > self.eval_hand(self.dealer_hand):
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], 1, True
        
        elif self.eval_hand(self.player_hand) < self.eval_hand(self.dealer_hand):
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], -1, True
        
        else:
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], 0, True


    def usable_ace(self, hand):
        count = 0
        for card in hand: 
            if card == 'A': count += 1
        
        val = sum(CARDS[card] for card in hand)
        while count > 0:
            val -= 10
            count -= 1

        return 'A' in hand and val <= 11

    def deal(self):

        self.player_hand = []
        self.dealer_hand = []

        if len(self.deck) < self.shuffle_card:
            self.deck = self.make_deck()

        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())

    def draw(self):
        drawn = np.random.choice(self.deck)
        self.deck.remove(drawn)
        return drawn
    
    def eval_hand(self, hand):
        val = sum(CARDS[card] for card in hand)
        num_aces = 0

        while val > 21 and 'A' in hand:
            num_aces += 1
            hand.remove('A')
            val -= 10
        
        for _ in range(num_aces):
            hand.append('A')

        return val

    def make_deck(self):
        deck = []

        for deck_num in range(3):
            for suit in range(4):
                for card in CARDS.keys():
                    deck.append(card)
        
        return deck
    
# b = BlackjackEnv()