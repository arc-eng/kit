import logging
import os

import pr_pilot
from pr_pilot import Task, Prompt

logger = logging.getLogger(__name__)


def _get_config_from_env():
    configuration = pr_pilot.Configuration(
        host="https://app.pr-pilot.ai",
    )
    if not os.environ.get("PR_PILOT_API_KEY"):
        raise ValueError("Please set the PR_PILOT_API_KEY environment variable.")
    configuration.api_key['apiKeyAuth'] = os.environ["PR_PILOT_API_KEY"]
    return configuration


def set_github_action_output(key: str, value: str):
    """Set an output parameter for GitHub Actions."""
    # Get the path to the environment file for outputs
    output_file = os.getenv('GITHUB_OUTPUT')

    # Ensure the output file path is available
    if output_file is not None:
        with open(output_file, "a") as file:
            file.write(f"{key}={value}\n")
    else:
        logger.debug("GITHUB_OUTPUT environment variable is not set.")


def create_task(repo: str, prompt: str, log=True) -> Task:
    """Create a task for the specified repository with the given prompt."""
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.TaskCreationApi(api_client)
        task = api_instance.tasks_create(Prompt(prompt=prompt, github_repo=repo))
        dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
        set_github_action_output("task-id", str(task.id))
        set_github_action_output("task-url", dashboard_url)
        if log:
            logger.info(f"PR Pilot task created: {dashboard_url}")
        return task


def get_task(task_id: str) -> Task:
    """Get the task with the specified ID."""
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.TaskRetrievalApi(api_client)
        return api_instance.tasks_retrieve(task_id)
