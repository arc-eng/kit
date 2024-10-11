import base64
import logging
import os
from pathlib import Path
from typing import Optional

import arcane
from arcane import Task, Prompt, Configuration
from arcane.util import _get_config_from_env, set_github_action_output

# Set log level to INFO
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

MAX_RESULT_WAIT_TIME = 60 * 4  # 4 minutes
POLL_INTERVAL = int(os.getenv("POLL_INTERVAL", "5"))
ARCANE_API_HOST = os.getenv("ARCANE_API_HOST", "https://arcane.engineer")

if POLL_INTERVAL <= 1:
    raise ValueError("POLL_INTERVAL must be greater than 1 seconds.")


class ArcaneEngine:

    def __init__(self, api_key: str = None):
        if api_key:
            self.config = arcane.Configuration(
                host=ARCANE_API_HOST, api_key={"apiKeyAuth": api_key}
            )
        else:
            self.config = _get_config_from_env()

    def create_task(self, repo: str, prompt: str, log=True, pr_number=None, branch=None,
                    issue_number=None, gpt_model=None, image: Optional[Path]=None, **kwargs) -> Task:
        """Create a task for the specified repository with the given prompt."""
        with arcane.ApiClient(self.config) as api_client:
            api_instance = arcane.TaskCreationApi(api_client)
            if pr_number is not None:
                pr_number = int(pr_number)
            if issue_number is not None:
                issue_number = int(issue_number)

            image_base64 = base64.b64encode(image.read_bytes()).decode("utf-8") if image else None
            task = api_instance.tasks_create(Prompt(prompt=prompt, github_repo=repo, issue_number=issue_number,
                                                    branch=branch, pr_number=pr_number, gpt_model=gpt_model,
                                                    image=image_base64, **kwargs))
            dashboard_url = f"https://arcane.engineer/dashboard/tasks/{str(task.id)}/"
            set_github_action_output("task-id", str(task.id))
            set_github_action_output("task-url", dashboard_url)
            if log:
                logger.info(f"Arcane Engine task created: {dashboard_url}")
            return task

    def get_task(self, task_id: str) -> Task:
        """Get the task with the specified ID."""
        with arcane.ApiClient(self.config) as api_client:
            api_instance = arcane.TaskRetrievalApi(api_client)
            return api_instance.tasks_retrieve(task_id)

    def list_tasks(self) -> list[Task]:
        """List the last 10 tasks."""
        with arcane.ApiClient(self.config) as api_client:
            api_instance = arcane.TaskRetrievalApi(api_client)
            return api_instance.tasks_list()

    @staticmethod
    def create_api_key(github_token: str, key_name: str) -> str:
        """
        Create an API key for the user with the specified GitHub token.
        :param github_token: A valid Github token
        :param key_name: Name to be given to the API key
        :return: They API key
        """
        with arcane.ApiClient(Configuration(host=ARCANE_API_HOST)) as api_client:
            api_instance = arcane.AuthenticationApi(api_client)
            params = arcane.Input(github_token=github_token, key_name=key_name)
            return api_instance.exchange_github_token_create(params).api_key