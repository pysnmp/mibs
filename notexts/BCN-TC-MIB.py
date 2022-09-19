#
# PySNMP MIB module BCN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-TC-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:25:21 2022
# On host fv-az278-268 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
bcnModules, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, MibIdentifier, IpAddress, Counter32, TimeTicks, Integer32, iso, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "MibIdentifier", "IpAddress", "Counter32", "TimeTicks", "Integer32", "iso", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 4, 3))
bcnTCMIB.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bcnTCMIB.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bcnTCMIB.setOrganization('BlueCat Networks Inc.')
class BcnAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 10, 20, 30, 40, 50, 60))
    namedValues = NamedValues(("ok", 1), ("other", 10), ("inform", 20), ("minor", 30), ("warning", 40), ("major", 50), ("critical", 60))

mibBuilder.exportSymbols("BCN-TC-MIB", PYSNMP_MODULE_ID=bcnTCMIB, BcnAlarmSeverity=BcnAlarmSeverity, bcnTCMIB=bcnTCMIB)
