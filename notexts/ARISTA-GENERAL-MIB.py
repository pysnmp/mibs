#
# PySNMP MIB module ARISTA-GENERAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-GENERAL-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:28:05 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, MibIdentifier, ObjectIdentity, Gauge32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, Unsigned32, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "ObjectIdentity", "Gauge32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "Unsigned32", "Counter32", "ModuleIdentity", "Counter64")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
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
mibBuilder.exportSymbols("ARISTA-GENERAL-MIB", aristaReloadUnitIndex=aristaReloadUnitIndex, aristaReloadCauseEntry=aristaReloadCauseEntry, aristaReloadCauseIndex=aristaReloadCauseIndex, aristaReloadTime=aristaReloadTime, aristaGeneralMibCompliances=aristaGeneralMibCompliances, aristaGeneralMibCompliance=aristaGeneralMibCompliance, PYSNMP_MODULE_ID=aristaGeneralMib, aristaReloadCauseTable=aristaReloadCauseTable, aristaGeneralMibGroup=aristaGeneralMibGroup, aristaGeneralMib=aristaGeneralMib, aristaGeneralMibGroups=aristaGeneralMibGroups, aristaGeneralMibConformance=aristaGeneralMibConformance, aristaGeneralMibNotifications=aristaGeneralMibNotifications, aristaGeneralMibObjects=aristaGeneralMibObjects, aristaReloadCauseDescription=aristaReloadCauseDescription, aristaReloadIndex=aristaReloadIndex)
