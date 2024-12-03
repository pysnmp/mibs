#
# PySNMP MIB module ARISTA-GENERAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-GENERAL-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:37:05 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Counter64, NotificationType, IpAddress, ObjectIdentity, Bits, Integer32, TimeTicks, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Counter64", "NotificationType", "IpAddress", "ObjectIdentity", "Bits", "Integer32", "TimeTicks", "iso", "MibIdentifier")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ARISTA-GENERAL-MIB", aristaGeneralMibCompliances=aristaGeneralMibCompliances, aristaGeneralMibNotifications=aristaGeneralMibNotifications, aristaReloadIndex=aristaReloadIndex, aristaReloadUnitIndex=aristaReloadUnitIndex, aristaGeneralMibGroups=aristaGeneralMibGroups, aristaReloadCauseTable=aristaReloadCauseTable, aristaReloadCauseIndex=aristaReloadCauseIndex, aristaReloadTime=aristaReloadTime, aristaGeneralMibConformance=aristaGeneralMibConformance, aristaReloadCauseDescription=aristaReloadCauseDescription, aristaGeneralMibGroup=aristaGeneralMibGroup, aristaGeneralMibObjects=aristaGeneralMibObjects, aristaReloadCauseEntry=aristaReloadCauseEntry, PYSNMP_MODULE_ID=aristaGeneralMib, aristaGeneralMibCompliance=aristaGeneralMibCompliance, aristaGeneralMib=aristaGeneralMib)
