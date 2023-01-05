#
# PySNMP MIB module AT-MIBVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-MIBVERSION-MIB
# Produced by pysmi-1.1.8 at Thu Jan  5 11:23:52 2023
# On host fv-az280-773 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, MibIdentifier, ModuleIdentity, Gauge32, IpAddress, TimeTicks, ObjectIdentity, NotificationType, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "MibIdentifier", "ModuleIdentity", "Gauge32", "IpAddress", "TimeTicks", "ObjectIdentity", "NotificationType", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atMibVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15))
atMibVersion.setRevisions(('2010-06-15 00:11', '2009-01-15 00:00',))
if mibBuilder.loadTexts: atMibVersion.setLastUpdated('201006150011Z')
if mibBuilder.loadTexts: atMibVersion.setOrganization('Allied Telesis Labs New Zealand')
atMibsetVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atMibsetVersion.setStatus('current')
mibBuilder.exportSymbols("AT-MIBVERSION-MIB", PYSNMP_MODULE_ID=atMibVersion, atMibsetVersion=atMibsetVersion, atMibVersion=atMibVersion)
