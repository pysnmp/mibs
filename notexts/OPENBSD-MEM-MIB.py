#
# PySNMP MIB module OPENBSD-MEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-MEM-MIB
# Produced by pysmi-1.1.12 at Thu May 30 02:19:41 2024
# On host fv-az775-912 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ifIndex, ifNumber = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifNumber")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, NotificationType, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter32, Counter64, MibIdentifier, Bits, Gauge32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "MibIdentifier", "Bits", "Gauge32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
memMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 5))
memMIBObjects.setRevisions(('2012-02-09 00:00', '2008-12-23 00:00',))
if mibBuilder.loadTexts: memMIBObjects.setLastUpdated('201202090000Z')
if mibBuilder.loadTexts: memMIBObjects.setOrganization('OpenBSD')
memMIBVersion = MibScalar((1, 3, 6, 1, 4, 1, 30155, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memMIBVersion.setStatus('current')
memIfTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 5, 2), )
if mibBuilder.loadTexts: memIfTable.setStatus('current')
memIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: memIfEntry.setStatus('current')
memIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfName.setStatus('current')
memIfLiveLocks = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 5, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: memIfLiveLocks.setStatus('current')
mibBuilder.exportSymbols("OPENBSD-MEM-MIB", PYSNMP_MODULE_ID=memMIBObjects, memIfTable=memIfTable, memIfName=memIfName, memMIBObjects=memMIBObjects, memIfLiveLocks=memIfLiveLocks, memIfEntry=memIfEntry, memMIBVersion=memMIBVersion)
