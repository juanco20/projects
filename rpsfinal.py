import random

#Parent class always plays rock
class Player:
    moves = ['rock', 'paper', 'scissors']
    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

#class were the player moves randomly between rock paper and scissors
class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)

#class that remembers what move the opponent played last round, and plays that move this round.
class ReflectPlayer(Player):
    def move(self):
        return self.their_move

#class that remembers what move it played last round, and cycles through the different moves
class CyclePlayer(Player):
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        if self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]
        

class HumanPlayer(Player):
    def move(self):
        while True:
            pickone = input("Pick one: Rock, paper or scissors? ")
            if pickone.lower()in self.moves:
                return pickone.lower()
            else:
                print('Please select a valid move!')           


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        if beats(move1, move2):
            self.p1.score +=1
            winner = 'You Win!'

        elif move1 == move2:
            self.p1.score = self.p2.score
            self.p2.score = self.p2.score
            winner = 'its a Tie!'

        else:
           self.p2.score +=1
           winner = 'Computer Wins!' 
        
        print(f"You: {move1}"
            f"\nComputer: {move2}"
            f"\n{winner}"
            f"\nScore: You ({self.p1.score})"
            f"\nScore: Computer ({self.p2.score})")
            
        
        
    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        print("Game over!")
        if self.p1.score > self.p2.score:
            print("You  Won!") 
        elif self.p2.score > self.p1.score:
            print("Computer Won!")
        else:
            print("Its a tie!") 

        
    


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice([CyclePlayer(), ReflectPlayer(), RandomPlayer()]))
    game.play_game()
