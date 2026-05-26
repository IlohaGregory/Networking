# DHCP Configuration Lab

## Objective:

The objective for this lab was to build and configure a network with dynamic IP assignment. The lab focused on router interface configuration, creating IP pools and exclusion lists as well as assigning IP automatically using DHCP.

## Network Topology:

View Topology.png

### The network consists of:

- 1 Router
- 1 Switch
- 4 PCS
  All PCs are connected to a central switch, which is then connected to a router(acting DHCP server)

```markdown
## IP Addressing Table

| Device | Interface | IP Address  | Subnet Mask   | Default Gateway |
| ------ | --------- | ----------- | ------------- | --------------- |
| Router | G0/0/0    | 192.168.1.1 | 255.255.255.0 | N/A             |
| PC0    | NIC       | 192.168.1.2 | 255.255.255.0 | 192.168.1.1     |
| PC1    | NIC       | 192.168.1.3 | 255.255.255.0 | 192.168.1.1     |
| PC2    | NIC       | 192.168.1.4 | 255.255.255.0 | 192.168.1.1     |
| PC3    | NIC       | 192.168.1.5 | 255.255.255.0 | 192.168.1.1     |

Note: IP addresses were assigned dynamically and are subject to change in future.
```

## Configuration Summary:

### Router:

- Configured router interface
- Created DHCP pool, assigned network address and subnet mask
- Configured exclusion list

### PCs:

- Switched IP addressing configuration from static to DHCP

### Connectivity:

- Verified successful communication using ping tests across all PCs

## Verification Tests:

### Tests performed:

- PC0 successfully pinged PC1 and PC2
- PC0 successfully pinged Router1

## What I Learned:

- How to configure DHCP on router interfaces
- Importance of dynamic addressing
- Basic Cisco CLI navigation

## Future Improvements:

- Combining with previous lab to implement network segmentation
- Expand topology and use subnetting to break up network range
