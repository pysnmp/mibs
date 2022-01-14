#
# PySNMP MIB module ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:55:52 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
softentIND1Aip, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Aip")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, ObjectIdentity, IpAddress, NotificationType, Bits, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "iso")
TextualConvention, DisplayString, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "MacAddress", "TruthValue")
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
mibBuilder.exportSymbols("ALCATEL-IND1-INTERSWITCH-PROTOCOL-MIB", alcatelIND1InterswitchProtocolMIBCompliances=alcatelIND1InterswitchProtocolMIBCompliances, aipLLDPConfigManAddrTable=aipLLDPConfigManAddrTable, aipLLDPConfGroup=aipLLDPConfGroup, aipLLDPConfigManAddrEntry=aipLLDPConfigManAddrEntry, alcatelIND1InterswitchProtocolMIBConformance=alcatelIND1InterswitchProtocolMIBConformance, alcatelIND1InterswitchProtocolMIBCompliance=alcatelIND1InterswitchProtocolMIBCompliance, alcatelIND1InterswitchProtocolMIBNotifications=alcatelIND1InterswitchProtocolMIBNotifications, aipLLDPConfigManAddrTlvTxEnable=aipLLDPConfigManAddrTlvTxEnable, alcatelIND1InterswitchProtocolMIBGroups=alcatelIND1InterswitchProtocolMIBGroups, aipLLDPConfigManAddrPortNum=aipLLDPConfigManAddrPortNum, aipLLDPConfig=aipLLDPConfig, alcatelIND1InterswitchProtocolMIBObjects=alcatelIND1InterswitchProtocolMIBObjects, PYSNMP_MODULE_ID=alcatelIND1InterswitchProtocolMIB, alcatelIND1InterswitchProtocolMIB=alcatelIND1InterswitchProtocolMIB, aipLLDPConfigNearestEdgeEnable=aipLLDPConfigNearestEdgeEnable)
