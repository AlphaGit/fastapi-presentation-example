from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import BaseModel, Field

from app.repositories.post import PostRepository

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

class ModifyBlogPostRequest(BaseModel):
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

class BlogPostResponse(BaseModel):
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

class PaginationRequest(BaseModel):
    page: int = Field(
        gt=0,
        example=1,
        description="Page number",
    )
    page_size: int = Field(
        gt=0,
        lt=100,
        example=10,
        description="Number of items per page",
        alias="pageSize",
    )

@router.post("/", response_model=BlogPostResponse, status_code=201,
    tags=["post"], summary="Create a new post",
    description="Create a new post")
def create_post(post: ModifyBlogPostRequest, db: PostRepository = Depends()):
    result = db.create(post)
    return BlogPostResponse(**result)

@router.get("/{post_id}", response_model=BlogPostResponse, status_code=200,
    tags=["post"], summary="Get a post by id",
    description="Get a post by id")
def get_post(post_id: int, db: PostRepository = Depends()):
    result = db.get(post_id)
    return BlogPostResponse(**result)

@router.get("/", response_model=list[BlogPostResponse], status_code=200,
    tags=["post"], summary="Get all posts (paginated)",
    description="Get all posts (paginated)")
def get_all_posts_paginated(db: PostRepository = Depends(), pagination: PaginationRequest = Depends()):
    result = db.get_page(pagination.page, pagination.page_size)
    return [BlogPostResponse(**post) for post in result]

@router.put("/{post_id}", response_model=BlogPostResponse, status_code=200,
    tags=["post"], summary="Update a post by id",
    description="Update a post by id")
def update_post(post_id: int, post: ModifyBlogPostRequest, db: PostRepository = Depends()):
    result = db.update(post_id, post)
    return BlogPostResponse(**result)

@router.delete("/{post_id}", status_code=204,
    tags=["post"], summary="Delete a post by id",
    description="Delete a post by id")
def delete_post(post_id: int, db: PostRepository = Depends()):
    db.delete(post_id)

@router.post("/seed", status_code=204, tags=["post"], summary="Seed posts",
             description="Seed posts (create initial database)")
def seed_posts(background_tasks: BackgroundTasks, db: PostRepository = Depends()):
    background_tasks.add_task(db.seed)
