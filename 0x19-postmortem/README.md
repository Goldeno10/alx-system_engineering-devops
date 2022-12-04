## Background Context


Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

- To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
- And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.

The structure is actually surprisingly simple and yet powerful. The report is made up of five parts, an issue summary, a timeline, root cause analysis, resolution and recovery, and lastly, corrective and preventative measures. Lets review each of these parts in detail.

# Issue Summary

- short summary (5 sentences)
- list the duration along with start and end times (include timezone)
- state the impact (most user requests resulted in 500 errors, at peak 100%)
- close with root cause

# Timeline

- list the timezone
- covers the outage duration
- when outage began
- when staff was notified
- actions, events, …
- when service was restored

# Root Cause

- give a detailed explanation of event
- do not sugarcoat

# Resolution and recovery

- give detailed explanation of actions taken (includes times)

# Corrective and Preventative Measures

- itemized list of ways to prevent it from happening again
- what can we do better next time?
