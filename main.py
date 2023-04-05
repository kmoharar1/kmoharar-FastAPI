from fastapi import FastAPI
from fastapi.params import Body, Optional
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
    
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
"title": "favorite foods", "content": "I like Pizza", "id":2}]
    

#requests  get method url: "/"

@app.get("/")
async def root():
    return {"message": "Hello World.."}

@app.get("/posts/{id}")
def get_posts(id: int):   #(variable) my_posts: list[dict(str,any]]\
    
    post = find_post(int(id))
    print(post)
    return{"post_detail": post}


@app.get("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append() 
    return {"data": post}


#@app.get("/createposts")
#def create_posts(new_post: Post):
#    print(new_post)
#    print(new_post.dict())
#    return{"data": "new_post"}