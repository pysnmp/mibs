#
# PySNMP MIB module ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.1.8 at Tue Jan 11 21:37:16 2022
# On host fv-az74-997 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
softentIND1Aip, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Aip")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, IpAddress, Bits, iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, MibIdentifier, Counter32, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "Bits", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "MibIdentifier", "Counter32", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, TruthValue, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "MacAddress", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", aipLLDPConfigManAddrTlvTxEnable=aipLLDPConfigManAddrTlvTxEnable, aipLLDPConfigManAddrEntry=aipLLDPConfigManAddrEntry, alcatelIND1InterswitchProtocolMIBNotifications=alcatelIND1InterswitchProtocolMIBNotifications, alcatelIND1InterswitchProtocolMIBObjects=alcatelIND1InterswitchProtocolMIBObjects, aipLLDPConfigNearestEdgeEnable=aipLLDPConfigNearestEdgeEnable, alcatelIND1InterswitchProtocolMIBConformance=alcatelIND1InterswitchProtocolMIBConformance, aipLLDPConfGroup=aipLLDPConfGroup, aipLLDPConfigManAddrTable=aipLLDPConfigManAddrTable, alcatelIND1InterswitchProtocolMIBCompliance=alcatelIND1InterswitchProtocolMIBCompliance, alcatelIND1InterswitchProtocolMIB=alcatelIND1InterswitchProtocolMIB, aipLLDPConfig=aipLLDPConfig, alcatelIND1InterswitchProtocolMIBCompliances=alcatelIND1InterswitchProtocolMIBCompliances, PYSNMP_MODULE_ID=alcatelIND1InterswitchProtocolMIB, alcatelIND1InterswitchProtocolMIBGroups=alcatelIND1InterswitchProtocolMIBGroups, aipLLDPConfigManAddrPortNum=aipLLDPConfigManAddrPortNum)
