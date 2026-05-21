Basic Office Network Lab

Objective: My objective for this lab was to build and configure a small office network using Cisco Packet Tracer. The lab focused on static IP addressing, router interface configuration and verifying communication between devices.

Network Topology:
The network consists of:

- 1 Router
- 2 Switches
- 4 PCs
  All PCs are connected through switches to a central router.

IP Addressing Table:

VERY important habit.

Use a markdown table.

Example:

```markdown id="md4"
## IP Addressing Plan

| Device | Interface | IP Address   | Subnet Mask   | Default Gateway |
| ------ | --------- | ------------ | ------------- | --------------- |
| Router | G0/0      | 192.168.1.1  | 255.255.255.0 | N/A             |
| PC1    | NIC       | 192.168.1.10 | 255.255.255.0 | 192.168.1.1     |
| PC2    | NIC       | 192.168.1.11 | 255.255.255.0 | 192.168.1.1     |
```

This is VERY good engineering practice.

---

Configuration Summary:
Router:

- Configured IP addresses on router interfaces
- Enabled interfaces using `no shutdown`
  PCs:
- Assigned static IP addresses
- Configured default gateways
  Connectivity:
- Verified successful communication using ping tests on local and remote network

Verification Tests:
Tests performed:

- PC1 successfully pinged Router interface
- PC1 successfully pinged PC3
- All devices communicated successfully

Problems Encountered:

- Didn't realize router interfaces were down, even after IP assignment.
- Solved the issue using `no shutdown`

What I Learned:

- How to configure router interfaces
- Basic router administrative commands
- Importance of default gateways
- How to troubleshoot failed connectivity
- Basic Cisco CLI navigation

Future Improvements:

- Add VLAN segmentation
- Add DHCP instead of static addressing
- Expand topology with additional routers
