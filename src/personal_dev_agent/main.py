from pydantic import BaseModel
from github import get_today_commits
from llm import linkedin_chain

commits = get_today_commits(owner="HussainDurrani1", repo="BoxspirePackaging")

learning_notes = """
I am building my Boxpire Packaging website backend.
Currently 5 posts uploaded, Heading: Backend Development | Episode 6
Also, try to add humor, where I got stuck, what I learned, and what I built so far.
Extract the data from the commits on GitHub, to know what I am learning and building.
"""

response = linkedin_chain.invoke({
    "learning_notes": learning_notes,
    "github_activity": commits,
})

print(f"Post: {response.post}")
print(f"Hashtags: {response.hashtags}")
print(f"Image_concept: {response.image_concept}")
