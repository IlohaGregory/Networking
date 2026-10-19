# NOC Lab 01: SNMP Monitoring and Incident Response with PRTG

## Objective

Configure PRTG Network Monitor to collect SNMP System Uptime data from a Windows 11 host, detect a monitoring failure, generate notifications, create an incident ticket, and verify recovery.

## Environment

- Operating system: Windows 11
- Monitoring platform: PRTG Network Monitor
- Protocol: SNMP
- Sensor: SNMP System Uptime
- Target: Local Windows host

## Implementation

1. Installed and configured the Windows SNMP Service.
2. Configured a read only SNMP community string.
3. Configured the SNMP permitted host list to allow the monitoring requests.
4. Added the Windows host to PRTG and configured its SNMP credentials.
5. Added an SNMP System Uptime sensor and verified that it collected data.
6. Configured notification triggers and ticket creation for sensor state changes.

## Failure Simulation

To simulate an SNMP monitoring failure, I temporarily removed the monitoring host's current IP address from the SNMP Service's permitted-host list.

PRTG reported that the SNMP sensor was Down and that it could not retrieve a response.

## Detection and Incident Handling

- Observed the sensor transition from Up to Down.
- Examined the sensor status and notification log.
- Verified the configured notification and ticket workflow.
- Captured evidence of the incident and the monitoring interruption.

## Recovery

Restored the monitoring host's IP address to the SNMP permitted host list.

The sensor subsequently returned to the Up state. I verified recovery, resolved the incident ticket, and added a resolution comment.

## Key Lessons

- SNMP monitoring depends on correct agent configuration and permitted manager settings.
- A working IP connection does not guarantee that SNMP requests will receive a response.
- Monitoring systems can detect failures and initiate notification and ticket workflows.
- Incident handling includes identifying the symptom, investigating the cause, restoring service, and documenting resolution.

## Evidence

See the `screenshots/` directory for the baseline, sensor down, notification, ticket, and recovery evidence.
