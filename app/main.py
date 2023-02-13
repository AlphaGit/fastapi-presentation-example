from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.repositories.post import PostRepository

app = FastAPI()

@app.get("/system/health")
def get_health():
    return {"health": "OK"}

class BlogPost(BaseModel):
    title: str = Field(
        min_length=3,
        max_length=200,
        example="First post",
        description="Title of the post",
    )
    content: str = Field(
        min_length=3,
        max_length=2_000,
        example="This is my first post",
        description="Content of the post",
    )
    created_at: Optional[datetime] = Field(
        description="Date and time when the post was created",
    )

@app.post("/post")
def create_post(post: BlogPost):
    post.created_at = datetime.now()
    post_repository = PostRepository()
    return post_repository.create(post)
