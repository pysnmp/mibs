#
# PySNMP MIB module OPENBSD-MEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-MEM-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:37:46 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ifNumber, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifIndex")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter64, Counter32, iso, Bits, Integer32, ModuleIdentity, TimeTicks, Gauge32, IpAddress, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "Counter32", "iso", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
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
mibBuilder.exportSymbols("OPENBSD-MEM-MIB", PYSNMP_MODULE_ID=memMIBObjects, memIfTable=memIfTable, memMIBVersion=memMIBVersion, memMIBObjects=memMIBObjects, memIfName=memIfName, memIfEntry=memIfEntry, memIfLiveLocks=memIfLiveLocks)
