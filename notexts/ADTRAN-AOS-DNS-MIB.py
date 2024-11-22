#
# PySNMP MIB module ADTRAN-AOS-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DNS-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 11:51:40 2024
# On host fv-az665-602 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
adGenAOSConformance, adGenAOSApplications = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSApplications")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter64, ObjectIdentity, NotificationType, Unsigned32, Counter32, Bits, Integer32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter32", "Bits", "Integer32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSDns = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1))
adGenAOSDns.setRevisions(('2012-04-30 00:00',))
if mibBuilder.loadTexts: adGenAOSDns.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: adGenAOSDns.setOrganization('ADTRAN, Inc.')
adDnsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0))
adDnsTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsTimestamp.setStatus('current')
adDnsNameserverInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsNameserverInetAddressType.setStatus('current')
adDnsNameserverInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsNameserverInetAddress.setStatus('current')
class AdDnsRequestErrorConditionTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("noError", 0), ("formatError", 1), ("serverFailure", 2), ("nameError", 3), ("notImplemented", 4), ("refused", 5), ("unsuportedRCode", 16), ("malformedResponse", 17), ("parseError", 18), ("timeoutWaitingForResponse", 19), ("emptyResponse", 20), ("unsupportedType", 21), ("onlyRootAnswer", 22), ("portDeficiency", 23), ("noServerCOnfigured", 24), ("udpSendError", 25))

adDnsRequestErrorCondition = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 4), AdDnsRequestErrorConditionTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsRequestErrorCondition.setStatus('current')
adDnsDomainName = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsDomainName.setStatus('current')
class AdDnsResourceRecordTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 28, 33, 65537))
    namedValues = NamedValues(("a", 1), ("ns", 2), ("md", 3), ("mf", 4), ("cname", 5), ("soa", 6), ("mb", 7), ("mg", 8), ("mr", 9), ("null", 10), ("wks", 11), ("ptr", 12), ("hinfo", 13), ("minfo", 14), ("mx", 15), ("txt", 16), ("aaaa", 28), ("srv", 33), ("aplusaaaa", 65537))

adDnsResourceRecordType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 6), AdDnsResourceRecordTypeTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adDnsResourceRecordType.setStatus('current')
adDnsIndividualResolutionFailure = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 8, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"), ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"), ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"), ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
if mibBuilder.loadTexts: adDnsIndividualResolutionFailure.setStatus('current')
adGenAOSDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13))
adGenAOSDnsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1))
adGenAOSDnsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2))
adGenAOSDnsFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 2, 1)).setObjects(("ADTRAN-AOS-DNS-MIB", "adGenAOSDnsInfoGroup"), ("ADTRAN-AOS-DNS-MIB", "adGenAOSDnsNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsFullCompliance = adGenAOSDnsFullCompliance.setStatus('current')
adGenAOSDnsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 1)).setObjects(("ADTRAN-AOS-DNS-MIB", "adDnsTimestamp"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddressType"), ("ADTRAN-AOS-DNS-MIB", "adDnsNameserverInetAddress"), ("ADTRAN-AOS-DNS-MIB", "adDnsRequestErrorCondition"), ("ADTRAN-AOS-DNS-MIB", "adDnsDomainName"), ("ADTRAN-AOS-DNS-MIB", "adDnsResourceRecordType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsInfoGroup = adGenAOSDnsInfoGroup.setStatus('current')
adGenAOSDnsNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 13, 1, 2)).setObjects(("ADTRAN-AOS-DNS-MIB", "adDnsIndividualResolutionFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDnsNotificationGroup = adGenAOSDnsNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-DNS-MIB", adGenAOSDnsFullCompliance=adGenAOSDnsFullCompliance, adDnsNameserverInetAddressType=adDnsNameserverInetAddressType, AdDnsRequestErrorConditionTC=AdDnsRequestErrorConditionTC, PYSNMP_MODULE_ID=adGenAOSDns, adDnsTraps=adDnsTraps, adGenAOSDns=adGenAOSDns, adDnsResourceRecordType=adDnsResourceRecordType, adDnsIndividualResolutionFailure=adDnsIndividualResolutionFailure, adGenAOSDnsCompliances=adGenAOSDnsCompliances, adDnsNameserverInetAddress=adDnsNameserverInetAddress, adDnsRequestErrorCondition=adDnsRequestErrorCondition, adGenAOSDnsConformance=adGenAOSDnsConformance, adDnsTimestamp=adDnsTimestamp, adGenAOSDnsGroup=adGenAOSDnsGroup, adGenAOSDnsNotificationGroup=adGenAOSDnsNotificationGroup, AdDnsResourceRecordTypeTC=AdDnsResourceRecordTypeTC, adDnsDomainName=adDnsDomainName, adGenAOSDnsInfoGroup=adGenAOSDnsInfoGroup)
