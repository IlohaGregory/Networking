# Access Control List Lab

## Objective:

The objective for this lab was to create and implement access control on a network. The lab focused on router interfaces, access control lists and understanding traffic direction.

## Network Topology:

View Topology.png

### The network consists of:

- 1 Router
- 1 Switch
- 4 PCS
- 1 Servers
  All PCs are connected to a central segmented switch, which is then connected to a router through a single link. The server is connected directly to the router.

```markdown
## IP Addressing Table

| Device   | Interface | IP Address   | Subnet Mask   | Default Gateway | VLAN |
| -------- | --------- | ------------ | ------------- | --------------- | ---- |
| Router0  | G0/0/0.10 | 192.168.10.1 | 255.255.255.0 | N/A             | 10   |
| Router0  | G0/0/0.20 | 192.168.20.1 | 255.255.255.0 | N/A             | 20   |
| Router0  | G0/0/1    | 192.168.30.1 | 255.255.255.0 | N/A             | N/A  |
| PC0      | NIC       | 192.168.10.2 | 255.255.255.0 | 192.168.10.1    | 10   |
| PC1      | NIC       | 192.168.10.3 | 255.255.255.0 | 192.168.10.1    | 10   |
| PC2      | NIC       | 192.168.20.2 | 255.255.255.0 | 192.168.20.1    | 20   |
| PC3      | NIC       | 192.168.20.3 | 255.255.255.0 | 192.168.20.1    | 20   |
| Server   | NIC       | 192.168.30.2 | 255.255.255.0 | 192.168.30.1    | N/A  |

Note: IP addresses were assigned dynamically and are subject to change in future.
```

## Configuration Summary:

### ACL Entries
```bash
ip access-list standard 50
10 deny 192.168.20.0 0.0.0.255
20 permit 192.168.10.0 0.0.0.255
```
The ACL was created to deny traffic originating from the Reception network. The ACL was applied on the server facing interface so that only access to the server network was affected.

### Router:

- Configured router interfaces
- configured DHCP settings for each network pool
- created standard access list
- Applied access group to the server facing interface to filter outbound packets 

### Switch:
- Configured VLAN segments on switch interfaces
- configured the trunk port connected to router

### Hosts(PCs and Servers ):

- Switched IP addressing configuration from static to DHCP

### Connectivity:

- Verified successful communication between hosts within the same VLAN
- Verified successful inter-VLAN communication between hosts in vlan 10 and vlan 20
- Verified successful communication between PCs0/1 (R&D Dept.) and Server
- Verified PCS2/3 (Reception) are unable to reach server0.

## Verification Tests:

### Tests performed:

- PC0 successfully pinged PC1
- PC0 successfully pinged PC2
- PC0 successfully pinged Server
- PC2 unsuccessfully pinged Server (View 'Unreachability.png')

## What I Learned:

- Learned about access control lists, what they are, the types and why they are important
- Learned the fundamentals on how ACL is enforced by the router
- Built a solid mental model on how to filter the flow of traffic, inbound/outbound traffic and best places to implement ACLs
- Advanced Cisco troubleshooting methods 

## Future Improvements:

- Expand topology
- Implement extended list for better control
- Increase complexity

## Troubleshooting Notes

- Initially considered applying the ACL on the trunk connection between switch and router
- Realized this would affect traffic beyond the intended destination network
- Moved the ACL to the server-facing interface to enforce the policy closer to the protected resource