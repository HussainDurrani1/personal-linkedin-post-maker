import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone, timedelta
from schemas import DevelopmentActivity, ChangedFile

load_dotenv()

GITHUB_API = "https://api.github.com"


def get_today_commits(owner: str, repo: str):
    token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }

    response = requests.get(
        f"{GITHUB_API}/repos/{owner}/{repo}/commits",
        headers=headers,
        params={
            "since": (datetime.now(timezone.utc) - timedelta(days=10)).strftime(
                "%Y-%m-%dT00:00:00Z"
            )
        },
    )

    response.raise_for_status()

    commits = response.json()

    return [
        get_commit_details(owner, repo, commit["sha"], headers) for commit in commits
    ]


def get_commit_details(owner: str, repo: str, sha: str, headers: dict):
    response = requests.get(
        f"{GITHUB_API}/repos/{owner}/{repo}/commits/{sha}",
        headers=headers,
    )

    response.raise_for_status()

    commit = response.json()

    return DevelopmentActivity(
        sha=commit["sha"],
        message=commit["commit"]["message"],
        date=commit["commit"]["author"]["date"],
        files=[
            ChangedFile(
                filename=file["filename"],
                status=file["status"],
                additions=file["additions"],
                deletions=file["deletions"],
                patch=file.get("patch"),
            )
            for file in commit.get("files", [])
        ],
    )
