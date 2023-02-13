class PostRepository():
    last_id = 0
    db = {}
    db['posts'] = {}

    def create(self, post):
        PostRepository.last_id += 1
        post.id = PostRepository.last_id
        PostRepository.db.get('posts')[post.id] = post
        return post

    def get(self, post_id):
        return PostRepository.db.get('posts')[post_id]

    def get_all(self):
        return list(PostRepository.db.get('posts').values())

    def update(self, post_id, post):
        PostRepository.db.get('posts')[post_id] = post
        return post

    def delete(self, post_id):
        del PostRepository.db.get('posts')[post_id]
