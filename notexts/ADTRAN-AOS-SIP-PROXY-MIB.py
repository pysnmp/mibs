#
# PySNMP MIB module ADTRAN-AOS-SIP-PROXY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-SIP-PROXY-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:10:42 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
adGenAOSVoice, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSVoice", "adGenAOSConformance")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Counter32, Bits, Counter64, ModuleIdentity, Gauge32, ObjectIdentity, MibIdentifier, TimeTicks, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Counter32", "Bits", "Counter64", "ModuleIdentity", "Gauge32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "NotificationType", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipProxy = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 5))
adGenAOSSipProxy.setRevisions(('2013-05-16 00:00',))
if mibBuilder.loadTexts: adGenAOSSipProxy.setLastUpdated('201305160000Z')
if mibBuilder.loadTexts: adGenAOSSipProxy.setOrganization('ADTRAN, Inc.')
adSipProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5))
adSipProxyTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0))
adProxyTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 1), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyTimestamp.setStatus('current')
adProxyRolloverFromServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 2), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddressType.setStatus('current')
adProxyRolloverFromServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 3), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverFromServerInetAddress.setStatus('current')
adProxyRolloverToServerInetAddressType = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 4), InetAddressType()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddressType.setStatus('current')
adProxyRolloverToServerInetAddress = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 5), InetAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverToServerInetAddress.setStatus('current')
class AdProxyRolloverCauseTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("transactionFailed", 1), ("pollFailed", 2), ("pollSucceeded", 3))

adProxyRolloverCause = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 6), AdProxyRolloverCauseTC()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adProxyRolloverCause.setStatus('current')
adSipProxyRollover = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 5, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if mibBuilder.loadTexts: adSipProxyRollover.setStatus('current')
adSipProxyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14))
adSipProxyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1))
adSipProxyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2))
adSipProxyFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 2, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyFullCompliance = adSipProxyFullCompliance.setStatus('current')
adSipProxyNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 1)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adSipProxyRollover"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationGroup = adSipProxyNotificationGroup.setStatus('current')
adSipProxyNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 14, 1, 2)).setObjects(("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyTimestamp"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverFromServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddressType"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverToServerInetAddress"), ("ADTRAN-AOS-SIP-PROXY-MIB", "adProxyRolloverCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipProxyNotificationUtilityGroup = adSipProxyNotificationUtilityGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-PROXY-MIB", adSipProxyCompliances=adSipProxyCompliances, adSipProxyGroups=adSipProxyGroups, adProxyRolloverFromServerInetAddressType=adProxyRolloverFromServerInetAddressType, adProxyRolloverToServerInetAddress=adProxyRolloverToServerInetAddress, adSipProxyNotificationUtilityGroup=adSipProxyNotificationUtilityGroup, adSipProxyTraps=adSipProxyTraps, adSipProxyConformance=adSipProxyConformance, adSipProxyRollover=adSipProxyRollover, AdProxyRolloverCauseTC=AdProxyRolloverCauseTC, adProxyRolloverFromServerInetAddress=adProxyRolloverFromServerInetAddress, adSipProxyNotificationGroup=adSipProxyNotificationGroup, adSipProxyFullCompliance=adSipProxyFullCompliance, PYSNMP_MODULE_ID=adGenAOSSipProxy, adProxyRolloverToServerInetAddressType=adProxyRolloverToServerInetAddressType, adGenAOSSipProxy=adGenAOSSipProxy, adSipProxy=adSipProxy, adProxyTimestamp=adProxyTimestamp, adProxyRolloverCause=adProxyRolloverCause)
