#
# PySNMP MIB module STORMSHIELD-AUTOUPDATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-AUTOUPDATE-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 01:07:14 2022
# On host fv-az74-933 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, MibIdentifier, IpAddress, Bits, ModuleIdentity, iso, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "Bits", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "TimeTicks", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("STORMSHIELD-AUTOUPDATE-MIB", snsAutoupdateLast=snsAutoupdateLast, snsAutoupdateState=snsAutoupdateState, snsAutoupdateIndex=snsAutoupdateIndex, snsAutoupdateEntry=snsAutoupdateEntry, PYSNMP_MODULE_ID=snsAutoupdate, snsAutoupdateTable=snsAutoupdateTable, snsAutoupdateSubsys=snsAutoupdateSubsys, snsAutoupdate=snsAutoupdate)
