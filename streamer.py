import cv2
import asyncio
import websockets
from camera_handler import CameraHandler 

async def handle_socket_connection(websocket, path):
    print("connection has been opened")
    for frame in camera.getFrames():
        print("got frame")
        await websocket.send(frame)

try:
    camera = CameraHandler()
    print("Start websocket server ...")
    socket_server = websockets.serve(handle_socket_connection, "localhost", 8001)
    asyncio.get_event_loop().run_until_complete(socket_server)
    asyncio.get_event_loop().run_forever()
except:
    camera.release()



