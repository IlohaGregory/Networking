# Secure Zones with Fortigate Firewall

## Objective

Design and configure a basic enterprise network with DMZs and trusted zones, using Fortigate firewall to enforce policies and dictate the interactions between internal LAN, DMZ and the cloud.

## Topology

view `screenshots\Topology.png`

### The network consists of:

- 1 Fortigate Firewall (v7.0.9)
- 1 Switch
- 4 PCS
- 1 Cloud Interface
  PCs 1-3 are connected to a segmented switch, which is then connected to the firewall(acting DHCP server). This virtual network is hosted on GNS3 VM and is connected via the Host-only network (eth0).

```markdown
## IP Addressing Table

| Device | Interface | IP Address     | Subnet Mask   | Default Gateway | VLAN |
| ------ | --------- | -------------- | ------------- | --------------- | ---- |
| Cloud1 | eth0      | 192.168.65.1   | 255.255.255.0 | N/A             | N/A  |
| FW     | port1     | 192.168.65.100 | 255.255.255.0 | N/A             | N/A  |
| FW     | port3     | 192.168.40.1   | 255.255.255.0 | N/A             | N/A  |
| FW     | port2.1   | 192.168.20.1   | 255.255.255.0 | N/A             | 20   |
| FW     | port2.2   | 192.168.30.1   | 255.255.255.0 | N/A             | 30   |
| PC1    | NIC       | 192.168.30.2   | 255.255.255.0 | 192.168.30.1    | 30   |
| PC2    | NIC       | 192.168.30.3   | 255.255.255.0 | 192.168.30.1    | 30   |
| PC3    | NIC       | 192.168.20.2   | 255.255.255.0 | 192.168.20.1    | 20   |
| PC4    | NIC       | 192.168.40.10  | 255.255.255.0 | 192.168.40.1    | N/A  |

Note: VLAN 20 = Admin, VLAN 30 = Users
```

see `screenshot/interfaces.png` for dashboard interfaces

## Configuration Summary:

- Configured basic credentials on the firewall.
- Configured firewall WAN interface to the connected cloud
- Configured LAN sub-interface(VLAN 20 and 30) and DMZ interface
- Enabled DHCP on internal VLAN interfaces
- Created firewall policies to control traffic between zones
- Configured a Virtual IP to allow controlled inbound access from the WAN to the DMZ host

## Verification Tests

### Firewall Policies:

- Allow WAN -> LAN for all services
- Allow LAN -> WAN for all services
- Allow WAN -> DMZ for HTTP and Ping
- Allow VLAN 20 -> VLAN 30 for all services
- Allow VLAN 30 -> VLAN 20 for Ping

### Results

Internal segmentation and WAN access worked as intended. WAN → DMZ policy showed traffic hits even though the VPCS could not respond

see `screenshots/Policies.png` for dashboard policies

### Connectivity:

- PC1-4 successfully pinged VM network adapter
- PC1-2 successfully pinged PC3 and vice versa
- PC4(DMZ) unsuccessfully pinged PC1-3

Note: The DMZ is accessible from the internet via an assigned Virtual IP

see `screenshots\Connectivity.png` for basic ping test on a single VPCS

## What I Learned:

- Basic firewall configurations and commands
- Workflow in designing and building enterprise networks
- The importance of a trusted zone, firewall policies and a DMZ
- Virtual IP and outbound internet connections using PAT

## Future Improvements

- Right now the VPCS in the DMZ is too lightweight and does not actually listen on port 80, however traffic can be seen on the firewall rule so connectivity is verifiable. I would like to change this to a lightweight linux server for actual connectivity.
- Expand network for increased complexity
