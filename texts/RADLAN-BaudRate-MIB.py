#
# PySNMP MIB module RADLAN-BaudRate-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-BaudRate-MIB
# Produced by pysmi-1.1.12 at Wed Nov  6 08:34:55 2024
# On host fv-az984-999 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, ObjectIdentity, MibIdentifier, Bits, Counter64, Counter32, NotificationType, iso, ModuleIdentity, Integer32, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "ObjectIdentity", "MibIdentifier", "Bits", "Counter64", "Counter32", "NotificationType", "iso", "ModuleIdentity", "Integer32", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlRs232 = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 104))
rlRs232.setRevisions(('2005-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlRs232.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlRs232.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlRs232.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlRs232.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlRs232.setDescription('The private MIB module definition for baudrate.')
rlRs232MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRs232MibVersion.setStatus('current')
if mibBuilder.loadTexts: rlRs232MibVersion.setDescription("MIB's version, the current version is 1.")
rlRs232AutoBaudRateStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatus.setStatus('current')
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatus.setDescription('Show the current Auto BaudRate status')
rlRs232AutoBaudRateStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatusAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatusAfterReset.setDescription('Show/Set the Auto BaudRate status after reset')
rlRs232BaudRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("baud2400", 1), ("baud4800", 2), ("baud9600", 3), ("baud19200", 4), ("baud38400", 5), ("baud57600", 6), ("baud115200", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRs232BaudRate.setStatus('current')
if mibBuilder.loadTexts: rlRs232BaudRate.setDescription('Show/Set the current Baud Rate status')
mibBuilder.exportSymbols("RADLAN-BaudRate-MIB", rlRs232AutoBaudRateStatus=rlRs232AutoBaudRateStatus, rlRs232AutoBaudRateStatusAfterReset=rlRs232AutoBaudRateStatusAfterReset, rlRs232MibVersion=rlRs232MibVersion, rlRs232=rlRs232, rlRs232BaudRate=rlRs232BaudRate, PYSNMP_MODULE_ID=rlRs232)
