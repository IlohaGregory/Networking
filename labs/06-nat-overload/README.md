# Network Address Translation (PAT)

## Objective:

The objective of this lab was to implement Network Address Translation using Port Address Translation (PAT), allowing multiple private hosts to communicate with a remote network through a shared public IP address.

## Network Topology:

View Topology.png

### The network consists of:

- 1 Router
- 2 Switches
- 7 PCS
- 1 Server
  The inside network consists of two VLANs distributed across two interconnected switches. The PCs are connected to access ports assigned to their respective VLANs, while the switches are connected through an interswitch link. The primary switch is connected to the router, which provides routing and connectivity between the internal networks and the server. The server is connected directly to the router.

```markdown
## IP Addressing Table

| Device   | Interface | IP Address   | Subnet Mask   | Default Gateway | VLAN |
| -------- | --------- | ------------ | ------------- | --------------- | ---- |
| Router0  | G0/0/0.10 | 192.168.10.1 | 255.255.255.0 | N/A             | 10   |
| Router0  | G0/0/0.20 | 192.168.20.1 | 255.255.255.0 | N/A             | 20   |
| Router0  | G0/0/1    | 37.4.1.30    | 255.255.255.0 | N/A             | N/A  |
| PC0      | NIC       | 192.168.10.2 | 255.255.255.0 | 192.168.10.1    | 10   |
| PC1      | NIC       | 192.168.20.2 | 255.255.255.0 | 192.168.20.1    | 20   |
| PC2      | NIC       | 192.168.20.3 | 255.255.255.0 | 192.168.20.1    | 20   |
| PC3      | NIC       | 192.168.20.4 | 255.255.255.0 | 192.168.20.1    | 20   |
| PC4      | NIC       | 192.168.10.3 | 255.255.255.0 | 192.168.10.1    | 10   |
| PC5      | NIC       | 192.168.10.4 | 255.255.255.0 | 192.168.10.1    | 10   |
| PC6      | NIC       | 192.168.20.5 | 255.255.255.0 | 192.168.20.1    | 20   |
| Server   | NIC       | 37.4.1.100   | 255.255.255.0 | 37.4.1.30       | N/A  |

Note: PC IP addresses were assigned dynamically and are subject to change in future.
```

## Configuration Summary:

### ACL Entries
```bash
ip access-list standard INSIDE_LOCAL
10 permit 192.168.10.0 0.0.0.255
```
The ACL was created to permit traffic originating from the R&D network while denying traffic from the Reception network. It was applied to the inside interface in the outbound direction toward the remote network.

### Router:

- Configured router interfaces
- configured DHCP settings for each network pool
- assigned inside and outside interfaces
- created standard access list
- applied access list to the inside interface
- configured PAT using NAT overload

### Switch:
- Configured VLAN segments on switch interfaces
- configured the trunk port connected to router

### Hosts(PCs and Servers ):

- Switched IP addressing configuration from static to DHCP

### Connectivity:

- Verified successful communication between hosts within the same VLAN
- Verified successful inter-VLAN communication between hosts in vlan 10 and vlan 20
- Verified successful communication between PCs0/1 (R&D Dept.) and remote Server
- Verified PCS2/3 (Reception) are unable to reach server.

## Verification Tests:

### Tests performed:

- PC0 successfully pinged PC1
- PC0 successfully pinged PC2
- PC0 successfully pinged Server
- PC2 unsuccessfully pinged Server
- Address translation verified (View Translation.png)

## What I Learned:

- Learned the different types of address translation and how to implement them
- Deeper understanding of how PAT works practically
- Advanced Cisco troubleshooting methods 

## Troubleshooting Notes

- Initially considered routing directly between the private networks and the remote network.
- Realized that private IP addresses are not directly routable across a public network, so NAT/PAT was required to translate the internal addresses before reaching the outside network.