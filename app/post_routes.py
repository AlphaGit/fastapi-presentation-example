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
    id: Optional[int] = Field(
        description="Id of the post",
        alias="id",
    )
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

@router.get("/{post_id}", response_model=BlogPost, status_code=200,
    tags=["post"], summary="Get a post by id",
    description="Get a post by id")
def get_post(post_id: int):
    post_repository = PostRepository()
    return post_repository.get(post_id)

@router.get("/", response_model=list[BlogPost], status_code=200,
    tags=["post"], summary="Get all posts",
    description="Get all posts")
def get_all_posts():
    post_repository = PostRepository()
    return post_repository.get_all()

@router.put("/{post_id}", response_model=BlogPost, status_code=200,
    tags=["post"], summary="Update a post by id",
    description="Update a post by id")
def update_post(post_id: int, post: BlogPost):
    post_repository = PostRepository()
    return post_repository.update(post_id, post)

@router.delete("/{post_id}", status_code=204,
    tags=["post"], summary="Delete a post by id",
    description="Delete a post by id")
def delete_post(post_id: int):
    post_repository = PostRepository()
    post_repository.delete(post_id)
