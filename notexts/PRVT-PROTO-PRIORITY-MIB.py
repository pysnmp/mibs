#
# PySNMP MIB module PRVT-PROTO-PRIORITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-PROTO-PRIORITY-MIB
# Produced by pysmi-1.1.0 at Tue Nov 16 11:56:31 2021
# On host fv-az121-894 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, TimeTicks, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "TimeTicks", "ObjectIdentity", "ModuleIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
prvtProtoPriorityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 182))
prvtProtoPriorityMIB.setRevisions(('2014-02-03 00:00',))
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setLastUpdated('201402030000Z')
if mibBuilder.loadTexts: prvtProtoPriorityMIB.setOrganization('BATM Advanced Communication')
prvtProtoPriorityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1))
dscpRemarkingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1), )
if mibBuilder.loadTexts: dscpRemarkingTable.setStatus('current')
dscpRemarkingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1), ).setIndexNames((0, "PRVT-PROTO-PRIORITY-MIB", "dscpRemarkingValue"))
if mibBuilder.loadTexts: dscpRemarkingEntry.setStatus('current')
dscpRemarkingValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: dscpRemarkingValue.setStatus('current')
dscpRemarkingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dscpRemarkingRowStatus.setStatus('current')
dscpRemarkingFc = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("be", 1), ("l2", 2), ("af", 3), ("l1", 4), ("h2", 5), ("ef", 6), ("h1", 7), ("nc", 8)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dscpRemarkingFc.setStatus('current')
prvtArpPriorityMappingToFc = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 5, 182, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("be", 1), ("l2", 2), ("af", 3), ("l1", 4), ("h2", 5), ("ef", 6), ("h1", 7), ("nc", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtArpPriorityMappingToFc.setStatus('current')
mibBuilder.exportSymbols("PRVT-PROTO-PRIORITY-MIB", dscpRemarkingValue=dscpRemarkingValue, prvtProtoPriorityMIB=prvtProtoPriorityMIB, prvtProtoPriorityMIBObjects=prvtProtoPriorityMIBObjects, prvtArpPriorityMappingToFc=prvtArpPriorityMappingToFc, dscpRemarkingFc=dscpRemarkingFc, dscpRemarkingEntry=dscpRemarkingEntry, dscpRemarkingTable=dscpRemarkingTable, PYSNMP_MODULE_ID=prvtProtoPriorityMIB, dscpRemarkingRowStatus=dscpRemarkingRowStatus)
