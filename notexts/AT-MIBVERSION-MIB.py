#
# PySNMP MIB module AT-MIBVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-MIBVERSION-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 19:18:31 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, TimeTicks, Gauge32, Integer32, Counter64, Counter32, IpAddress, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "Gauge32", "Integer32", "Counter64", "Counter32", "IpAddress", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atMibVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15))
atMibVersion.setRevisions(('2010-06-15 00:11', '2009-01-15 00:00',))
if mibBuilder.loadTexts: atMibVersion.setLastUpdated('201006150011Z')
if mibBuilder.loadTexts: atMibVersion.setOrganization('Allied Telesis Labs New Zealand')
atMibsetVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atMibsetVersion.setStatus('current')
mibBuilder.exportSymbols("AT-MIBVERSION-MIB", atMibVersion=atMibVersion, atMibsetVersion=atMibsetVersion, PYSNMP_MODULE_ID=atMibVersion)
