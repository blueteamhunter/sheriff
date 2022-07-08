# sheriff
A simple DNS resolution tool
Currently supporting zone transfer attemps and the following record lookup:

A Record Lookup
 - Address or IPv4 DNS records, these store IP addresses for domain names.
 
 MX Record Lookup
 - Mail Exchanger DNS records are used to store which email servers are responsible for handling email for the domain name.
 
 NS Record Lookup
 - Nameserver DNS records store the authoritative nameserver for a domain name.
 
 SOA Record Lookup
 - Start of Authority DNS records store meta details about a domain name such as the administrator contact email address and when the domain last had changes made to its DNS configuration.
 
 TXT Record Lookup
 - Text records are used to store notes as DNS records, however they are typically used to store configuration settings for various services like SPF records which are used to define which email servers are allowed to send email from the domain or verification codes for some webmaster tools.

