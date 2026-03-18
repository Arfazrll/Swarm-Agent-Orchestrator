import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI
from swarm import Swarm, Agent

load_dotenv()

class SwarmRouterClient:
    def __init__(self):
        self.groq_client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY")
        )
        self.gemini_client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=os.environ.get("GEMINI_API_KEY")
        )

    @property
    def chat(self):
        return self

    @property
    def completions(self):
        return self

    def create(self, model, messages, **kwargs):
        cleaned_history = []
        for msg in messages:
            cleaned_msg = {
                "role": msg.get("role"),
                "content": msg.get("content") or ""
            }
            if "tool_calls" in msg and msg["tool_calls"]:
                cleaned_msg["tool_calls"] = msg["tool_calls"]
            if "tool_call_id" in msg:
                cleaned_msg["tool_call_id"] = msg["tool_call_id"]
            cleaned_history.append(cleaned_msg)

        print(f"\n[DEBUG] AI Calling Model: {model}")
        client_to_use = self.gemini_client if "gemini" in model.lower() else self.groq_client
        
        if "tool_choice" in kwargs and kwargs["tool_choice"] is None:
            kwargs.pop("tool_choice")
        kwargs["parallel_tool_calls"] = False
        
        resp = client_to_use.chat.completions.create(model=model, messages=cleaned_history, **kwargs)
        
        if hasattr(resp, 'choices') and resp.choices:
            msg = resp.choices[0].message
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tc in msg.tool_calls:
                    args = tc.function.arguments
                    
                    if args is None or args == "" or args == "null" or args == "None":
                        tc.function.arguments = '{}'
                    elif isinstance(args, dict):
                        tc.function.arguments = json.dumps(args)
                    else:
                        try:
                            parsed = json.loads(str(args))
                            if not isinstance(parsed, dict):
                                tc.function.arguments = '{}'
                        except:
                            tc.function.arguments = '{}'
                
                print(f"[DEBUG] Tool Call: {msg.tool_calls[0].function.name} with {msg.tool_calls[0].function.arguments}")
            elif msg.content:
                print(f"[DEBUG] Content Preview: {msg.content[:100]}...")
            
        return resp

latest_result = {
    "status": "idle",
    "logs": [],
    "title": "",
    "content": ""
}

def log_event(message):
    print(f"[SWARM LOG] {message}")
    latest_result["logs"].append(message)

def generate_content(title="", content="", **kwargs):
    """Save the blog post content and mark as finished."""
    log_event(f"Blog post finalized: {title}")
    latest_result["title"] = title
    latest_result["content"] = content
    latest_result["status"] = "completed"
    return "Successfully generated blog post."

def complete_blog_post(title="", content="", **kwargs):
    """Complete the process and save the final blog."""
    return generate_content(title, content)

def transfer_to_planner(*args, **kwargs):
    """Handoff to the planning agent."""
    log_event("Transferring to Planner Agent...")
    return planner_agent

def transfer_to_researcher(*args, **kwargs):
    """Handoff to the researcher agent."""
    log_event("Transferring to Researcher Agent...")
    return researcher_agent

def transfer_to_writer(*args, **kwargs):
    """Handoff to the writer agent."""
    log_event("Transferring to Writer Agent...")
    return writer_agent

def transfer_to_editor(*args, **kwargs):
    """Handoff to the editor agent."""
    log_event("Transferring to Editor Agent...")
    return editor_agent

ALL_TOOLS = [
    transfer_to_planner, 
    transfer_to_researcher, 
    transfer_to_writer, 
    transfer_to_editor, 
    generate_content,
    complete_blog_post
]

DEFAULT_STABLE_MODEL = "llama-3.3-70b-versatile"

admin_agent = Agent(
    name="Admin Agent",
    instructions="You are the Admin. Call transfer_to_planner to start. Be professional.",
    functions=ALL_TOOLS,
    model=DEFAULT_STABLE_MODEL
)

planner_agent = Agent(
    name="Planner Agent",
    instructions="""Create a comprehensive and detailed outline for a blog post. 
The outline must contain at least 5 main sections, including an introduction, deep-dive modules, and a final conclusion.
After providing the outline as internal logic, immediately call transfer_to_researcher to get more details for each section.""",
    functions=ALL_TOOLS,
    model=DEFAULT_STABLE_MODEL
)

researcher_agent = Agent(
    name="Researcher Agent",
    instructions="""Research the topic and the outline provided by the planner in great depth. 
Collect at least 3 relevant facts or use cases for each section.
Provide these findings and transfer to the writer agent. BE EXTREMELY VERBOSE in your research notes.""",
    functions=ALL_TOOLS,
    model=DEFAULT_STABLE_MODEL
)

writer_agent = Agent(
    name="Writer Agent",
    instructions="""Write a long-form, comprehensive blog post. 
Target at least 800-1200 words. 
Use markdown formatting: headers, bold text, and bullet points. 
Flesh out every single section from the planner's outline with at least 3-4 detailed paragraphs.
Add a catchy title and a summary. 
When done, transfer to the editor agent.""",
    functions=ALL_TOOLS,
    model=DEFAULT_STABLE_MODEL
)

editor_agent = Agent(
    name="Editor Agent",
    instructions="""Review the long-form blog post. 
Ensure it is engaging, grammatically correct, and covers all points in depth. 
If it is too short (less than 1000 words), ask the writer to expand. 
If perfect, call complete_blog_post with the final TITLE and CONTENT.""",
    functions=ALL_TOOLS,
    model=DEFAULT_STABLE_MODEL
)

def run_swarm_backend(topic):
    global latest_result
    latest_result["status"] = "running"
    latest_result["logs"] = []
    latest_result["content"] = ""
    latest_result["title"] = ""
    
    log_event(f"Starting Swarm process for: {topic}")
    
    try:
        client = Swarm(client=SwarmRouterClient())
        response = client.run(
            agent=admin_agent,
            messages=[{"role": "user", "content": f"Write a blog post about {topic}"}],
            max_turns=50
        )
        
        if latest_result["status"] == "running":
            final_msg = response.messages[-1]
            if final_msg.get("content"):
                log_event("Process ended. Saving content as fallback.")
                latest_result["title"] = f"Blog Post: {topic}"
                latest_result["content"] = final_msg["content"]
                latest_result["status"] = "completed"
            else:
                log_event("Process ended without content.")
                latest_result["status"] = "failed"
                
    except Exception as e:
        log_event(f"Error: {str(e)}")
        latest_result["status"] = "failed"
    
    return latest_result
