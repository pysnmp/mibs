#
# PySNMP MIB module STORMSHIELD-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTOUPDATE-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:28:24 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, IpAddress, NotificationType, iso, Counter64, TimeTicks, Integer32, Bits, MibIdentifier, ModuleIdentity, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "iso", "Counter64", "TimeTicks", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsAutoupdate = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 9))
snsAutoupdate.setRevisions(('2017-02-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snsAutoupdate.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: snsAutoupdate.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsAutoupdate.setOrganization('Stormshield')
if mibBuilder.loadTexts: snsAutoupdate.setContactInfo('Customer Support\n\n         22 rue du Gouverneur General Eboue\n         92130 Issy-les-Moulineaux\n         FRANCE\n\n         Tel: +33 (0)9 69 32 96 29\n         E-mail: support@stormshield.eu\n         http://www.stormshield.eu')
if mibBuilder.loadTexts: snsAutoupdate.setDescription('stormshield autoupdate')
snsAutoupdateTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1), )
if mibBuilder.loadTexts: snsAutoupdateTable.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateTable.setDescription('State of autoupdate subsystems')
snsAutoupdateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1), ).setIndexNames((0, "STORMSHIELD-AUTOUPDATE-MIB", "snsAutoupdateIndex"))
if mibBuilder.loadTexts: snsAutoupdateEntry.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateEntry.setDescription('Each entry in the snsAutoupdateTable holds a set of information\n         (subsystem, state, last run).')
snsAutoupdateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateIndex.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateIndex.setDescription('A unique value for the table.  Its value\n         ranges between 1 and 65535 and may not be contigous.\n         the index has no other meaning but a pure index')
snsAutoupdateSubsys = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateSubsys.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateSubsys.setDescription('Subsystem name')
snsAutoupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateState.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateState.setDescription('state of the update of a subsystem')
snsAutoupdateLast = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateLast.setStatus('current')
if mibBuilder.loadTexts: snsAutoupdateLast.setDescription('Date of the last update of a subsystem')
mibBuilder.exportSymbols("STORMSHIELD-AUTOUPDATE-MIB", PYSNMP_MODULE_ID=snsAutoupdate, snsAutoupdateState=snsAutoupdateState, snsAutoupdateLast=snsAutoupdateLast, snsAutoupdateEntry=snsAutoupdateEntry, snsAutoupdateSubsys=snsAutoupdateSubsys, snsAutoupdate=snsAutoupdate, snsAutoupdateIndex=snsAutoupdateIndex, snsAutoupdateTable=snsAutoupdateTable)
