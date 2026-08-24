# mibs
This MIB Repository is based on the original repository provided by snmplabs with updates from the mib collection from librenms.

In Addition an index is published allowing remote clients to identify a mib based on OID alone. All hosted on github pages.


pysnmplib (formerly pysnmp) applications can retrieve mibs from `https://pysnmp.github.io/mibs/asn1/@mib@`

## IPv6 listeners

IPv6 listener support is disabled by default. Enabling it adds IPv6 listeners while preserving the existing IPv4 listeners on both endpoints:

- MIB content: TCP/8000
- NGINX status and readiness: TCP/8080
