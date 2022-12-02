#
# PySNMP MIB module ARISTA-GENERAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-GENERAL-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:01:40 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, MibIdentifier, ModuleIdentity, Integer32, TimeTicks, iso, Bits, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "MibIdentifier", "ModuleIdentity", "Integer32", "TimeTicks", "iso", "Bits", "IpAddress", "Unsigned32", "Counter32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
aristaGeneralMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 24))
aristaGeneralMib.setRevisions(('2017-11-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaGeneralMib.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: aristaGeneralMib.setLastUpdated('201711060000Z')
if mibBuilder.loadTexts: aristaGeneralMib.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaGeneralMib.setContactInfo('Arista Networks, Inc.\n\n         Postal: 5453 Great America Parkway\n                 Santa Clara, CA 95054\n\n         Tel: +1 408 547-5500\n\n         E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaGeneralMib.setDescription('First draft.')
aristaGeneralMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 0))
aristaGeneralMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1))
aristaGeneralMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2))
aristaReloadCauseTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1), )
if mibBuilder.loadTexts: aristaReloadCauseTable.setStatus('current')
if mibBuilder.loadTexts: aristaReloadCauseTable.setDescription('Information describing the reload cause of each CPU unit.\n         On a modular system, entries for reboot instances of the\n         standby supervisor are present only when the redundancy\n         protocol is stateful switchover (SSO).')
aristaReloadCauseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1), ).setIndexNames((0, "ARISTA-GENERAL-MIB", "aristaReloadUnitIndex"), (0, "ARISTA-GENERAL-MIB", "aristaReloadIndex"), (0, "ARISTA-GENERAL-MIB", "aristaReloadCauseIndex"))
if mibBuilder.loadTexts: aristaReloadCauseEntry.setStatus('current')
if mibBuilder.loadTexts: aristaReloadCauseEntry.setDescription('This entry contains reload cause information of a CPU unit\n          for a particular reboot instance.')
aristaReloadUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaReloadUnitIndex.setStatus('current')
if mibBuilder.loadTexts: aristaReloadUnitIndex.setDescription('A unique identifier for a CPU unit.  On a modular system, it is\n         the slot number of the supervisor.  Unit index 0 mirrors the entries\n         of the active supervisor.  On a fixed system, unit index 0 is for\n         the whole system.')
aristaReloadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: aristaReloadIndex.setStatus('current')
if mibBuilder.loadTexts: aristaReloadIndex.setDescription('A unique key to get the particular reboot instance.  Reboot instances\n         are numbered in reverse chronological order, with the latest reboot\n         at index 0.')
aristaReloadCauseIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: aristaReloadCauseIndex.setStatus('current')
if mibBuilder.loadTexts: aristaReloadCauseIndex.setDescription('A unique key to get one of the causes of a particular reboot instance.')
aristaReloadCauseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaReloadCauseDescription.setStatus('current')
if mibBuilder.loadTexts: aristaReloadCauseDescription.setDescription('Description for the reload cause.')
aristaReloadTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 24, 1, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaReloadTime.setStatus('current')
if mibBuilder.loadTexts: aristaReloadTime.setDescription('Time when the reload happened.')
aristaGeneralMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1))
aristaGeneralMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2))
aristaGeneralMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 1, 1)).setObjects(("ARISTA-GENERAL-MIB", "aristaGeneralMibGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaGeneralMibCompliance = aristaGeneralMibCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaGeneralMibCompliance.setDescription('The compliance statement for Arista switches that support\n        the ARISTA-GENERAL-MIB.')
aristaGeneralMibGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 24, 2, 2, 1)).setObjects(("ARISTA-GENERAL-MIB", "aristaReloadCauseDescription"), ("ARISTA-GENERAL-MIB", "aristaReloadTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaGeneralMibGroup = aristaGeneralMibGroup.setStatus('current')
if mibBuilder.loadTexts: aristaGeneralMibGroup.setDescription('The collection of objects that provide reload cause\n        information for the CPU units in the system.')
mibBuilder.exportSymbols("ARISTA-GENERAL-MIB", aristaGeneralMibNotifications=aristaGeneralMibNotifications, aristaReloadCauseIndex=aristaReloadCauseIndex, aristaGeneralMibCompliance=aristaGeneralMibCompliance, aristaGeneralMibGroup=aristaGeneralMibGroup, aristaReloadTime=aristaReloadTime, aristaReloadCauseEntry=aristaReloadCauseEntry, aristaReloadCauseTable=aristaReloadCauseTable, aristaReloadCauseDescription=aristaReloadCauseDescription, aristaReloadIndex=aristaReloadIndex, aristaGeneralMibObjects=aristaGeneralMibObjects, aristaGeneralMibConformance=aristaGeneralMibConformance, aristaGeneralMib=aristaGeneralMib, aristaGeneralMibCompliances=aristaGeneralMibCompliances, PYSNMP_MODULE_ID=aristaGeneralMib, aristaGeneralMibGroups=aristaGeneralMibGroups, aristaReloadUnitIndex=aristaReloadUnitIndex)
