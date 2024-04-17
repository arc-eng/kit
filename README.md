<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="PR Pilot Logo">
</div>

<p align="center">
  <a href="https://github.com/marketplace/pr-pilot-ai"><b>Install</b></a> |
  <a href="https://docs.pr-pilot.ai">Documentation</a> | 
  <a href="https://www.pr-pilot.ai/blog">Blog</a> | 
  <a href="https://www.pr-pilot.ai">Website</a>
</p>


# 🤖 PR Pilot - Python SDK

PR Pilot is a **text-to-task** automation platform that enables GitHub developers to trigger AI-driven development tasks in their repositories from anywhere.

This project contains the official Python SDK.

## Usage

Install the Python SDK using pip:

```bash
pip install pr-pilot
```

Use the `create_task`, `get_task` and `wait_for_result` functions to automate your Github project:

```python
from pr_pilot.util import create_task, wait_for_result

task = create_task("PR-Pilot-AI/pr-pilot", "Summarize the README file and create a Github issue with the result.")
result = wait_for_result(task)
print(f"Task completed. Result:\n\n{task.result}")
```