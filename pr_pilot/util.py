import os
import time

import pr_pilot
from pr_pilot import Task, Prompt


def _get_config_from_env():
    configuration = pr_pilot.Configuration(
        host="https://app.pr-pilot.ai",
    )
    if not os.environ.get("PR_PILOT_API_KEY"):
        raise ValueError("Please set the PR_PILOT_API_KEY environment variable.")
    configuration.api_key['apiKeyAuth'] = os.environ["PR_PILOT_API_KEY"]
    return configuration


def create_task(repo: str, prompt: str) -> Task:
    """Create a task for the specified repository with the given prompt."""
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.TaskCreationApi(api_client)
        return api_instance.tasks_create(Prompt(prompt=prompt, github_repo=repo))


def get_task(task_id: str) -> Task:
    """Get the task with the specified ID."""
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.TaskRetrievalApi(api_client)
        return api_instance.tasks_retrieve(task_id)
