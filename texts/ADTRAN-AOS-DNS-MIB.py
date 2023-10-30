#
# PySNMP MIB module ADTRAN-AOS-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DNS-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:11:28 2023
# On host fv-az443-612 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSApplications = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSApplications")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Unsigned32, IpAddress, Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks, Bits, Counter64, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Bits", "Counter64", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSDns = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1))
adGenAOSDns.setRevisions(('2012-04-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSDns.setRevisionsDescriptions(('Created the adGenAosDns MIB.\n                    Changes by Stefan Hammer.',))
if mibBuilder.loadTexts: adGenAOSDns.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: adGenAOSDns.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSDns.setContactInfo('        Technical Support Dept.\n                        Postal: ADTRAN, Inc.\n                        901 Explorer Blvd.\n                        Huntsville, AL 35806\n\n                   Tel: +1 800 923 8726\n                   Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSDns.setDescription('The MIB module for AdtranOS Dns statistics.')
adDnsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0))
adDnsTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsTimestamp.setStatus('current')
if mibBuilder.loadTexts: adDnsTimestamp.setDescription('The time (seconds since epoch) that DNS event occured')
adDnsNameserverInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsNameserverInetAddressType.setStatus('current')
if mibBuilder.loadTexts: adDnsNameserverInetAddressType.setDescription('The address type of adDnsNameserverInetAddress')
adDnsNameserverInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsNameserverInetAddress.setStatus('current')
if mibBuilder.loadTexts: adDnsNameserverInetAddress.setDescription('The IP address of the nameserver for the DNS Resolution')
class AdDnsRequestErrorConditionTC(TextualConvention, Integer32):
    description = "Indicates which specific error condition occurred. Error codes 0-15 are\n        the RCODE error codes, while 16-n are Adtran proprietary DNS Request\n        error conditions.\n        \n        The noError(0) state indicates that there is no error condition.\n        \n        The formatError(1) state indicates that name server was unable to interpret the\n        query.\n        \n        The serverFailure(2) state indicates that  name server was unable to process this\n         query due to a problem with the name server.\n        \n        The nameError(3) state indicates that the domain name referenced in the query does \n        not exist.  Meaningful only for responses from an authoritative name server.\n        \n        The notImplemented(4) state indicates that the  name server does not support\n        the requested kind of query.\n        \n        The refused(5) state indicates the name server refuses to perform the specified \n        operation for policy reasons. For example, a name server may not wish to \n        provide the information to the particular requester, or a name server may\n        not wish to perform a particular operation (e.g., zone transfer) for \n        particular data.\n        \n        The 6-15 states are reserved for future use.\n        \n        The unsuportedRCode(16) state indicates that the AOS unit does not support the\n        RCODE (error condition) returned by the DNS sever.\n        \n        The malformedResponse(17) state indicates that AOS unit received an improperly\n        formated data packet from the DNS server.\n        \n        The parseError(18) state indicates that AOS unit could not parse the data from\n        the DNS server correctly.\n        \n        The timeoutWaitingForResponse(19) state indicates that AOS unit did not receive\n        a response from DNS server in the predetermined waiting period.\n        \n        The emptyResponse(20) state indicates that the AOS unit received an empty\n        response from the DNS server.  Many DNS servers send responses without any \n        answers as a form of failure.\n        \n        The unsupportedType(21) state indicates that the AOS unit does not support the\n        qtype indicated in the DNS server's answer.\n        \n        The onlyRootAnswer(22) state indicates that the DNS server responded only with\n        a '.' answer, the root domain. Per RFC2782 page 6, this is a failure.\n        \n        The portDeficiency(23) state indicates that the AOS unit failed to allocate\n        an open port to send the DNS question to the DNS sever.\n        \n        The noServerConfigured(24) state indicates that the AOS unit does not have a\n        DNS lookup server configured.\n        \n        The updSendError(25) state indicates that the AOS unit could not send the\n        DNS question packet (maybe a routing issue with the configured name-server)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("noError", 0), ("formatError", 1), ("serverFailure", 2), ("nameError", 3), ("notImplemented", 4), ("refused", 5), ("unsuportedRCode", 16), ("malformedResponse", 17), ("parseError", 18), ("timeoutWaitingForResponse", 19), ("emptyResponse", 20), ("unsupportedType", 21), ("onlyRootAnswer", 22), ("portDeficiency", 23), ("noServerCOnfigured", 24), ("udpSendError", 25))

adDnsRequestErrorCondition = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 4), AdDnsRequestErrorConditionTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsRequestErrorCondition.setStatus('current')
if mibBuilder.loadTexts: adDnsRequestErrorCondition.setDescription('This field indicates which specific error condition occurred')
adDnsDomainName = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsDomainName.setStatus('current')
if mibBuilder.loadTexts: adDnsDomainName.setDescription('The FQDN sent in the QNAME field of the question section of the DNS request')
class AdDnsResourceRecordTypeTC(TextualConvention, Integer32):
    description = "       A       =       1,  // a host address RFC1035\n            NS      =       2,  // an authoritative name server RFC1035\n            MD      =       3,  // a mail destination (Obsolete - use MX) RFC1035\n            MF      =       4,  // a mail forwarder (Obsolete - use MX) RFC1035\n            CNAME   =       5,  // the canonical name for an alias RFC1035\n            SOA     =       6,  // marks the start of a zone of authority RFC1035\n            MB      =       7,  // a mailbox domain name (EXPERIMENTAL) RFC1035\n            MG      =       8,  // a mail group member (EXPERIMENTAL) RFC1035\n            MR      =       9,  // a mail rename domain name (EXPERIMENTAL) RFC1035\n            NULL    =       10, // a null RR (EXPERIMENTAL) RFC1035\n            WKS     =       11, // a well known service description RFC1035\n            PTR     =       12, // a domain name pointer RFC1035\n            HINFO   =       13, // host information RFC1035\n            MINFO   =       14, // mailbox or mail list information RFC1035\n            MX      =       15, // mail exchange RFC1035\n            TXT     =       16, // text strings RFC1035\n            AAAA    =       28, // Ipv6 quad A addresses RFC3596\n            SRV     =       33, // service record RFC2782\n            A_PLUS_AAAA  =  65537 // Beyond 16 bit range. \n            Not a record. An A query's and AAAA query's results bound together"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 28, 33, 65537))
    namedValues = NamedValues(("a", 1), ("ns", 2), ("md", 3), ("mf", 4), ("cname", 5), ("soa", 6), ("mb", 7), ("mg", 8), ("mr", 9), ("null", 10), ("wks", 11), ("ptr", 12), ("hinfo", 13), ("minfo", 14), ("mx", 15), ("txt", 16), ("aaaa", 28), ("srv", 33), ("aplusaaaa", 65537))

