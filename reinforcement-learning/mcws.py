import numpy as np

class Node():

    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.id = state.id
        self.children = []
        self.action = action

        self.visits = 0
        self.exp_reward = 0
        self.actual_reward = 0
        self.action_probabilities = []

    def is_leaf(self):
        if len(self.children) > 0:
            return False
        else:
            return True
        

class MCWS():

    def __init__(self, root, cpuct):
        self.root = root
        self.tree = {}
        self.cpuct = cpuct
        self.add_node(root)

    def add_node(self, node):
        self.tree[node.id] = node