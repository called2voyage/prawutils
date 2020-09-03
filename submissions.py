def loop_submissions(subreddit, func, limit, *args):
     results = []
     for submission in subreddit.new(limit=limit):
         results.append(func(submission, *args))
     return results
