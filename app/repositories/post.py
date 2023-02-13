class PostRepository():
    def __init__(self):
        self.db = {}
        self.db['posts'] = []

    def create(self, post):
        self.db.get('posts').append(post)
        return post
