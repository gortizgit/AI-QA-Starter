import pathlib

PROMPT = pathlib.Path('ai/prompts/test_generation.md').read_text()

def call_llm(system_prompt: str, user_content: str) -> str:
    # TODO: integrate with your LLM provider (OpenAI/HF/etc.)
    raise NotImplementedError("Integrate your LLM provider here.")

STORY = """
User Story: As a user, I want to log in with username and password to access my dashboard.
Acceptance Criteria:
- AC1: Valid credentials return 200 and a bearer token.
- AC2: Invalid credentials return 401 with error message.
- AC3: Rate limit after 5 failed attempts in 1 minute.
- AC4: Password field is masked and required.
"""

if __name__ == "__main__":
    content = f"{PROMPT}\n\n<USER_STORY>\n{STORY}\n</USER_STORY>"
    try:
        out = call_llm("You help generate QA assets.", content)
    except NotImplementedError:
        print("[NOTE] Implement the LLM call to get YAML with TCs.")
        out = ""
    path = pathlib.Path("qa/data/generated")
    path.mkdir(parents=True, exist_ok=True)
    (path / "login_testplan.yaml").write_text(out, encoding="utf-8")
    print("Wrote qa/data/generated/login_testplan.yaml")
