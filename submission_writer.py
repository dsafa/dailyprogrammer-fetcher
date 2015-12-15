import os
import challenge


def write_challenge(c):
    fileName = get_filename(c)
    fileContents = get_fileContents(c)

    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, "w", encoding="utf-8") as file:
        file.write(fileContents)
        file.close()


def get_fileContents(c):
    fileContents = "%s\n%s\n\n%s" % (c.url, c.fullTitle, c.contents)

    return fileContents


def get_filename(c):
    diff = ""
    if (c.difficulty == challenge.ChallengeDifficulty.HARD):
        diff = "Hard"
    elif (c.difficulty == challenge.ChallengeDifficulty.INTERMEDIATE):
        diff = "Intermediate"
    else:
        diff = "Easy"

    fileName = "%s/%s/%s Challenge.txt" % (diff, c.challengeNum, c.date)

    return fileName