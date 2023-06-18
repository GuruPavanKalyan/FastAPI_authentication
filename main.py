import uvicorn
from fastapi import FastAPI,Body,Depends
app = FastAPI()

from app.model import PostSchema,UserLoginSchema,UserSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
posts = [
    {
        "id":1,
        "title":"Penguin",
        "test": "penuings are likely to live near by Oceans"
    },
    {
        "id":2,
        "title":"Kolas",
        "test": "penuings are likely to live near by Mangrove Forest"
    },
    {
        "id":3,
        "title":"tiger",
        "test": "penuings are likely to lives in Forest"
    }
    ]
users = []

@app.get('/',tags=["test"])
def greet():
    return {"Hello":"World"}
#for getting all the posts
@app.get('/posts',tags=["posts"])
def get_Post():
    return {"data":posts}

# get single post
@app.get('/posts{id}',tags=["posts"])
def get_single_post(id:int):
    if id > len(posts):
        return {
            "error":"Post with this ID doesn't exit!"

        }
    for post in posts:
        if post["id"]==id:
            return{
                "data":post
            }

#posst a single blog post for creating a post
@app.post("/posts",dependencies=[Depends(jwtBearer())],tags=["posts"])
def add_post(post:PostSchema):
    post.id = len(posts)+1
    posts.append(post.dict())
    return {
        "info":"Post added"
    }
#for signup
@app.post('/users/signup',tags=['user'])
def user_signup(user:UserSchema=Body(default=None)):
    users.append(user)
    return signJWT(user.email)
#function to check user
def check_user(data:UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

#for login
@app.post("/user/login",tags=["user"])
def user_login(user:UserLoginSchema=Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return{
            "error":"Invalid Login Details"
        }


if __name__=="__main__":

    uvicorn.run(app,host="127.0.0.1",port="8000")