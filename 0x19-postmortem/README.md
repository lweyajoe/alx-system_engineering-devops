# Postmortem Report

**Issue Summary:**
On 01/8/2023, a critical issue was detected in our job board project. The outage lasted for approximately 1 day and impacted the functionality of the entire job board platform. Users experienced slow response times, and many of them encountered difficulties accessing the website during this period. Approximately 100% of our users were affected by this outage. The root cause of the issue was traced back to a misconfiguration in the web server.

**Timeline:**
- 01/08/2023 and 2.30 a.m: The issue was initially detected when users started reporting slow loading times and difficulties accessing the job board platform.
- Actions Taken: Our monitoring system triggered an alert for increased response times. The engineering team was alerted and started investigating the issue. Initial assumptions pointed to potential database problems.
- Misleading Investigation: As part of the initial investigation, we focused on the database, assuming that it might be the bottleneck. However, after careful examination, it was determined that the database was functioning correctly.
- Escalation: The incident was escalated to the senior engineering team to expedite the resolution process.
- Resolution: Upon further inspection, it was discovered that a misconfiguration in the web server settings was causing the slowdown. Specifically, the server was not properly optimized to handle incoming traffic. The misconfiguration was corrected by adjusting server settings.

**Root Cause and Resolution:**
The root cause of the issue was a misconfiguration in the web server settings. The server was not adequately configured to handle the incoming traffic, resulting in slow response times and difficulties for users in accessing the platform.

To resolve the issue, we performed the following steps:
- Identified the specific misconfiguration in the web server settings.
- Adjusted the server settings to optimize resource allocation for incoming traffic.
- Monitored the system to ensure that response times returned to normal and that users could access the platform without issues.

**Corrective and Preventative Measures:**
To prevent similar issues in the future and improve the overall reliability of our job board project, we have identified the following corrective and preventative measures:

1. Regular Configuration Audits: Implement regular audits of server configurations to identify and rectify any misconfigurations promptly.

2. Enhanced Monitoring: Strengthen our monitoring system to provide early alerts for abnormal server behavior and potential misconfigurations.

3. Documentation: Maintain up-to-date documentation of server configurations and best practices to ensure that future configurations are optimized for traffic.

4. Load Testing: Conduct load testing under controlled conditions to simulate heavy traffic and identify potential bottlenecks or misconfigurations before they impact users.

5. Incident Response Plan: Develop and refine an incident response plan to ensure that all team members know how to escalate and address critical issues promptly.

By implementing these measures, we aim to enhance the stability and performance of our job board platform, providing a seamless experience for our users and minimizing the risk of similar incidents in the future.