import asyncio
from pyzeebe import ZeebeWorker, Job, create_camunda_cloud_channel
from dotenv import load_dotenv
import os
from task import router


async def main():
    load_dotenv()
    my_client_id = os.environ.get('ZEEBE_CLIENT_ID')
    my_client_secret = os.environ.get('ZEEBE_CLIENT_SECRET')
    my_cluster_id = os.environ.get('ZEEBE_ADDRESS')

    channel = create_camunda_cloud_channel(
        client_id=my_client_id,
        client_secret=my_client_secret,
        cluster_id=my_cluster_id,
        region="bru-2",  # Default is bru-2
    )

    worker = ZeebeWorker(channel)  # Create a zeebe worker
    worker.include_router(router)
    await worker.work()


asyncio.run(main())
