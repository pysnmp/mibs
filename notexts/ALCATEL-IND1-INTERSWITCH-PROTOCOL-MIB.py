#
# PySNMP MIB module ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:33:21 2022
# On host fv-az42-180 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1Aip, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Aip")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, Integer32, TimeTicks, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, Counter64, Unsigned32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Integer32", "TimeTicks", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier")
TruthValue, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "MacAddress")
alcatelIND1InterswitchProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1))
alcatelIND1InterswitchProtocolMIB.setRevisions(('2010-05-13 00:00', '2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setLastUpdated('201005130000Z')
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIB.setOrganization('Alcatel-Lucent')
alcatelIND1InterswitchProtocolMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 0))
if mibBuilder.loadTexts: alcatelIND1InterswitchProtocolMIBNotifications.setStatus('current')
alcatelIND1InterswitchProtocolMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1))
aipLLDPConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1))
alcatelIND1InterswitchProtocolMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2))
aipLLDPConfigManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1), )
if mibBuilder.loadTexts: aipLLDPConfigManAddrTable.setStatus('current')
aipLLDPConfigManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1), ).setIndexNames((0, "ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrPortNum"))
if mibBuilder.loadTexts: aipLLDPConfigManAddrEntry.setStatus('current')
aipLLDPConfigManAddrPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: aipLLDPConfigManAddrPortNum.setStatus('current')
aipLLDPConfigManAddrTlvTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aipLLDPConfigManAddrTlvTxEnable.setStatus('current')
aipLLDPConfigNearestEdgeEnable = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aipLLDPConfigNearestEdgeEnable.setStatus('current')
alcatelIND1InterswitchProtocolMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1))
alcatelIND1InterswitchProtocolMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2))
aipLLDPConfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigManAddrTlvTxEnable"), ("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfigNearestEdgeEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aipLLDPConfGroup = aipLLDPConfGroup.setStatus('current')
alcatelIND1InterswitchProtocolMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 9, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", "aipLLDPConfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1InterswitchProtocolMIBCompliance = alcatelIND1InterswitchProtocolMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", alcatelIND1InterswitchProtocolMIBGroups=alcatelIND1InterswitchProtocolMIBGroups, aipLLDPConfigManAddrEntry=aipLLDPConfigManAddrEntry, alcatelIND1InterswitchProtocolMIBNotifications=alcatelIND1InterswitchProtocolMIBNotifications, alcatelIND1InterswitchProtocolMIBCompliance=alcatelIND1InterswitchProtocolMIBCompliance, aipLLDPConfigNearestEdgeEnable=aipLLDPConfigNearestEdgeEnable, PYSNMP_MODULE_ID=alcatelIND1InterswitchProtocolMIB, alcatelIND1InterswitchProtocolMIBCompliances=alcatelIND1InterswitchProtocolMIBCompliances, aipLLDPConfig=aipLLDPConfig, alcatelIND1InterswitchProtocolMIBObjects=alcatelIND1InterswitchProtocolMIBObjects, aipLLDPConfigManAddrPortNum=aipLLDPConfigManAddrPortNum, alcatelIND1InterswitchProtocolMIB=alcatelIND1InterswitchProtocolMIB, alcatelIND1InterswitchProtocolMIBConformance=alcatelIND1InterswitchProtocolMIBConformance, aipLLDPConfigManAddrTable=aipLLDPConfigManAddrTable, aipLLDPConfGroup=aipLLDPConfGroup, aipLLDPConfigManAddrTlvTxEnable=aipLLDPConfigManAddrTlvTxEnable)
