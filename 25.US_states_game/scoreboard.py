
class Scoreboard:
    def __init__(self, file = "track_score.txt"):
        self.right_answers = []
        with open(file,"r") as file:
            for state in file.readlines():
                self.right_answers.append(state.split('\n')[0])
        self.score = self.count()

    def add_state(self,new_state):
        self.right_answers.append(new_state)
        self.score = self.count()

    def save_file(self):
        with open("track_score.txt","w") as file:
            for state in self.right_answers:
                file.write(f"{str(state)}\n")

    def count(self):
        return len(self.right_answers)
