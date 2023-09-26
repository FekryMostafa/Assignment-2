from random import choices

# Task 1:

states = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
terminal_state = 'J'
initial_state = 'A'
treasure_states = ['B', 'D', 'H']

actions = ['move', 'dig']

gamma = 0.9

trans_prob = {
    'A': {'A': 0.2, 'B': 0.8},
    'B': {'B': 0.2, 'C': 0.8},
    'C': {'C': 0.2, 'D': 0.8},
    'D': {'D': 0.2, 'E': 0.8},
    'E': {'E': 0.2, 'F': 0.8},
    'F': {'F': 0.2, 'G': 0.8},
    'G': {'G': 0.2, 'H': 0.8},
    'H': {'H': 0.2, 'I': 0.8},
    'I': {'I': 0.2, 'J': 0.8},
    'J': {'J': 1}
}

def get_reward(state, action, treasures_found):
    if state == terminal_state:
        return 15 if treasures_found == len(treasure_states) else 5
    if action == 'dig' and state in treasure_states:
        return 2
    if action == 'move':
        return -1
    return 0

# Task 2:

class Agent:
    def __init__(self):
        self.state = initial_state
        self.treasures_found = 0
        self.total_reward = 0
        self.gamma = gamma
        self.history = []
        
    def policy(self):
        return choices(actions, [0.9, 0.1])[0]
    
    def step(self):
        action = self.policy()
        #print(f"Current State: {self.state}, Action: {action}")  # Print the current state and action

        if action == 'move':
            self.state = choices(list(trans_prob[self.state].keys()), list(trans_prob[self.state].values()))[0]
        
        reward = get_reward(self.state, action, self.treasures_found)
        self.total_reward += reward * (self.gamma ** len(self.history))
        #print(f"Reward Received: {reward}, Total Reward: {self.total_reward}")  # Print reward information

        if action == 'dig' and self.state in treasure_states:
            self.treasures_found += 1

        self.history.append((self.state, action, reward))
        return self.state, action, reward

# Task 3:

def run_episode(agent, max_steps=25):
    #print("Starting New Episode...")  # Print episode start
    
    agent.__init__()
    for step in range(max_steps):
        state, action, reward = agent.step()
        if state == terminal_state:
            #print("Terminal State Reached!")
            break

    print("Agent's History: ", agent.history)
    print(f"Cumulative Reward for Episode: {agent.total_reward}")
    #print("Episode Ended.")  # Print episode end
    return agent.history, agent.total_reward

agent = Agent()
all_episode_histories = []
all_episode_rewards = []

for episode in range(1, 11):
    print(f"=== Episode {episode} ===")
    episode_history, episode_reward = run_episode(agent)
    all_episode_histories.append(episode_history)
    all_episode_rewards.append(episode_reward)

all_episode_histories, all_episode_rewards
