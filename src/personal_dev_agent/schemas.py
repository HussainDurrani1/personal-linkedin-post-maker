from pydantic import BaseModel
class ChangedFile(BaseModel):
    filename: str
    status: str
    additions: int
    deletions: int
    patch: str | None

class DevelopmentActivity(BaseModel):
    sha: str
    message: str
    date: str
    files: list[ChangedFile]    

class LinkedInPost(BaseModel):
    post: str
    hashtags: list[str]
    image_concept: str