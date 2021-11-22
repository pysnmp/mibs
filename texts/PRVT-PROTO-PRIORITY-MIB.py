#
# PySNMP MIB module PRVT-PROTO-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-PROTO-PRIORITY-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 11:54:27 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter64, Unsigned32, NotificationType, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "Unsigned32", "NotificationType", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "iso", "TimeTicks")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
prvtProtoPriorityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 182))
prvtProtoPriorityMIB.setRevisions(('2014-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtProtoPriorityMIB.setRevisionsDescriptions(('Initial implementation',))
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setLastUpdated('201402030000Z')
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setDescription('This document is the SNMP MIB module to manage dscp remarking.')
prvtProtoPriorityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1))
dscpRemarkingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1), )
if mibBuilder.loadTexts: dscpRemarkingTable.setStatus('current')
if mibBuilder.loadTexts: dscpRemarkingTable.setDescription('A table that contains dscpRemarking information.')
dscpRemarkingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1), ).setIndexNames((0, "PRVT-PROTO-PRIORITY-MIB", "dscpRemarkingValue"))
if mibBuilder.loadTexts: dscpRemarkingEntry.setStatus('current')
if mibBuilder.loadTexts: dscpRemarkingEntry.setDescription('Information about a specific dscpRemarking.')
dscpRemarkingValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: dscpRemarkingValue.setStatus('current')
if mibBuilder.loadTexts: dscpRemarkingValue.setDescription('Specify DSCP value to be remarked.')
dscpRemarkingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dscpRemarkingRowStatus.setStatus('current')
if mibBuilder.loadTexts: dscpRemarkingRowStatus.setDescription('This object indicates the status of this row.')
dscpRemarkingFc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("be", 1), ("l2", 2), ("af", 3), ("l1", 4), ("h2", 5), ("ef", 6), ("h1", 7), ("nc", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dscpRemarkingFc.setStatus('current')
if mibBuilder.loadTexts: dscpRemarkingFc.setDescription('Forwarding class.')
prvtArpPriorityMappingToFc = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("be", 1), ("l2", 2), ("af", 3), ("l1", 4), ("h2", 5), ("ef", 6), ("h1", 7), ("nc", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtArpPriorityMappingToFc.setStatus('current')
if mibBuilder.loadTexts: prvtArpPriorityMappingToFc.setDescription('Specify ARP packets mapping\n         to forwarding class')
mibBuilder.exportSymbols("PRVT-PROTO-PRIORITY-MIB", dscpRemarkingValue=dscpRemarkingValue, prvtProtoPriorityMIBObjects=prvtProtoPriorityMIBObjects, PYSNMP_MODULE_ID=prvtProtoPriorityMIB, dscpRemarkingEntry=dscpRemarkingEntry, dscpRemarkingFc=dscpRemarkingFc, dscpRemarkingRowStatus=dscpRemarkingRowStatus, prvtProtoPriorityMIB=prvtProtoPriorityMIB, prvtArpPriorityMappingToFc=prvtArpPriorityMappingToFc, dscpRemarkingTable=dscpRemarkingTable)
