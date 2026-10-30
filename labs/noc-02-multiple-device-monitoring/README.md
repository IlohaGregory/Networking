# NOC Lab 02: Multiple Device Monitoring with PRTG

## Objective

Configure PRTG Network Monitor to collect data from a network hosted on GNS3 VM. System Uptime, interface status.... are collected from the central SNMP enabled Router, while the VPCS on the network are monitored for connectivity using a simple ping sensor.

## Topology

view `screenshots\Topology.png`

### The network consists of:

- 1 Router(Cisco C3600)
- 2 Switches
- 2 PCS
- 1 Cloud Interface
  All PCs are connected to a central switch, which is then connected to a router(acting DHCP server). This virtual network is hosted on GNS3 VM and is connected via the Host-only network (eth0).

```markdown
## IP Addressing Table

| Device  | Interface | IP Address    | Subnet Mask   | Default Gateway |
| ------- | --------- | ------------- | ------------- | --------------- |
| R1      | Fa0/1     | 192.168.65.10 | 255.255.255.0 | N/A             |
| R1      | Fa0/0     | 192.168.10.1  | 255.255.255.0 | N/A             |
| Cloud1  | Fa0/0     | 192.168.65.1  | 255.255.255.0 | N/A             |
| PC1     | NIC       | 192.168.10.2  | 255.255.255.0 | 192.168.10.1    |
| PC2     | NIC       | 192.168.10.3  | 255.255.255.0 | 192.168.10.1    |

Note: IP addresses were assigned dynamically using DHCP and are subject to change in future.
```

## Configuration Summary:

- Installed and configured GNS3 VM to connectivity between the virtual network and my PC.
- Configured router interface, dhcp pool and VPCSs
- Configured a read only SNMP community string on Router1.
- Added the individual router interfaces to PRTG and configured their SNMP credentials.
- Added recommended SNMP sensors and verified that they collected data.
- Added the VPCS devices to PRTG and connected a simple ping sensor
- Configured notification triggers and ticket creation for sensor state changes.

## Verification Tests

### Connectivity:

- PC0 and PC1 successfully pinged Router1
- PC0 and PC1 successfully pinged VM network adapter

### Failure Simulation

To simulate an SNMP monitoring failure, I temporarily shutdown the interfaces on Router1.

PRTG reported that the SNMP sensor was Down and that it could not retrieve a response. It also reported that the VPCS were unresponsive to Ping

## Detection and Incident Handling

- Observed the sensor transition from Up to Down.
- Examined the sensor status and notification log.
- Verified the configured notification and ticket workflow.
- Captured evidence of the incident and the monitoring interruption.
  view `screenshots\Sensor-down.png`

## Recovery

Switched the router interfaces on with `no shutdown`

The sensor subsequently returned to the Up state. I verified recovery, resolved the incident ticket, and added a resolution comment.

## What I Learned:

- I learned about network adapters, their configuration and types. Used the GNS3 VM + Host-only adapter.
- How and when to manually add routes.
- Incident handling and the role monitoring software plays in trouble shooting.

## Troubleshooting Notes

- Had to manually add a route for the VPCS subnet on my local computer so that PRTG could reach it.
- Disable firewall to allow traffic from the local PC to the virtual network

## Evidence

See the `screenshots/` directory for the baseline, sensor down, notification, ticket, and recovery evidence.
