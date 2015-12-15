from enum import Enum


class ChallengeDifficulty(Enum):
    HARD = 1
    INTERMEDIATE = 2
    EASY = 3


class Challenge:
    def __init__(self, fullTitle, date, challengeNum, difficulty, title, contents, url):
        self.fullTitle = fullTitle
        self.date = date
        self.challengeNum = challengeNum
        self.difficulty = self.get_difficulty(difficulty)
        self.title = title
        self.contents = contents
        self.url = url

    def get_difficulty(self, difficulty):
        val = difficulty.lower()
        if (val == "hard" or val == "difficult"):
            return ChallengeDifficulty.HARD
        elif (val == "intermediate"):
            return ChallengeDifficulty.INTERMEDIATE
        else:
            return ChallengeDifficulty.EASY

    def to_string(self):
        return str(self.difficulty.value) + " " + self.date + " " + self.challengeNum + " " + self.title + "\nContents: " + self.contents