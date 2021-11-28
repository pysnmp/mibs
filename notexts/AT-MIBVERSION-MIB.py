#
# PySNMP MIB module AT-MIBVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-MIBVERSION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:45:57 2021
# On host fv-az36-794 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, TimeTicks, ModuleIdentity, Integer32, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, IpAddress, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "IpAddress", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atMibVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15))
atMibVersion.setRevisions(('2010-06-15 00:11', '2009-01-15 00:00',))
if mibBuilder.loadTexts: atMibVersion.setLastUpdated('201006150011Z')
if mibBuilder.loadTexts: atMibVersion.setOrganization('Allied Telesis Labs New Zealand')
atMibsetVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atMibsetVersion.setStatus('current')
mibBuilder.exportSymbols("AT-MIBVERSION-MIB", atMibsetVersion=atMibsetVersion, PYSNMP_MODULE_ID=atMibVersion, atMibVersion=atMibVersion)
