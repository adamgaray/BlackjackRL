import numpy as np

CARDS = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,\
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

# ACTIONS: 0 hit, 1 stand, 2 double, 3 split
class BlackjackMoreEnv():
    
    def __init__(self):
        
        self.shuffle_card = np.random.choice(range(30, 80))
        self.deck = self.make_deck()
        self.player_hand = []
        self.split_hand = []
        self.dealer_hand = []


    def play(self):
        self.deal()

        can_split = True if self.player_hand[0] == self.player_hand[1] else False

        # state, reward, can_split, over
        return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                0, can_split, False


    def step(self, action):
    # state, reward, split_still_to_play, over

        # if split:
        if action == 3:
            self.split_hand.append(self.player_hand.pop())
            self.player_hand.append(self.draw())
            self.split_hand.append(self.draw())
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                  0, True, False

        split = len(self.split_hand) != 0

        # if hit:
        if action == 0:
            self.player_hand.append(self.draw())

            if self.eval_hand(self.player_hand) > 21:
                return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                      -1, split, True

            else:
                return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                      0, split, False
       
       
        reward = 1

        # double
        if action == 2:
            self.player_hand.append(self.draw())
            reward = 2
            if self.eval_hand(self.player_hand) > 21:
                if split: 
                    self.player_hand = self.split_hand
                    self.split_hand = []
                return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                      -2, split, True


        # if stood:
        while self.eval_hand(self.dealer_hand) < 17:
            self.dealer_hand.append(self.draw())

        if self.eval_hand(self.dealer_hand) > 21:
            if split: 
                    self.player_hand = self.split_hand
                    self.split_hand = []
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                  reward, split, True
        
        if self.eval_hand(self.player_hand) > self.eval_hand(self.dealer_hand):
            if split: 
                    self.player_hand = self.split_hand
                    self.split_hand = []
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                  reward, split, True
        
        elif self.eval_hand(self.player_hand) < self.eval_hand(self.dealer_hand):
            if split: 
                    self.player_hand = self.split_hand
                    self.split_hand = []
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                  -1*reward, split, True
        
        else:
            if split: 
                    self.player_hand = self.split_hand
                    self.split_hand = []
            return [self.eval_hand(self.player_hand), CARDS[self.dealer_hand[0]], self.usable_ace(self.player_hand)], \
                  0, split, True


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
        self.split_hand = []

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