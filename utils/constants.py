import random

NUM_EPISODES = 5
MAX_STEPS_PER_EPISODE = 100
LEARNING_RATE = 0.1  # a parameter
DISCOUNT_RATE = 0.99  # gamma parameter

EXPLORATION_RATE = 1
MAX_EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = 0
EXPLORATION_DECAY_RATE = 0.01


A_REWARD = random.randint(0, 100)
B_REWARD = random.randint(0, 100)

C_REWARD = random.randint(-100, min(A_REWARD, B_REWARD))
D_REWARD = random.randint(-100, min(A_REWARD, B_REWARD))