#
# PySNMP MIB module CISCO-BGP-POLICY-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-BGP-POLICY-ACCOUNTING-MIB
# Source digest sha256:f7a56dcd396d0c53a404bb04c57ec5f96969481ea7800e8c51d4dc07490d31a6
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 148))
ciscoBgpPolAcctMIB.setRevisions(('2002-07-26 00:00', '1999-12-17 00:00',))
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setLastUpdated('2002-07-26 00:00')
if mibBuilder.loadTexts: ciscoBgpPolAcctMIB.setOrganization('Cisco Systems, Inc.')
ciscoBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 1))
cbpAcctTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cbpAcctTable.setStatus('current')
cbpAcctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"))
if mibBuilder.loadTexts: cbpAcctEntry.setStatus('current')
cbpAcctTrafficIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctTrafficIndex.setStatus('current')
cbpAcctInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInPacketCount.setStatus('current')
cbpAcctInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctInOctetCount.setStatus('current')
cbpAcctOutPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutPacketCount.setStatus('current')
cbpAcctOutOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 148, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbpAcctOutOctetCount.setStatus('current')
ciscoBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3))
ciscoBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1))
ciscoBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2))
ciscoBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBCompliance = ciscoBgpPolAcctMIBCompliance.setStatus('deprecated')
ciscoBgpPolAcctMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 1, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTableGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBgpPolAcctMIBComplianceRev1 = ciscoBgpPolAcctMIBComplianceRev1.setStatus('current')
cbpAcctTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 1)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroup = cbpAcctTableGroup.setStatus('deprecated')
cbpAcctTableGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 148, 3, 2, 2)).setObjects(("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctTrafficIndex"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctInOctetCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutPacketCount"), ("CISCO-BGP-POLICY-ACCOUNTING-MIB", "cbpAcctOutOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cbpAcctTableGroupRev1 = cbpAcctTableGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-BGP-POLICY-ACCOUNTING-MIB", PYSNMP_MODULE_ID=ciscoBgpPolAcctMIB, cbpAcctEntry=cbpAcctEntry, cbpAcctInOctetCount=cbpAcctInOctetCount, cbpAcctInPacketCount=cbpAcctInPacketCount, cbpAcctOutOctetCount=cbpAcctOutOctetCount, cbpAcctOutPacketCount=cbpAcctOutPacketCount, cbpAcctTable=cbpAcctTable, cbpAcctTableGroup=cbpAcctTableGroup, cbpAcctTableGroupRev1=cbpAcctTableGroupRev1, cbpAcctTrafficIndex=cbpAcctTrafficIndex, ciscoBgpPolAcctMIB=ciscoBgpPolAcctMIB, ciscoBgpPolAcctMIBCompliance=ciscoBgpPolAcctMIBCompliance, ciscoBgpPolAcctMIBComplianceRev1=ciscoBgpPolAcctMIBComplianceRev1, ciscoBgpPolAcctMIBCompliances=ciscoBgpPolAcctMIBCompliances, ciscoBgpPolAcctMIBConformance=ciscoBgpPolAcctMIBConformance, ciscoBgpPolAcctMIBGroups=ciscoBgpPolAcctMIBGroups, ciscoBgpPolAcctMIBObjects=ciscoBgpPolAcctMIBObjects)
