# Simple subnet calculator in Python

import ipaddress

def calculate_subnet_info(ip_interface):
    # Parse the input to get an IPv4Interface object
    interface = ipaddress.ip_interface(ip_interface)
    
    # Extract the network information
    network = interface.network
    subnet_mask = interface.netmask
    network_address = network.network_address
    broadcast_address = network.broadcast_address
    
    # Calculate the number of usable hosts
    num_usable_hosts = network.num_addresses - 2  # Subtract network and broadcast addresses
    
    # Calculate the range of host addresses
    host_addresses = list(network.hosts())
    first_host = host_addresses[0]
    last_host = host_addresses[-1]
    
    # Return the calculated information
    return {
        'Subnet Mask': str(subnet_mask),
        'Network Address': str(network_address),
        'Broadcast Address': str(broadcast_address),
        'Usable Hosts': num_usable_hosts,
        'Host Address Range': f"{first_host} - {last_host}"
    }

# Example usage:
ip_interface = input("Please, provide de ip Address & Mask: ")
subnet_info = calculate_subnet_info(ip_interface)
for key, value in subnet_info.items():
    print(f"{key}: {value}")
