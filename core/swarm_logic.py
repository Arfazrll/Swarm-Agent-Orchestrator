import os
import json
from core.agents import run_pydantic_ai_pipeline

# Global state for Flask (backward compatibility)
latest_result = {
    "status": "idle",
    "logs": [],
    "title": "",
    "content": ""
}

def log_event(message):
    print(f"[AI LOG] {message}")
    latest_result["logs"].append(message)

def run_swarm_backend(topic):
    """
    Interface for app.py to run the new Pydantic AI pipeline.
    """
    global latest_result
    latest_result["status"] = "running"
    latest_result["logs"] = [f"Starting generation for topic: {topic}"]
    
    try:
        # Run the structured pipeline
        blog = run_pydantic_ai_pipeline(topic)
        
        latest_result["title"] = blog.title
        latest_result["content"] = blog.content
        latest_result["status"] = "completed"
        log_event("Blog post generation completed successfully!")
        
    except Exception as e:
        log_event(f"Error in pipeline: {str(e)}")
        latest_result["status"] = "failed"
    
    return latest_result
