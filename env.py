

class SingleDeterministic():
    def __init__(self, init_state=[0, 1], fixed_policy=0):
        self.current_state = init_state
        self.init_state = init_state
        self.fixed_policy = fixed_policy
        self.obs = {"[0, 0]": [0], "[0, 1]": [1], "[1, 0]": [2], "[1, 1]": [3]}
        print(f"Starting at state {self.current_state}, fixed second agent with policy {self.fixed_policy}")
        if self.fixed_policy == 0:
            self.s_agent_action = 0
        if self.fixed_policy == 1:
            self.s_agent_action = 1

    def step(self, action):
        if action == 0:
            self.current_state = [0, self.s_agent_action]
        if action == 1:
            self.current_state = [1, self.s_agent_action]
        return self.obs[str(self.current_state)]

    def reset(self):
        self.current_state = self.init_state
        self.fixed_policy = self.fixed_policy
        print("Environment reset")
        return self.obs[str(self.current_state)]