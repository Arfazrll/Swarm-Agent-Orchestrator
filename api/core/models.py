from pydantic import BaseModel, Field
from typing import List, Optional

class BlogSection(BaseModel):
    """A single section of the blog post outline."""
    title: str = Field(description="Title of the section")
    outline: str = Field(description="Key points or sub-topics for this section")
    research_notes: Optional[str] = Field(None, description="Detailed Markdown string containing research, facts, and sources for this section. DO NOT use lists.")

class BlogPlan(BaseModel):
    """The structured plan for the blog post."""
    topic: str = Field(description="The main topic of the blog post")
    suggested_title: str = Field(description="A catchy, SEO-friendly suggested title")
    sections: List[BlogSection] = Field(description="List of sections for the blog", min_items=5)
    target_word_count: int = Field(1000, description="Target total word count for the post")

class FinalBlog(BaseModel):
    """The final completed blog post."""
    title: str = Field(description="Final title used for the post")
    content: str = Field(description="The complete blog post in markdown format")
    word_count: int = Field(description="Final word count of the generated content")
