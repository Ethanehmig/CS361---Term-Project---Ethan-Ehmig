import socket

# Global variable to store the suggested dish
received_dish = None

def send_temperature(host, port, temperature):
    global received_dish
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str(temperature).encode())
        received_dish = s.recv(1024).decode()
        print(f"Received response: {received_dish}")

# Example usage
send_temperature('localhost', 12345, 105)

# After running the sender, you can access the received_dish variable to see the stored dish
print("Received Dish:", received_dish)
