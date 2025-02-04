import psutil
import time

# Set threshold for network usage (in bytes)
THRESHOLD = 10000000  # 10MB

# Function to monitor network traffic
def monitor_network():
    print("Monitoring network traffic...")
    while True:
        # Get the current network stats
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Print the traffic data
        print(f"Bytes Sent: {bytes_sent / (1024 * 1024):.2f} MB")
        print(f"Bytes Received: {bytes_recv / (1024 * 1024):.2f} MB")

        # Check if either the sent or received data exceeds the threshold
        if bytes_sent > THRESHOLD or bytes_recv > THRESHOLD:
            print("Warning: High network traffic detected!")
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    monitor_network()
