from pydantic import BaseModel, Field,EmailStr

class PostSchema(BaseModel):
    id :int =Field(default=None)
    title : str = Field(default=None)
    content : str = Field(default =None)
    class Config:
        schema_extra={
            "post_demo":{
                'title':"some title about animals",
                "cotent":"some content about aniamls"
            }
        }
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr=Field(default=None)
    password : str =Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "name":"Bek",
                "emial":"pavankalyanbandaru6@gmail.com",
                "password":"123"
            }
        }

class UserLoginSchema(BaseModel):
    #fullname : str = Field(default=None)
    email : EmailStr=Field(default=None)
    password : str =Field(default=None)
    class Config:
        the_schema={
            "user_demo":{
                "emial":"pavankalyanbandaru6@gmail.com",
                "password":"123"
            }
        }