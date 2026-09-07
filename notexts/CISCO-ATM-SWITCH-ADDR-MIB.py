#
# PySNMP MIB module CISCO-ATM-SWITCH-ADDR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-SWITCH-ADDR-MIB
# Source digest sha256:24032e0e242379c20e945d0430b801f40aebe9d278867f9c22c05d5536e912dd
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoAtmSwAddrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 51))
ciscoAtmSwAddrMIB.setRevisions(('1996-01-10 00:00',))
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setLastUpdated('1996-01-10 00:00')
if mibBuilder.loadTexts: ciscoAtmSwAddrMIB.setOrganization('Cisco Systems, Inc.')
ciscoAtmSwAddrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 1))
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(13, 13), ValueSizeConstraint(20, 20), )
ciscoAtmSwAddrTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmSwAddrTable.setStatus('current')
ciscoAtmSwAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrIndex"))
if mibBuilder.loadTexts: ciscoAtmSwAddrEntry.setStatus('current')
ciscoAtmSwAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: ciscoAtmSwAddrIndex.setStatus('current')
ciscoAtmSwAddrAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrAddress.setStatus('current')
ciscoAtmSwAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ciscoAtmSwAddrRowStatus.setStatus('current')
ciscoAtmSwAddrMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3))
ciscoAtmSwAddrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1))
ciscoAtmSwAddrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2))
ciscoAtmSwAddrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBCompliance = ciscoAtmSwAddrMIBCompliance.setStatus('current')
ciscoAtmSwAddrMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1)).setObjects(("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrAddress"), ("CISCO-ATM-SWITCH-ADDR-MIB", "ciscoAtmSwAddrRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmSwAddrMIBGroup = ciscoAtmSwAddrMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-SWITCH-ADDR-MIB", AtmAddr=AtmAddr, PYSNMP_MODULE_ID=ciscoAtmSwAddrMIB, ciscoAtmSwAddrAddress=ciscoAtmSwAddrAddress, ciscoAtmSwAddrEntry=ciscoAtmSwAddrEntry, ciscoAtmSwAddrIndex=ciscoAtmSwAddrIndex, ciscoAtmSwAddrMIB=ciscoAtmSwAddrMIB, ciscoAtmSwAddrMIBCompliance=ciscoAtmSwAddrMIBCompliance, ciscoAtmSwAddrMIBCompliances=ciscoAtmSwAddrMIBCompliances, ciscoAtmSwAddrMIBConformance=ciscoAtmSwAddrMIBConformance, ciscoAtmSwAddrMIBGroup=ciscoAtmSwAddrMIBGroup, ciscoAtmSwAddrMIBGroups=ciscoAtmSwAddrMIBGroups, ciscoAtmSwAddrMIBObjects=ciscoAtmSwAddrMIBObjects, ciscoAtmSwAddrRowStatus=ciscoAtmSwAddrRowStatus, ciscoAtmSwAddrTable=ciscoAtmSwAddrTable)
