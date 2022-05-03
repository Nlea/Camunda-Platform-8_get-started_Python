# Camunda Platform 8 - Get Started - Python
This guide explains how to get started with [Camunda Platform 8](https://camunda.com/platform/) using Python. The project uses the [PyZeebe](https://github.com/camunda-community-hub/pyzeebe) client.

## Install the module
``` pip install pyzeebe```

## Create a client
If we want to connect to a Camunda Platform 8 SaaS. We need to [create a Cluster](https://docs.camunda.io/docs/components/console/manage-clusters/create-cluster/)
and provide the ```cluster id (Zeebe Address)```. Additionally, for [the authentication](https://docs.camunda.io/docs/components/console/manage-clusters/manage-api-clients/) we need the ```client id``` and the ```the client secret```. 

This project saves the credentials in a ```.env``` file (not part of this repo) with a structure like this: 
```env
ZEEBE_ADDRESS='xxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
ZEEBE_CLIENT_ID='xxxxxxxxxxx-x-xxxxxxx-'
ZEEBE_CLIENT_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```
Make sure to delete `.bru-2.zeebe.camunda.io:443` from the Zeebe Address. 

The [python-dotenv](https://github.com/theskumar/python-dotenv) module sets key value pairs as environment variables from the ```.env``` file.
Make sure to install it: 

```pip install python-dotenv ```

The [os](https://docs.python.org/3/library/os.html) module reads out the environment variables in your client and worker. Os is part of the Python standard library.

The credentials can be specified in the client builder:

```python
load_dotenv()
    my_client_id = os.environ.get('ZEEBE_CLIENT_ID')
    my_client_secret = os.environ.get('ZEEBE_CLIENT_SECRET')
    my_cluster_id = os.environ.get('ZEEBE_ADDRESS')
    
    grpc_channel = create_camunda_cloud_channel(
        client_id= my_client_id,
        client_secret=my_client_secret,
        cluster_id= my_cluster_id,
        region="bru-2",  # Default is bru-2
        )
        
    zeebe_client = ZeebeClient(grpc_channel)


```
If you are using a self-managed Camunda Platform 8 cluster, you create a client with an insecure channel:

```python
channel = create_insecure_channel()  # Will use ZEEBE_ADDRESS environment variable or localhost:26500
client = ZeebeClient(channel)
```

## Deploy Process and Start Instance
To deploy a process you have to specify the filepath of the BPMN file.

```python
 await zeebe_client.deploy_process('send-mail.bpmn')
```

To start a new instance you can specify the ```bpmnProcessId```, i.e. ```send-email``` and **optionally** process variables.

```python
 result = await zeebe_client.run_process(bpmn_process_id="send-email", variables={"message_content":"Hello from the Python get started"})
```
For the complete code see [deploy-and-start-instance.py](). You can run it using the following command:

```
python deploy-and-start-instance.py
```
 
## Job Worker

