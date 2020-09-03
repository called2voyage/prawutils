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
