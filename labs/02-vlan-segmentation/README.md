# VLAN Segmentation Lab

## Objective:

My objective for this lab was to build, configure a network and implement segmentation using VLAN. The lab focused on switch interface configuration and verifying communication between devices on the same VLAN.

## Network Topology:

### The network consists of:

- 1 Switch
- 6 PCs
  All PCs are connected to a central switch, 3 devices were assigned to VLAN 10 and 3 devices were assigned to VLAN 20

```markdown
## IP Addressing Table

| Device | Interface | IP Address   | Subnet Mask   | VLAN |
| ------ | --------- | ------------ | ------------- | ---- |
| Switch | N/A       | N/A          | 255.255.255.0 | N/A  |
| PC0    | NIC       | 192.168.1.10 | 255.255.255.0 | 10   |
| PC1    | NIC       | 192.168.1.11 | 255.255.255.0 | 10   |
| PC2    | NIC       | 192.168.1.12 | 255.255.255.0 | 10   |
| PC3    | NIC       | 192.168.1.20 | 255.255.255.0 | 20   |
| PC4    | NIC       | 192.168.1.21 | 255.255.255.0 | 20   |
| PC5    | NIC       | 192.168.1.22 | 255.255.255.0 | 20   |
```

## Configuration Summary:

### Switch:

- Configured VLAN segments on switch interfaces

### PCs:

- Assigned static IP addresses

### Connectivity:

- Verified successful communication using ping tests on PCs on the same VLAN
- Verified unsuccessful communication using ping tests on PCs across segments

## Verification Tests:

### Tests performed:

- PC0 successfully pinged PC1 and PC2
- PC3 successfully pinged PC4 and PC5
- PC0 unsuccessfully pinged PC3

## What I Learned:

- How to configure switch interfaces
- Basic switch administrative commands
- Importance of VLAN segmentation
- Basic Cisco CLI navigation

## Future Improvements:

- Add routing across VLANs
- Add DHCP instead of static addressing
- Expand topology with additional routers
