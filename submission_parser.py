import re
import challenge


def parse_submission(submission):
    try:
        challengeDate, challengeNum, challengeDifficulty, challengeDesciption = parse_submission_title(submission.title)
        challengeContents = parse_submission_contents(submission)
        challengeURL = submission.url
        return challenge.Challenge(submission.title, challengeDate, challengeNum, challengeDifficulty, challengeDesciption, challengeContents, challengeURL)
    except ValueError:
        return None


def parse_submission_contents(submission):
    return submission.selftext


def parse_submission_title(title):
    #typical format: [yyyy-mm-dd] Challenge # <num> [<difficulty>] <description>
    SUBMISSON_REGEX = "\[(.+)\]\s*Challenge\s*#\s*(\d+)\s*\[(\w+)\](.*)"

    #older format: [date] challenge #<num> [difficulty]
    ALT_SUBMISSON_REGEX = "\[(.+)\] [Cc]hallenge #(\d+)\s\[(\w+)\].*"

    #first format: [<difficulty>] challenge #<num>
    OLD_SUBMISSON_REGEX = "\[(.+)\] challenge #(\d+).*"

    match = re.search(SUBMISSON_REGEX, title, 0)
    if match != None:
        return (replace_date(match.group(1)), match.group(2), match.group(3), match.group(4))

    altMatch = re.search(ALT_SUBMISSON_REGEX, title, 0)
    if (altMatch != None):
        return (replace_date(altMatch.group(1)), altMatch.group(2), altMatch.group(3), "")

    oldMatch = re.search(OLD_SUBMISSON_REGEX, title, 0)
    if oldMatch != None:
        return ("", oldMatch.group(2), oldMatch.group(1), "")

    raise ValueError("Unknown Title Format: " + title)

# replace "/" with "-" to prevent confusion with filepaths
def replace_date(date):
    return date.replace("/", "-")