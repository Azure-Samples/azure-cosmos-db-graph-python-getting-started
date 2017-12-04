---
services: cosmos-db
platforms: python
author: luisbosquez
---

# Developing a Python Gremlin app using Azure Cosmos DB
Azure Cosmos DB is a globally distributed multi-model database. One of the supported APIs is the Graph (Gremlin) API, which provides a graph data model with [Gremlin query/traversals](https://tinkerpop.apache.org/gremlin.html). This sample shows you how to use the Azure Cosmos DB with the Graph API to store and access data from a Python application.

## Running this sample

* Before you can run this sample, you must have the following prerequisites:

  * An active Azure account. If you don't have one, you can sign up for a [free account](https://azure.microsoft.com/free/). 
  * [Python](https://www.python.org/downloads/) version v3.4 or newer. In order for this sample to work with Python 2.7, change all references from `input()` to `raw_input()`.
  * [pip package manager](https://pip.pypa.io/en/stable/installing/)
  * [Git](http://git-scm.com/)
  * [Python Driver for Gremlin](https://github.com/apache/tinkerpop/tree/master/gremlin-python)


* Then, clone this repository using `git clone https://github.com/Azure-Samples/azure-cosmos-db-graph-python-getting-started.git`

* Next, substitute the endpoint and authorization key in the `connect.py`, on line 105, with your Cosmos DB account's values:

```python
client = client.Client('wss://<YOUR_ENDPOINT>:443/','g', 
        username="/dbs/<YOUR_DATABASE>/colls/<YOUR_COLLECTION_OR_GRAPH>", 
        password="<YOUR_PASSWORD>")
```

| Setting | Suggested Value | Description |
| ------- | --------------- | ----------- |
| YOUR_ENDPOINT   | [***.graphs.azure.com] | This is the Gremlin URI value on the Overview page of the Azure portal, in square brackets, with the trailing :443/ removed.  This value can also be retrieved from the Keys tab, using the URI value by removing https://, changing documents to graphs, and removing the trailing :443/. |
| port | 443 | Set the port to 443 |
| username | `/dbs/<db>/colls/<coll>` | The resource of the form `/dbs/<db>/colls/<coll>` where `<db>` is your database name and `<coll>` is your collection name. |
| password | Your primary key | This is your primary key, which you can retrieve from the Keys page of the Azure portal, in the Primary Key box. Use the copy button on the left side of the box to copy the value. |

* From a command prompt or shell, run `pip install -r requirements.txt` to get and resolve dependencies.

* From a command prompt or shell, run `python connect.py` to run the application.

## About the code
The code included in this sample is intended to get you quickly started with a Python application that connects to Azure Cosmos DB with the Graph (Gremlin) API.

## More information

- [Azure Cosmos DB](https://docs.microsoft.com/azure/cosmos-db/introduction)
- [Azure Cosmos DB : Graph API](https://docs.microsoft.com/en-us/azure/cosmos-db/graph-introduction)
- [Gremlin Python](http://tinkerpop.apache.org/docs/current/reference/#gremlin-python)
- [Gremlin-Python driver source code](https://github.com/apache/tinkerpop/tree/master/gremlin-python)
