import eightgame as game



# while True:
#     try:
#         user_input = int(input("Enter a valid move"))
#     except ValueError:
#         print("Invalid Input try again")
#         continue

#  #   move = tuple(int(item) for item in user_input.split(" "))
#     move = game.position_of_number(gameBoard, user_input)

#     try:
#         updatedgameBoard = game.result(gameBoard, move)
#     except:
#         print("Invalid Move try again")
#         continue

#     game.display_board(updatedgameBoard)
#     if game.game_over(updatedgameBoard):
#         print("Game over")
#         break
#     else:
#         gameBoard = updatedgameBoard

#AI stuff start

class Node:
    def __init__(self, state,  parent, action, depth):
        self.parent = parent
        self.action = action
        self.state = state
        self.depth = depth

class StackFrontier:
    
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def remove(self):
        if self.empty():
            raise Exception("Removing from empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Removing from empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class PriorityFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Removing from empty frontier")
        else:
            minval = 100
            node = self.frontier[0]
            for new_node in self.frontier:
                if (game.hamming(new_node.state) + new_node.depth) < minval:
                    node = new_node
                    minval = game.hamming(new_node.state) + new_node.depth
            self.frontier.remove(node)
        return node

def solve_game(gameBoard):

    
    start = Node(gameBoard, None, None, 0)
    
    frontier = PriorityFrontier()
    frontier.add(start)

    states_explored = 0
    explored = list()

    while True:

        if frontier.empty():
            raise Exception ("No solution")
        
        node = frontier.remove()
        states_explored +=1

        if game.game_over(node.state):
            depth = node.depth
            actions = []
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent
            actions.reverse()
            return actions, depth
        
        explored.append(node)

        for action in game.possible_moves(node.state):
            newBoard = game.result(node.state,action)
            if not node.parent:
                newState = Node(newBoard, node, action, node.depth+1)
                frontier.add(newState)
            elif newBoard != node.parent.state:
                newState = Node(newBoard, node, action, node.depth+1)
                frontier.add(newState)


gameBoard = game.create_board([0, 1, 2, 3, 4, 5, 6, 7, 8])
game.display_board(gameBoard)

actions, depth = solve_game(gameBoard)
for action in actions:
    gameBoard = game.result(gameBoard, action)
    game.display_board(gameBoard)
print(f"Solution in depth: {depth}")
