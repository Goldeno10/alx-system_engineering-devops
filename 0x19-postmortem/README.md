The following is the incident report on the "0x17. Web stack
debugging #3" task which was released on Nov 29, 2022, 6:00 AM WAT.

# Issue Summary 

From 6:00 AM to 8:51 PM WAT the WordPress Apache server was 
returning a 500 error response message. Clients who rely on the services of this 
web server received an error response from the server. The root cause of this error was 
a typo in the name of an essential module in the configuration file.

# Timeline (All time in West African Time)

6:00 AM: A configuration push was done 
6:00 AM: The server services went down 
7:40 AM: Analysis of possible causes begins.
2:30 PM: A first failed configuration solution rollback.
3:56 PM: Another failed configuration solution rollback.
5:14 PM: Identified root cause.
6:00 PM: Successful Configuration change push.
6:02: Server restart begins.
6:10: Server fully back online.

# Root Cause 

At 6:00 AM WAT, a configuration change was inadvertently released to the 
production environment without first being released to the testing environment.
The change includes a typo in the name of a key module in the configuration file. This caused the server - without the required module - to crash. As a result, the server sent 500 internal server error responses to clients.

# Resolution and recovery 

At 6:00 AM WAT, the task was released but it was until 7:40 AM that the check into the possible causes of the failure began.
Between 2:30 PM and 5:14 PM, possible solutions were pushed, and while they all failed they also negate other possible causes and helped streamline the troubleshooting. 
By 5:14 PM the root cause was identified, it happens that a vital module in the configuration file "/var/www/html/wp-settings.php" was named with the extension ".phpp" instead of ".php".
Once this change was made and the server restarted, everything worked just fine.

# Corrective and Preventative Measures 

I have documented this issue for future cases.
To address and prevent similar issues in the future all configuration files must be properly and carefully checked for such typos.
Testing the configurations on developed servers before the push can help prevent future downtime.

Sincerely,
Muhammad Ibrahim
