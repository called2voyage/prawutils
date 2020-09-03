import re

def loop_submissions(subreddit, func, limit, *args):
     results = []
     for submission in subreddit.new(limit=limit):
         results.append(func(submission, *args))
     return results

def search_title(submission, *queries):
    found = False
    for query in queries:
        if re.search(query, submission.title, re.IGNORECASE):
            found = True
    return found
