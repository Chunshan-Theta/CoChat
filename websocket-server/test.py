import websockets
import asyncio
import json

# The main function that will handle connection and communication
# with the server
async def ws_client():
    print("WebSocket: Client Connected.")
    url = "ws://127.0.0.1:8000"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send values to the server
        body = {
            "userId": "00001",
            "action": "test",
            "log": "200 GET \"something text\" 中文測試"
        }
        print(f"[OnGoing] Sending body to server: {body}")
        res1 = await ws.send(json.dumps(body))
        print(f"[Success] Send body to server: {res1}")
 
        # Stay alive forever, listen to incoming msgs
        while True:
            print(f"[OnGoing] Getting body to server.")
            msg = await ws.recv()
            print(f"[Success] Getting body to server.{msg}")
            print(f"[OnGoing] Pasering body from server.")
            response = json.loads(msg)
            print(f"[Success] Paser body to server.{response}")
            assert response["userBody"] == body, f"response: {response}, response.userBody: {response['userBody']}"
            print(f"[ALL Success] response: {response}, response.userBody: {response['userBody']}")
            break
 
# Start the connection
asyncio.run(ws_client())