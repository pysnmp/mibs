#
# PySNMP MIB module CISCO-NAT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-NAT-EXT-MIB
# Source digest sha256:0ef8613727068e9710b6bd1b5e5057a954bbc5e3a8b73ab685009bedccce622c
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNATExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 532))
ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))
if mibBuilder.loadTexts: ciscoNATExtMIB.setLastUpdated('2006-06-05 00:00')
if mibBuilder.loadTexts: ciscoNATExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoNatExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 0))
ciscoNatExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 1))
ciscoNatExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2))
cneAddrTranslationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setStatus('current')
cneAddrTranslationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setStatus('current')
cneAddrTranslationNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1), Gauge32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setStatus('current')
cneAddrTranslationNumPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2), Unsigned32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setStatus('current')
cneAddrTranslation1min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation1min.setStatus('current')
cneAddrTranslation5min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation5min.setStatus('current')
ciscoNatExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1))
ciscoNatExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2))
ciscoNatExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)).setObjects(("CISCO-NAT-EXT-MIB", "ciscoNatExtAddrTransStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtMIBCompliance = ciscoNatExtMIBCompliance.setStatus('current')
ciscoNatExtAddrTransStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)).setObjects(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtAddrTransStatsGroup = ciscoNatExtAddrTransStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NAT-EXT-MIB", PYSNMP_MODULE_ID=ciscoNATExtMIB, ciscoNATExtMIB=ciscoNATExtMIB, ciscoNatExtAddrTransStatsGroup=ciscoNatExtAddrTransStatsGroup, ciscoNatExtMIBCompliance=ciscoNatExtMIBCompliance, ciscoNatExtMIBCompliances=ciscoNatExtMIBCompliances, ciscoNatExtMIBConformance=ciscoNatExtMIBConformance, ciscoNatExtMIBGroups=ciscoNatExtMIBGroups, ciscoNatExtMIBNotifs=ciscoNatExtMIBNotifs, ciscoNatExtMIBObjects=ciscoNatExtMIBObjects, cneAddrTranslation1min=cneAddrTranslation1min, cneAddrTranslation5min=cneAddrTranslation5min, cneAddrTranslationNumActive=cneAddrTranslationNumActive, cneAddrTranslationNumPeak=cneAddrTranslationNumPeak, cneAddrTranslationStatsEntry=cneAddrTranslationStatsEntry, cneAddrTranslationStatsTable=cneAddrTranslationStatsTable)