adDnsResourceRecordType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 6), AdDnsResourceRecordTypeTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsResourceRecordType.setStatus('current')
if mibBuilder.loadTexts: adDnsResourceRecordType.setDescription('This field indicates which record type the request was querying.')
adDnsIndividualResolutionFailure = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"), ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"), ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"), ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
if mibBuilder.loadTexts: adDnsIndividualResolutionFailure.setStatus('current')
if mibBuilder.loadTexts: adDnsIndividualResolutionFailure.setDescription('This trap indicates that a DNS resolution failure has occured for a single,\n        particular lookup.  Information about the lookup and the failure are contained\n        within this trap.')
adGenAOSDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13))
adGenAOSDnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1))
adGenAOSDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2))
adGenAOSDnsFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2, 1)).setObjects(("ADTRAN-AOS-DNS-MIB", "adGenAOSDnsInfoGroup"), ("ADTRAN-AOS-DNS-MIB", "adGenAOSDnsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsFullCompliance = adGenAOSDnsFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDnsFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n            version 2 of the adGenAOSDns MIB.')
adGenAOSDnsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 1)).setObjects(("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"), ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"), ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"), ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsInfoGroup = adGenAOSDnsInfoGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDnsInfoGroup.setDescription('Objects designed to assist in providing information about DNS Client.')
adGenAOSDnsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 2)).setObjects(("ADTRAN-AOS-DNS-MIB", "adDnsIndividualResolutionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsNotificationGroup = adGenAOSDnsNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSDnsNotificationGroup.setDescription('Objects designed to assist in sending DNS notifications.')
mibBuilder.exportSymbols("ADTRAN-AOS-DNS-MIB", adDnsRequestErrorCondition=adDnsRequestErrorCondition, adGenAOSDnsConformance=adGenAOSDnsConformance, adGenAOSDnsGroup=adGenAOSDnsGroup, adDnsDomainName=adDnsDomainName, adGenAOSDnsFullCompliance=adGenAOSDnsFullCompliance, adDnsResourceRecordType=adDnsResourceRecordType, AdDnsRequestErrorConditionTC=AdDnsRequestErrorConditionTC, adGenAOSDnsNotificationGroup=adGenAOSDnsNotificationGroup, adDnsTimestamp=adDnsTimestamp, adDnsNameserverInetAddress=adDnsNameserverInetAddress, adDnsIndividualResolutionFailure=adDnsIndividualResolutionFailure, adGenAOSDnsCompliances=adGenAOSDnsCompliances, adGenAOSDnsInfoGroup=adGenAOSDnsInfoGroup, adDnsNameserverInetAddressType=adDnsNameserverInetAddressType, AdDnsResourceRecordTypeTC=AdDnsResourceRecordTypeTC, adGenAOSDns=adGenAOSDns, PYSNMP_MODULE_ID=adGenAOSDns, adDnsTraps=adDnsTraps)
