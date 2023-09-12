#
# PySNMP MIB module IANAPowerStateSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANAPowerStateSet-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:56:22 2023
# On host fv-az447-19 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, TimeTicks, Counter64, Integer32, Bits, Counter32, Unsigned32, IpAddress, ModuleIdentity, NotificationType, mib_2, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "TimeTicks", "Counter64", "Integer32", "Bits", "Counter32", "Unsigned32", "IpAddress", "ModuleIdentity", "NotificationType", "mib-2", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaPowerStateSet = ModuleIdentity((1, 3, 6, 1, 2, 1, 228))
ianaPowerStateSet.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: ianaPowerStateSet.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaPowerStateSet.setOrganization('IANA')
class PowerStateSet(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/power-state-sets'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 255, 256, 257, 258, 259, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036))
    namedValues = NamedValues(("other", 0), ("unknown", 255), ("ieee1621", 256), ("ieee1621Off", 257), ("ieee1621Sleep", 258), ("ieee1621On", 259), ("dmtf", 512), ("dmtfOn", 513), ("dmtfSleepLight", 514), ("dmtfSleepDeep", 515), ("dmtfOffHard", 516), ("dmtfOffSoft", 517), ("dmtfHibernate", 518), ("dmtfPowerOffSoft", 519), ("dmtfPowerOffHard", 520), ("dmtfMasterBusReset", 521), ("dmtfDiagnosticInterrapt", 522), ("dmtfOffSoftGraceful", 523), ("dmtfOffHardGraceful", 524), ("dmtfMasterBusResetGraceful", 525), ("dmtfPowerCycleOffSoftGraceful", 526), ("dmtfPowerCycleHardGraceful", 527), ("eman", 1024), ("emanMechOff", 1025), ("emanSoftOff", 1026), ("emanHibernate", 1027), ("emanSleep", 1028), ("emanStandby", 1029), ("emanReady", 1030), ("emanLowMinus", 1031), ("emanLow", 1032), ("emanMediumMinus", 1033), ("emanMedium", 1034), ("emanHighMinus", 1035), ("emanHigh", 1036))

mibBuilder.exportSymbols("IANAPowerStateSet-MIB", ianaPowerStateSet=ianaPowerStateSet, PowerStateSet=PowerStateSet, PYSNMP_MODULE_ID=ianaPowerStateSet)
