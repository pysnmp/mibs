#
# PySNMP MIB module STORMSHIELD-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTOUPDATE-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 18:30:54 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Gauge32, IpAddress, Counter64, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "IpAddress", "Counter64", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STORMSHIELD-AUTOUPDATE-MIB", snsAutoupdateTable=snsAutoupdateTable, PYSNMP_MODULE_ID=snsAutoupdate, snsAutoupdateSubsys=snsAutoupdateSubsys, snsAutoupdate=snsAutoupdate, snsAutoupdateIndex=snsAutoupdateIndex, snsAutoupdateLast=snsAutoupdateLast, snsAutoupdateEntry=snsAutoupdateEntry, snsAutoupdateState=snsAutoupdateState)
