#
# PySNMP MIB module AT-MIBVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-MIBVERSION-MIB
# Produced by pysmi-1.1.12 at Mon Sep 16 14:51:07 2024
# On host fv-az1272-448 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Gauge32, iso, Integer32, Counter64, Counter32, NotificationType, ObjectIdentity, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Gauge32", "iso", "Integer32", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atMibVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15))
atMibVersion.setRevisions(('2010-06-15 00:11', '2009-01-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atMibVersion.setRevisionsDescriptions(('MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: atMibVersion.setLastUpdated('201006150011Z')
if mibBuilder.loadTexts: atMibVersion.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: atMibVersion.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atMibVersion.setDescription("The mib-set version MIB, for detailing the versions of MIB's\n                that are currently supported by AT software.")
atMibsetVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atMibsetVersion.setStatus('current')
if mibBuilder.loadTexts: atMibsetVersion.setDescription("The overall version of the complete set of MIB's that is\n                currently supported by the software running on the device.\n\n                It returns an integer which relates to the last software\n                release that contained changes to the supported AT Enterprise\n                MIB definition files. For example, if the currently loaded\n                software release on the the device is 5.3.1-03 but the\n                Enterprise MIB's have not changed since 5.3.1-01, then the\n                value returned will be 5030101 (5.03.01-01).")
mibBuilder.exportSymbols("AT-MIBVERSION-MIB", PYSNMP_MODULE_ID=atMibVersion, atMibsetVersion=atMibsetVersion, atMibVersion=atMibVersion)
