import worker
from pyzeebe import ZeebeTaskRouter

router = ZeebeTaskRouter()


@router.task(task_type="mail")
async def my_task(message_content: str):
    ##Your business logic goes here
    print('Sending email with message content: ' + message_content)

    return {}
