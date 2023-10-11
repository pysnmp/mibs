#
# PySNMP MIB module ARISTA-GENERAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-GENERAL-MIB
# Produced by pysmi-1.1.8 at Wed Oct 11 11:20:01 2023
# On host fv-az456-991 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Unsigned32, Counter32, NotificationType, iso, TimeTicks, Bits, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter32", "NotificationType", "iso", "TimeTicks", "Bits", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ModuleIdentity", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
aristaGeneralMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 24))
aristaGeneralMib.setRevisions(('2017-11-06 00:00',))
if mibBuilder.loadTexts: aristaGeneralMib.setLastUpdated('201711060000Z')
if mibBuilder.loadTexts: aristaGeneralMib.setOrganization('Arista Networks, Inc.')
aristaGeneralMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 0))
aristaGeneralMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1))
aristaGeneralMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2))
aristaReloadCauseTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1), )
if mibBuilder.loadTexts: aristaReloadCauseTable.setStatus('current')
aristaReloadCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1), ).setIndexNames((0, "ARISTA-GENERAL-MIB", "aristaReloadUnitIndex"), (0, "ARISTA-GENERAL-MIB", "aristaReloadIndex"), (0, "ARISTA-GENERAL-MIB", "aristaReloadCauseIndex"))
if mibBuilder.loadTexts: aristaReloadCauseEntry.setStatus('current')
aristaReloadUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaReloadUnitIndex.setStatus('current')
aristaReloadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: aristaReloadIndex.setStatus('current')
aristaReloadCauseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: aristaReloadCauseIndex.setStatus('current')
aristaReloadCauseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaReloadCauseDescription.setStatus('current')
aristaReloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaReloadTime.setStatus('current')
aristaGeneralMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1))
aristaGeneralMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2))
aristaGeneralMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1, 1)).setObjects(("ARISTA-GENERAL-MIB", "aristaGeneralMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaGeneralMibCompliance = aristaGeneralMibCompliance.setStatus('current')
aristaGeneralMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2, 1)).setObjects(("ARISTA-GENERAL-MIB", "aristaReloadCauseDescription"), ("ARISTA-GENERAL-MIB", "aristaReloadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaGeneralMibGroup = aristaGeneralMibGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-GENERAL-MIB", aristaGeneralMibObjects=aristaGeneralMibObjects, aristaReloadIndex=aristaReloadIndex, aristaReloadCauseDescription=aristaReloadCauseDescription, PYSNMP_MODULE_ID=aristaGeneralMib, aristaGeneralMibCompliances=aristaGeneralMibCompliances, aristaGeneralMibGroups=aristaGeneralMibGroups, aristaGeneralMibCompliance=aristaGeneralMibCompliance, aristaReloadTime=aristaReloadTime, aristaGeneralMibNotifications=aristaGeneralMibNotifications, aristaGeneralMib=aristaGeneralMib, aristaGeneralMibGroup=aristaGeneralMibGroup, aristaReloadCauseEntry=aristaReloadCauseEntry, aristaGeneralMibConformance=aristaGeneralMibConformance, aristaReloadCauseIndex=aristaReloadCauseIndex, aristaReloadUnitIndex=aristaReloadUnitIndex, aristaReloadCauseTable=aristaReloadCauseTable)
