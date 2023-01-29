from ..models.models import PostCreate, Post, PostUpdate
from fastapi import APIRouter, HTTPException
from ..database import db
from typing import List


router = APIRouter(
    prefix="/api/v1",
    tags=["posts"]
)


# ** Get all posts:
@router.get("/posts/all", response_model=List[Post])
async def get_all_items() -> List[Post]:
    return db.get_all_posts()


# ** get all a specific post using its id:
@router.get("/post/{post_id}")
async def get_post_by_id(post_id: int) -> Post:

    post = db.get_post_by_id(post_id)

    if not post:
        raise HTTPException(status_code=404, detail="This Post is not found")

    return post


# ** create a new post:
@router.post("/post/new", response_model=dict)
async def create_new_post(post: PostCreate) -> dict:
    post_id = db.create_new_post(post)
    return {
        "Message": "Post created successfully",
        "Post Id": post_id
    }


# ** update an existing post:
@router.put("/post/update", response_model=dict)
async def update_post(post: PostUpdate) -> dict:
    post_id = db.update_post(post)
    return {
        "Message": "Post updated successfully",
        "Post Id": post_id
    }


# ** delete an existing post:
@router.delete("/post/delete/{post_id}", response_model=dict)
async def delete_post(post_id: int) -> dict:
    res = db.delete_post(post_id)
    if res:
        return {
            "Message": "Post Deleted successfully",
        }
    else:
        raise HTTPException(status_code=400, detail="Something went wrong")
