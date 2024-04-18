import logging
import os
import time

import pr_pilot
from pr_pilot import Task, Prompt

# Set log level to INFO
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

MAX_RESULT_WAIT_TIME = 60 * 4  # 4 minutes
POLL_INTERVAL = 5


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


def set_github_step_summary(summary: str):
    """Set the step summary for GitHub Actions."""
    # Get the path to the environment file for outputs
    output_file = os.getenv('GITHUB_STEP_SUMMARY')

    # Ensure the output file path is available
    if output_file is not None:
        with open(output_file, "a") as file:
            file.write(f"{summary}\n")
    else:
        logger.debug("GITHUB_STEP_SUMMARY environment variable is not set.")


def create_task(repo: str, prompt: str, log=True, pr_number=None, issue_number=None) -> Task:
    """Create a task for the specified repository with the given prompt."""
    with pr_pilot.ApiClient(_get_config_from_env()) as api_client:
        api_instance = pr_pilot.TaskCreationApi(api_client)
        if pr_number is not None:
            pr_number = int(pr_number)
        if issue_number is not None:
            issue_number = int(issue_number)
        task = api_instance.tasks_create(Prompt(prompt=prompt, github_repo=repo, issue_number=issue_number, pr_number=pr_number))
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


def wait_for_result(task: Task, log=True, write_step_summary=True) -> str:
    """Wait for the task to be completed and return the result."""
    start_time = time.time()
    while task.status not in ["completed", "failed"]:
        if time.time() - start_time > MAX_RESULT_WAIT_TIME:
            raise TimeoutError("The task took too long to complete.")
        if log:
            logger.info(f"Task status: {task.status}. Waiting for completion...")
        task = get_task(task.id)

        time.sleep(POLL_INTERVAL)
    if write_step_summary:
        dashboard_url = f"https://app.pr-pilot.ai/dashboard/tasks/{str(task.id)}/"
        markdown_link = f"[Event Log]({dashboard_url})"
        set_github_step_summary(f"{task.result}\n\n{markdown_link}")
    return task.result