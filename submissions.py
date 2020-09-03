# Copyright 2020 called2voyage
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import re

def loop_submissions(subreddit, func, limit, *args):
    """Loop over submissions on a given subreddit with
    a given limit and apply a function to each submission
    with optional arguments, any outputs of the function are
    returned as a list

    Keyword arguments:
    subreddit -- the subreddit to gather submissions from
    func      -- the function to apply to each submission
    limit     -- number of submissions to limit the retrievals
    *args     -- optional arguments to pass to the function
    """
    results = []
    for submission in subreddit.new(limit=limit):
        results.append(func(submission, *args))
    return results

def search_title(submission, *queries):
    """Search a submission title for given expressions
    and return True if any found, ignore case

    Keyword arguments:
    submission -- the submission to check
    *queries   -- the expressions to look for
    """
    found = False
    for query in queries:
        if re.search(query, submission.title, re.IGNORECASE):
            found = True
    return found
