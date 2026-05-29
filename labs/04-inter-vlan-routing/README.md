# Inter-VLAN Routing Lab

## Objective:

The objective for this lab was to segment a network into VLANs and configure routing  for inter-VLAN communication. The lab focused on router subinterfaces, switch trunk ports and VLAN configuration.

## Network Topology:

View Topology.png

### The network consists of:

- 1 Router
- 1 Switch
- 2 PCS
- 2 Servers
  All PCs are connected to a central segmented switch, which is then connected to a router through a single link

```markdown
## IP Addressing Table

| Device   | Interface | IP Address  | Subnet Mask   | Default Gateway | VLAN |
| -------- | --------- | ----------- | ------------- | --------------- | ---- |
| Router   | G0/0/0.10 | 192.168.1.1 | 255.255.255.0 | N/A             | 10   |
| Router   | G0/0/0.20 | 192.168.2.1 | 255.255.255.0 | N/A             | 20   |
| PC0      | NIC       | 192.168.1.2 | 255.255.255.0 | 192.168.1.1     | 10   |
| PC1      | NIC       | 192.168.1.3 | 255.255.255.0 | 192.168.1.1     | 10   |
| Server 1 | NIC       | 192.168.2.2 | 255.255.255.0 | 192.168.2.1     | 20   |
| Server 2 | NIC       | 192.168.2.3 | 255.255.255.0 | 192.168.2.1     | 20   |

Note: IP addresses were assigned dynamically and are subject to change in future.
Veiw "Router IP table.png"
```

## Configuration Summary:

### Router:

- Configured router subinterface
- configured DHCP settings for each network pool

### Switch:
- Configured VLAN segments on switch interfaces
- configured the trunk port connected to router

### Hosts(PCs and Servers ):

- Switched IP addressing configuration from static to DHCP

### Connectivity:

- Verified successful communication between hosts within the same VLAN
- Verified successful inter-VLAN communication between PCs and Servers

## Verification Tests:

### Tests performed:

- PC0 successfully pinged PC1
- Server 0 successfully pinged Server 1
- PC0 successfully pinged Server 1

## What I Learned:

- Learned the concept of router on a stick, how to configure router subinterfaces as well as its importance
- Learned about the trunk port, VLAN encapsulation and the 802.1Q standard
- Advanced Cisco CLI navigation for router and switch

## Future Improvements:

- Expand topology

## Troubleshooting Notes

- Initial DHCP requests failed because the switch-router link was not configured as a trunk port