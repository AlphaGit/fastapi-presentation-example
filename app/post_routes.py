from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.repositories.post import PostRepository

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

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
        alias="createdAt",
    )

@router.post("/", response_model=BlogPost, status_code=201,
    tags=["post"], summary="Create a new post",
    description="Create a new post")
def create_post(post: BlogPost):
    post.created_at = datetime.now()
    post_repository = PostRepository()
    return post_repository.create(post)
