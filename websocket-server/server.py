import asyncio
import json
import websockets
 
# create handler for each connection
CONNECTIONS = {}


async def handler(sourceWebsocket, path):
    print("WebSocket: Server Started.")
    try:
        while True:
            # Receiving values from client
            client_msg = await sourceWebsocket.recv()
            
 
            # Sending a response back to the client
            userRq = json.loads(client_msg)
            userId = userRq['userId']
            CONNECTIONS[userId] = sourceWebsocket
            await sourceWebsocket.send(json.dumps(
                {
                    "userBody": userRq
                }
            ))
 
    except websockets.ConnectionClosedError as e:
        print("Internal Server Error.")
    except websockets.exceptions.ConnectionClosed as e:
        print("client out")
 
 
 
start_server = websockets.serve(handler, "localhost", 8000)
 
 
 
asyncio.get_event_loop().run_until_complete(start_server)
 
asyncio.get_event_loop().run_forever()