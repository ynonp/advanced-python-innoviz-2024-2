import asyncio
import logging

num_clients = 0

async def client_connected_handler(reader, writer):
    global num_clients
    num_clients += 1
    print(f"You are my {num_clients}th client")
    line = await reader.readline()
    writer.write(line.upper())
    await writer.drain()
    writer.close()
    num_clients -= 1

async def tcp_echo_server():
    print("Starting a server")
    server = await asyncio.start_server(client_connected_handler, port='9999')
    await server.serve_forever()

logging.basicConfig(level=logging.DEBUG)
asyncio.run(tcp_echo_server(), debug=True)

