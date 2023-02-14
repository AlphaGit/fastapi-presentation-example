from datetime import datetime


class PostRepository():
    last_id = 0
    db = {}
    db['posts'] = {}

    def create(self, post):
        PostRepository.last_id += 1
        post_id = PostRepository.last_id

        post_dict = post.dict()
        post_dict['id'] = post_id
        post_dict['createdAt'] = datetime.now()
        PostRepository.db.get('posts')[post_id] = post_dict

        return post_dict

    def get(self, post_id):
        return PostRepository.db.get('posts')[post_id]

    def get_all(self):
        return list(PostRepository.db.get('posts').values())

    def get_page(self, page, page_size):
        posts = PostRepository.db.get('posts')
        return list(posts.values())[(page - 1) * page_size:page * page_size]

    def update(self, post_id, post):
        post_dict = post.dict()
        PostRepository.db.get('posts')[post_id] = post_dict
        return post_dict

    def delete(self, post_id):
        del PostRepository.db.get('posts')[post_id]
