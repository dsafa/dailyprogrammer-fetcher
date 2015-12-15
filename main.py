import time
import praw
import submission_parser
import submission_writer
import fetch_settings


def main():
    fetch_challenges()


def fetch_challenges():
    userAgent = "daily_programmer_fetcher"
    p = praw.Reddit(userAgent)
    subreddit = p.get_subreddit("dailyprogrammer", fetch=True)

    #get posts after the last time they were fetched
    try:
        startDate = fetch_settings.read_last_date()
    except KeyError:
        startDate = subreddit.created_utc

    currentDate = int(time.time())
    endDate = currentDate

    fetching = True
    while (fetching):
        #search all posts from startdate to enddate
        searchQuery = "timestamp:%d..%d" % (startDate, endDate)
        numSubmissionsFound = 0
        lastSubmissionDate = 0;

        for submission in p.search(query=searchQuery, subreddit=subreddit, sort="new", limit=None, syntax="cloudsearch"):
            challenge = submission_parser.parse_submission(submission)

            if (challenge != None):
                submission_writer.write_challenge(challenge)

            numSubmissionsFound += 1
            lastSubmissionDate = submission.created_utc

        # Reddit has a 1000 max item cache
        if (numSubmissionsFound >= 1000):
            #found max submissions , so we should keep searching just in case
            #move the time window back
            endDate = lastSubmissionDate
        else:
            fetching = False

    fetch_settings.write_last_date(currentDate)


if __name__ == '__main__':
    main()