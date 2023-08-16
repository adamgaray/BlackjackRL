# BlackjackRL

Explores the effectiveness of three prominent reinforcement learning algorithms - Q-learning, SARSA, and DQN - in learning optimal strategies for blackjack. The performance of these algorithms is evaluated through simulations and experiments, offering insights into the application of reinforcement learning techniques for tackling intricate decision-making challenges.

## Blackjack Environments

Custom blackjack environments allow agents to interact with the game and learn strategies through reinforcement learning.

### BlackjackEnv

A basic blackjack environment is introduced, encompassing three state values (player score, dealer card, and usable ace) and two actions (hit or stand).

### BlackjackCountEnv

An extended environment incorporates card counting techniques used by skilled players. This environment keeps track of the number of aces and tens remaining in the deck, emulating a card counting strategy.

### BlackjackMoreEnv

A more advanced environment introduces actions such as splitting and doubling, increasing complexity and more closely mirroring actions available to real players.

## Algorithms

Three reinforcement learning algorithms are implements for learning optimal blackjack strategy.

### Q-Learning

Q-learning is an off-policy algorithm approximating the optimal action-value function by iteratively updating state-action pairs' Q-values using the Bellman equation.

### SARSA

SARSA is an on-policy algorithm approximating the optimal action-value function by updating Q-values based on observed rewards, next state, and action. An epsilon-greedy exploration strategy is employed.

### DQN

Deep Q-Network (DQN) is an off-policy algorithm utilizing deep neural networks. DQN extends Q-learning and handles high-dimensional state spaces. Experience replay and a target network stabilize the learning process.

<br><br>

Originally written for COMP 579 (Winter 2023) at McGill University.
