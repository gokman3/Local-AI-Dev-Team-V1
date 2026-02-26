import os
from crewai import Agent, Task, Crew, Process, LLM
from rich.console import Console
from rich.markdown import Markdown

# ---------------------------------------------------------
# 1. SYSTEM AND ENVIRONMENT SETTINGS
# ---------------------------------------------------------
os.environ["OPENAI_API_KEY"] = "NA"
os.environ["CREWAI_TRACING_ENABLED"] = "false" # Prevents terminal clutter
console = Console()

# ---------------------------------------------------------
# 2. LLM ENGINE AND PARAMETER OPTIMIZATION
# ---------------------------------------------------------
local_llm = LLM(
    model="ollama/qwen2.5-coder:3b",
    base_url="http://localhost:11434",
    temperature=0.3, # Ideal level for focused and rule-abiding code generation
    max_tokens=2048  # Prevents the model from cutting off long code in the middle
)

# ---------------------------------------------------------
# 3. FINE-TUNED AGENTS
# ---------------------------------------------------------
coder_agent = Agent(
    role='Senior Python Architect and Algorithm Expert',
    goal='Write industry-standard code that solves the user problem with the lowest Time and Space Complexity.',
    backstory=(
        "You are a top-tier software architect. Your core principles are Clean Code and SOLID rules. "
        "You ABSOLUTELY follow these rules:\n"
        "1. You always add 'Type Hinting' to the code (e.g., def func(data: list) -> dict:).\n"
        "2. When designing algorithms, you consider optimizations like Dynamic Programming or memoization.\n"
        "3. You never use conversational phrases like 'Here is your code' or 'I understand'. You focus directly on the solution.\n"
        "4. You explicitly declare required libraries (imports) at the very top of the code."
    ),
    verbose=False, 
    allow_delegation=False,
    max_iter=3, # Infinite loop (Repetition Collapse) breaker
    llm=local_llm 
)

tester_agent = Agent(
    role='Senior QA and Defensive Programming Expert',
    goal='Take the developer\'s code, ruthlessly review it, and add armor (try-except, type checking) to prevent crashes.',
    backstory=(
        "You are a highly meticulous and 'paranoid' test engineer sworn to prevent systems from crashing. "
        "When reviewing the code from the developer, you ABSOLUTELY fix the following edge cases:\n"
        "1. 'Timeout' and 'Connection Error' possibilities in scraping or network operations.\n"
        "2. The possibility of empty lists ([]), None, or invalid data types being passed to functions.\n"
        "3. Adding logging mechanisms or descriptive error messages (raise ValueError) to the code.\n"
        "You wrap the developer's code with safety blocks without breaking its core logic."
    ),
    verbose=False,
    allow_delegation=False,
    max_iter=3,
    llm=local_llm
)

doc_agent = Agent(
    role='Technical Documentation Robot',
    goal='Produce a professional Markdown document for the tested final code, adhering strictly to a rigid template.',
    backstory=(
        "You are a documentation robot with zero creativity, 100% obedient to the rules. "
        "You take the safe code from the tester agent and report it WITHOUT EVER DEVIATING from the template below:\n"
        "RULE 1: Never repeat the same word or sentence twice.\n"
        "RULE 2: Your output must strictly be in this Markdown template:\n"
        "## 🛠️ Purpose of the Function\n(1-2 clear sentences explaining the purpose)\n\n"
        "## ⚡ Performance Analysis\n- **Time:** O(...)\n- **Space:** O(...)\n\n"
        "## 🛡️ Security and Test Status\n(A short summary of the try-except or edge case protections added by the tester)\n\n"
        "## 💻 Final Code\n```python\n[CODE HERE]\n```"
    ),
    verbose=False,
    allow_delegation=False,
    max_iter=3,
    llm=local_llm 
)

# ---------------------------------------------------------
# 4. WORKFLOW AND TASK MANAGEMENT
# ---------------------------------------------------------
def run_agent_crew(user_message):
    task_code = Task(
        description=f"Write optimized code fulfilling this user request: '{user_message}'",
        expected_output="An optimized and clean code block using Type Hinting.",
        agent=coder_agent
    )
    
    task_test = Task(
        description="Take the developer's code. Add try-except blocks and error checks, considering potential network errors, empty data, and type mismatches.",
        expected_output="A safe, final code block protected against edge cases.",
        agent=tester_agent
    )

    task_doc = Task(
        description="Take the safe code from the tester agent and exactly fill out the provided Markdown template. Never repeat yourself and do not deviate from the template.",
        expected_output="A repetition-free Markdown document that perfectly matches the specified template.",
        agent=doc_agent
    )
    
    my_crew = Crew(
        agents=[coder_agent, tester_agent, doc_agent],
        tasks=[task_code, task_test, task_doc],
        process=Process.sequential,
        memory=False, # Prevents confusion and hallucinations in smaller models
        verbose=False 
    )
    
    return my_crew.kickoff()

# ---------------------------------------------------------
# 5. TERMINAL INTERFACE
# ---------------------------------------------------------
if __name__ == "__main__":
    console.print("[bold green]🤖 3-Agent Senior Software Team Active![/bold green]")
    console.print("   - To exit: [bold red]'q'[/bold red]\n")
    console.print("-" * 50)
    
    while True:
        message = console.input("[bold cyan]Assign Task:[/bold cyan] ")
        
        if message.lower() == 'q':
            console.print("[bold red]System Shutting Down...[/bold red]")
            break
            
        with console.status("[bold magenta]Agents are working (Architecture Design -> Security Testing -> Documentation)...", spinner="dots"):
            response = str(run_agent_crew(message))
        
        console.print("\n[bold green]Final Documentation and Code:[/bold green]")
        console.print(Markdown(response))
        console.print("-" * 50)