import time

from websocket.connection import WebSocket

# async def websocket_view(socket):
#     await socket.accept()
#     await socket.send_text('hello')
#     await socket.close()


async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        print(message)
        await socket.send_text(message)

# cuando un user envia una actión se mandaría al resto