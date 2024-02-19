#
# PySNMP MIB module STORMSHIELD-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTOUPDATE-MIB
# Produced by pysmi-1.1.10 at Mon Feb 19 03:02:25 2024
# On host fv-az1016-227 platform Linux version 6.2.0-1019-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Gauge32, Counter32, IpAddress, ModuleIdentity, Counter64, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "Counter32", "IpAddress", "ModuleIdentity", "Counter64", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsAutoupdate = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 9))
snsAutoupdate.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsAutoupdate.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsAutoupdate.setOrganization('Stormshield')
snsAutoupdateTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1), )
if mibBuilder.loadTexts: snsAutoupdateTable.setStatus('current')
snsAutoupdateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1), ).setIndexNames((0, "STORMSHIELD-AUTOUPDATE-MIB", "snsAutoupdateIndex"))
if mibBuilder.loadTexts: snsAutoupdateEntry.setStatus('current')
snsAutoupdateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateIndex.setStatus('current')
snsAutoupdateSubsys = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateSubsys.setStatus('current')
snsAutoupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateState.setStatus('current')
snsAutoupdateLast = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 9, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsAutoupdateLast.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-AUTOUPDATE-MIB", snsAutoupdateLast=snsAutoupdateLast, PYSNMP_MODULE_ID=snsAutoupdate, snsAutoupdateState=snsAutoupdateState, snsAutoupdate=snsAutoupdate, snsAutoupdateEntry=snsAutoupdateEntry, snsAutoupdateTable=snsAutoupdateTable, snsAutoupdateSubsys=snsAutoupdateSubsys, snsAutoupdateIndex=snsAutoupdateIndex)
