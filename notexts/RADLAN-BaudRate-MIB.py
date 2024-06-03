#
# PySNMP MIB module RADLAN-BaudRate-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-BaudRate-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:27:52 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Counter32, TimeTicks, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, ObjectIdentity, Unsigned32, Counter64, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter32", "TimeTicks", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlRs232 = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 104))
rlRs232.setRevisions(('2005-04-14 00:00',))
if mibBuilder.loadTexts: rlRs232.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlRs232.setOrganization('Radlan Computer Communications Ltd.')
rlRs232MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRs232MibVersion.setStatus('current')
rlRs232AutoBaudRateStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatus.setStatus('current')
rlRs232AutoBaudRateStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRs232AutoBaudRateStatusAfterReset.setStatus('current')
rlRs232BaudRate = MibScalar((1, 3, 6, 1, 4, 1, 89, 104, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("baud2400", 1), ("baud4800", 2), ("baud9600", 3), ("baud19200", 4), ("baud38400", 5), ("baud57600", 6), ("baud115200", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlRs232BaudRate.setStatus('current')
mibBuilder.exportSymbols("RADLAN-BaudRate-MIB", rlRs232AutoBaudRateStatus=rlRs232AutoBaudRateStatus, rlRs232=rlRs232, rlRs232MibVersion=rlRs232MibVersion, PYSNMP_MODULE_ID=rlRs232, rlRs232BaudRate=rlRs232BaudRate, rlRs232AutoBaudRateStatusAfterReset=rlRs232AutoBaudRateStatusAfterReset)
