<div align="center">
<img src="https://avatars.githubusercontent.com/ml/17635?s=140&v=" width="100" alt="Arcane Engine Logo">
</div>

<p align="center">
  <a href="https://github.com/apps/arcane-engine/installations/new"><b>Install</b></a> |
  <a href="https://docs.arcane.engineer">Documentation</a> |
  <a href="https://arcane.engineer/">Website</a>
</p>

# Arcane Kit

Welcome to the development kit for **[Arcane Engine](https://arcane.engineer/engine)**, a platform that enables developers to create agentic workflows easily.

This project contains the official Python SDK.

## Usage

Install the Python SDK using pip:

```bash
pip install arcane-engine
```

Use the `ArcaneEngine` class to create tasks and interact with the engine. Here's an example of how to create a task and wait for the result:

```python
from arcane.engine import ArcaneEngine
from arcane.util import wait_for_result

engine = ArcaneEngine()
task = engine.create_task("arc-eng/kit", "Summarize the README file and create a Github issue with the result.")
result = wait_for_result(task)
print(f"Task completed. Result:\n\n{task.result}")
```
