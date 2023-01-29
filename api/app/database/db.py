from ..models.models import Post, PostCreate, PostUpdate
from contextlib import contextmanager
from ..config import settings
from typing import List
import psycopg2


@contextmanager
def get_db_connection():
    with psycopg2.connect(settings.postgres_dsn) as connection:
        yield connection


# ** Get All The Posts from the database (This will return a list of posts):
def get_all_posts() -> List[Post]:
    query = "select * from post;"

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            columns = [column.name for column in cursor.description]
            rows = cursor.fetchall()
            return [Post.parse_obj(dict(zip(columns, row))) for row in rows]


# ** Get a specific post from the database using its id (this will return a post object):
def get_post_by_id(post_id: int) -> List[Post]:

    query = "select * from post where id = %s;"

    with get_db_connection() as connection:

        with connection.cursor() as cursor:
            cursor.execute(query, (post_id,))
            columns = [column.name for column in cursor.description]
            row = cursor.fetchone()
            if not row:
                return None

            return Post.parse_obj(dict(zip(columns, row)))


# ** Create a new Post (this will return the post id):
def create_new_post(post: PostCreate) -> int:

    query = "insert into post (title, content, author) VALUES (%s, %s, %s) returning id;"

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,
                           (post.title, post.content, post.author)
                           )
            connection.commit()
            post_id = cursor.fetchone()[0]
            return post_id


# ** Update an existing Post (this will return the post id):
def update_post(post: PostUpdate) -> int:

    query = "update post set title=%s, content=%s where id=%s returning id;"

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query,
                           (post.title, post.content, post.id)
                           )
            connection.commit()
            post_id = cursor.fetchone()[0]
            return post_id


# ** Delete an existing Post:
def delete_post(post_id: int) -> bool:

    query = "delete from post where id=%s"

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, (post_id,))
                connection.commit()
                return True
            except (Exception, psycopg2.DatabaseError):
                return False
