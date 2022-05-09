from pyzeebe import ZeebeTaskRouter

router = ZeebeTaskRouter()


@router.task(task_type="email")
async def my_task(message_content: str):
    ##Your business logic goes here
    print('Sending email with message content: ' + message_content)

    return {}
