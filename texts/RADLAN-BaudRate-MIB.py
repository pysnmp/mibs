#
# PySNMP MIB module RADLAN-BaudRate-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-BaudRate-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 13:13:55 2023
# On host fv-az247-868 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter32, ObjectIdentity, IpAddress, iso, ModuleIdentity, TimeTicks, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "iso", "ModuleIdentity", "TimeTicks", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RADLAN-BaudRate-MIB", rlRs232MibVersion=rlRs232MibVersion, rlRs232BaudRate=rlRs232BaudRate, rlRs232AutoBaudRateStatusAfterReset=rlRs232AutoBaudRateStatusAfterReset, rlRs232AutoBaudRateStatus=rlRs232AutoBaudRateStatus, PYSNMP_MODULE_ID=rlRs232, rlRs232=rlRs232)
