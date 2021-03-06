from pydantic.class_validators import Optional
from pydantic import BaseModel, validator, constr, Field
from pydantic.typing import Literal

from rest_framework import serializers

import re


class BodyStructureValidator(BaseModel):
    method: constr(min_length=2, strip_whitespace=True)
    data: dict
    auth: constr(min_length=24, max_length=24, strip_whitespace=True)
    platform: Literal['IOS', 'Android', 'Desktop', 'Web']
    lang_code: str = Field(min_length=2, max_length=2)
    ver_api: int


# PROFILE SERIALIZERS
class ProfileValidator(BaseModel):
    username: constr(min_length=5, max_length=100, strip_whitespace=True)
    first_name: Optional[str] = Field(None, min_length=2, max_length=50, extra={'strip_whitespace': True})
    last_name: Optional[str] = Field(None, min_length=2, max_length=50, extra={'strip_whitespace': True})
    picture: Optional[str] = Field(None, min_length=2, max_length=200, extra={'strip_whitespace': True})
    private: bool

    @validator('username', allow_reuse=True)
    def check_username_len_and_char(cls, v):
        if re.fullmatch(r'[A-Za-z0-9@#-_=]{5,}', v):
            return v
        else:
            raise ValueError('number of char is less than 5 or '
                             'invalid char, valid characters are [a-z] , [A-Z] , [0-9] , [@, #, -, _]')


class FollowingRelationValidator(BaseModel):
    follower: constr(min_length=24, max_length=24, strip_whitespace=True)


class DeleteFollowingValidator(BaseModel):
    following: constr(min_length=24, max_length=24, strip_whitespace=True)


class DetermineFollowRequest(BaseModel):
    action: Literal['accept', 'reject']
    follower_id: constr(min_length=24, max_length=24, strip_whitespace=True)


# POST SERIALIZERS
class PostValidator(BaseModel):
    image: constr(min_length=5, max_length=100, strip_whitespace=True)
    caption: Optional[str] = Field(None, min_length=2, max_length=50, extra={'strip_whitespace': True})


class CommentValidator(BaseModel):
    post_id: constr(min_length=24, max_length=24, strip_whitespace=True)
    comment_text: constr(min_length=5, max_length=100, strip_whitespace=True)


class LikeValidator(BaseModel):
    post_id: constr(min_length=24, max_length=24, strip_whitespace=True)


class PagePostsValidator(BaseModel):
    profile_id: constr(min_length=24, max_length=24, strip_whitespace=True)
    start_id: Optional[str] = Field(None, min_length=24, max_length=24, extra={'strip_whitespace': True})


class SearchValidator(BaseModel):
    search_value: constr(min_length=3, max_length=50, strip_whitespace=True)
    start_id: Optional[str] = Field(None, min_length=24, max_length=24, extra={'strip_whitespace': True})


class DeletePictureValidator(BaseModel):
    image_id: constr(min_length=24, max_length=24, strip_whitespace=True)
