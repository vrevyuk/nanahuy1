import cv2
import asyncio
import websockets
from pi_camera_handler import PiCameraHandler 

async def handle_socket_connection(websocket, path):
    print("connection has been opened", websocket)
    for frame in camera.getFrames():
        await websocket.send(frame)

try:
    camera = PiCameraHandler()
    print("Start websocket server ...")
    socket_server = websockets.serve(handle_socket_connection, "0.0.0.0", 8001)
    asyncio.get_event_loop().run_until_complete(socket_server)
    asyncio.get_event_loop().run_forever()
except:
    print("\r\n")
    camera.release()



