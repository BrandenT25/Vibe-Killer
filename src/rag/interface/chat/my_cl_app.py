import chainlit as cl

@cl.on_window_message
async def receive_message(message: str):
    if message.startswith("Client: "):
        await cl.Message(content=f"Message from client: {message}").send()