#
# PySNMP MIB module BCN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-TC-MIB
# Produced by pysmi-1.1.10 at Thu Oct 26 12:24:00 2023
# On host fv-az583-292 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
bcnModules, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, Bits, Integer32, IpAddress, ModuleIdentity, ObjectIdentity, Counter64, iso, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Counter64", "iso", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 3))
bcnTCMIB.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bcnTCMIB.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnTCMIB.setOrganization('BlueCat Networks Inc.')
class BcnAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30, 40, 50, 60))
    namedValues = NamedValues(("ok", 1), ("other", 10), ("inform", 20), ("minor", 30), ("warning", 40), ("major", 50), ("critical", 60))

mibBuilder.exportSymbols("BCN-TC-MIB", bcnTCMIB=bcnTCMIB, BcnAlarmSeverity=BcnAlarmSeverity, PYSNMP_MODULE_ID=bcnTCMIB)
