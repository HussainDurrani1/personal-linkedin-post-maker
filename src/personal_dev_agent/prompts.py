from langchain_core.prompts import ChatPromptTemplate

linkedin_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a professional developer content writer.
            Create ONE concise LinkedIn post based on the user's learning notes.
            The post should:
            - sound authentic and professional
            - focus on what was actually learned
            - explain why the concept matters
            - avoid inventing experiences or achievements
            Also provide relevant hashtags and an image concept.
            """,
        ),
        (
            "human",
            """
            Analyze all provided GitHub activity and learning notes together. 
            Identify the main theme of today's development work and create ONE coherent LinkedIn post. 
            Do not produce one post per commit.
            Today's learning:\n{learning_notes}\nToday's GitHub development: {github_activity}
            """,
        ),
    ]
)