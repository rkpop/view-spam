import praw


class loader(object):
    def __init__(self, details):
        self._reddit_instance = praw.Reddit(**details)

    def get_latest_removal(self):
        data = self._reddit_instance.subreddit("kpop").mod.spam(
            only="submissions", limit=1000
        )
        return data

