from gremlin_python.driver import client, serializer
import sys
import traceback

_gremlin_cleanup_graph = "g.V().drop()"

_gremlin_insert_vertices = [
    "g.addV('person').property('id', 'thomas').property('firstName', 'Thomas').property('age', 44).property('pk', 'pk')",
    "g.addV('person').property('id', 'mary').property('firstName', 'Mary').property('lastName', 'Andersen').property('age', 39).property('pk', 'pk')",
    "g.addV('person').property('id', 'ben').property('firstName', 'Ben').property('lastName', 'Miller').property('pk', 'pk')",
    "g.addV('person').property('id', 'robin').property('firstName', 'Robin').property('lastName', 'Wakefield').property('pk', 'pk')"
]

_gremlin_insert_edges = [
    "g.V('thomas').addE('knows').to(g.V('mary'))",
    "g.V('thomas').addE('knows').to(g.V('ben'))",
    "g.V('ben').addE('knows').to(g.V('robin'))"
]

_gremlin_update_vertices = [
    "g.V('thomas').property('age', 100)"
]

_gremlin_count_vertices = "g.V().count()"

_gremlin_traversals = {
    "Get all persons older than 40": "g.V().hasLabel('person').has('age', gt(40)).values('firstName', 'age')",
    "Get all persons and their first name": "g.V().hasLabel('person').values('firstName')",
    "Get all persons sorted by first name": "g.V().hasLabel('person').order().by('firstName', incr).values('firstName')",
    "Get all persons that Thomas knows": "g.V('thomas').out('knows').hasLabel('person').values('firstName')",
    "People known by those who Thomas knows": "g.V('thomas').out('knows').hasLabel('person').out('knows').hasLabel('person').values('firstName')",
    "Get the path from Thomas to Robin": "g.V('thomas').repeat(out()).until(has('id', 'robin')).path().by('firstName')"
}

_gremlin_drop_operations = {
    "Drop Edge - Thomas no longer knows Mary": "g.V('thomas').outE('knows').where(inV().has('id', 'mary')).drop()",
    "Drop Vertex - Drop Thomas": "g.V('thomas').drop()"
}


def cleanup_graph(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(
        _gremlin_cleanup_graph))
    callback = client.submitAsync(_gremlin_cleanup_graph)
    if callback.result() is not None:
        print("\tCleaned up the graph!")
    print("\n")


def insert_vertices(client):
    for query in _gremlin_insert_vertices:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this vertex:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query: {0}".format(query))
    print("\n")


def insert_edges(client):
    for query in _gremlin_insert_edges:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tInserted this edge:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query:\n\t{0}".format(query))
    print("\n")


def update_vertices(client):
    for query in _gremlin_update_vertices:
        print("\tRunning this Gremlin query:\n\t{0}\n".format(query))
        callback = client.submitAsync(query)
        if callback.result() is not None:
            print("\tUpdated this vertex:\n\t{0}\n".format(
                callback.result().one()))
        else:
            print("Something went wrong with this query:\n\t{0}".format(query))
    print("\n")


def count_vertices(client):
    print("\tRunning this Gremlin query:\n\t{0}".format(
        _gremlin_count_vertices))
    callback = client.submitAsync(_gremlin_count_vertices)
    if callback.result() is not None:
        print("\tCount of vertices: {0}".format(callback.result().one()))
    else:
        print("Something went wrong with this query: {0}".format(
            _gremlin_count_vertices))
    print("\n")


def execute_traversals(client):
    for key in _gremlin_traversals:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}\n".format(
            _gremlin_traversals[key]))
        callback = client.submitAsync(_gremlin_traversals[key])
        for result in callback.result():
            print("\t{0}".format(str(result)))
        print("\n")


def execute_drop_operations(client):
    for key in _gremlin_drop_operations:
        print("\t{0}:".format(key))
        print("\tRunning this Gremlin query:\n\t{0}".format(
            _gremlin_drop_operations[key]))
        callback = client.submitAsync(_gremlin_drop_operations[key])
        for result in callback.result():
            print(result)
        print("\n")


try:
    client = client.Client('wss://<YOUR_ENDPOINT>.gremlin.cosmosdb.azure.com:443/', 'g',
                           username="/dbs/<YOUR_DATABASE>/colls/<YOUR_COLLECTION_OR_GRAPH>",
                           password="<YOUR_PASSWORD>",
                           message_serializer=serializer.GraphSONSerializersV2d0()
                           )

    print("Welcome to Azure Cosmos DB + Gremlin on Python!")

    # Drop the entire Graph
    input("We're about to drop whatever graph is on the server. Press any key to continue...")
    cleanup_graph(client)

    # Insert all vertices
    input("Let's insert some vertices into the graph. Press any key to continue...")
    insert_vertices(client)

    # Create edges between vertices
    input("Now, let's add some edges between the vertices. Press any key to continue...")
    insert_edges(client)

    # Update a vertice
    input("Ah, sorry. I made a mistake. Let's change the ages of one of the vertices. Press any key to continue...")
    update_vertices(client)

    # Count all vertices
    input("Okay. Let's count how many vertices we have. Press any key to continue...")
    count_vertices(client)

    # Execute traversals and get results
    input("Cool! Let's run some traversals on our graph. Press any key to continue...")
    execute_traversals(client)

    # Drop a few vertices and edges
    input("So, life happens and now we will make some changes to the graph. Press any key to continue...")
    execute_drop_operations(client)

    # Count all vertices again
    input("How many vertices do we have left? Press any key to continue...")
    count_vertices(client)

except Exception as e:
    print('There was an exception: {0}'.format(e))
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)

print("\nAnd that's all! Sample complete")
input("Press Enter to continue...")
