import numpy as np

CARDS = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,\
        '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

class Blackjack():
    
    def __init__(self):
        
        self.shuffle_card = np.random.choice(range(30, 80))
        self.actions = 2
        self.deck = self.make_deck()
        self.player_hand = []
        self.dealer_hand = []


    def play(self):
        self.deal()
        print('Your Hand: ', self.player_hand)
        print('Dealer Hand: ', [self.dealer_hand[0], '?'])


        while self.eval_hand(self.player_hand) <= 21:
            action = input('Enter 0 to hit, 1 to stand \n')
            if action == '1':
                print('YOU STAND:')
                break
            
            self.player_hand.append(self.draw())
            
            print('YOU HIT:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', [self.dealer_hand[0],'?'])
        

        if self.eval_hand(self.player_hand) > 21:
            print('YOU WENT BUST:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', self.dealer_hand)
            self.player_hand = []
            self.dealer_hand = []
            return -1
        

        print('Your Hand: ', self.player_hand)
        print('Dealer Hand: ', self.dealer_hand)
        while self.eval_hand(self.dealer_hand) < 17:
            print('DEALER DRAWS:')
            self.dealer_hand.append(self.draw())
            print('Dealer Hand: ', self.dealer_hand)

        if self.eval_hand(self.dealer_hand) > 21:
            print('DEALER WENT BUST:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', self.dealer_hand)
            self.player_hand = []
            self.dealer_hand = []
            return 1
        
        if self.eval_hand(self.player_hand) > self.eval_hand(self.dealer_hand):
            print('YOU WON:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', self.dealer_hand)
            self.player_hand = []
            self.dealer_hand = []
            return 1
        
        elif self.eval_hand(self.player_hand) < self.eval_hand(self.dealer_hand):
            print('YOU LOST:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', self.dealer_hand)
            self.player_hand = []
            self.dealer_hand = []
            return -1
        
        else:
            print('YOU TIED:')
            print('Your Hand: ', self.player_hand)
            print('Dealer Hand: ', self.dealer_hand)
            self.player_hand = []
            self.dealer_hand = []
            return 0


    def deal(self):
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
    


Blackjack().play()