#
# PySNMP MIB module BCN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-TC-MIB
# Produced by pysmi-1.1.12 at Wed May 29 08:07:25 2024
# On host fv-az698-992 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
bcnModules, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Bits, Counter64, Unsigned32, ModuleIdentity, Counter32, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 3))
bcnTCMIB.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bcnTCMIB.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnTCMIB.setOrganization('BlueCat Networks Inc.')
class BcnAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30, 40, 50, 60))
    namedValues = NamedValues(("ok", 1), ("other", 10), ("inform", 20), ("minor", 30), ("warning", 40), ("major", 50), ("critical", 60))

mibBuilder.exportSymbols("BCN-TC-MIB", PYSNMP_MODULE_ID=bcnTCMIB, bcnTCMIB=bcnTCMIB, BcnAlarmSeverity=BcnAlarmSeverity)
