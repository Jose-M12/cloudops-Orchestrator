from celery import shared_task
from app.services.infrastructure.terraform_wrapper import run_terraform

@shared_task(bind=True, autoretry_for=(RuntimeError,), retry_backoff=True, max_retries=5)
def terraform_apply(self, stack_path: str, vars_: dict, workspace: str):
    return run_terraform("apply", stack_path, vars_, workspace)
