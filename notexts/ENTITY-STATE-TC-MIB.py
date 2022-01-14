#
# PySNMP MIB module ENTITY-STATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ENTITY-STATE-TC-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:32:30 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Bits, Counter32, MibIdentifier, Integer32, IpAddress, NotificationType, ObjectIdentity, mib_2, ModuleIdentity, Gauge32, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "NotificationType", "ObjectIdentity", "mib-2", "ModuleIdentity", "Gauge32", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
entityStateTc = ModuleIdentity((1, 3, 6, 1, 2, 1, 130))
entityStateTc.setRevisions(('2005-11-22 00:00',))
if mibBuilder.loadTexts: entityStateTc.setLastUpdated('200511220000Z')
if mibBuilder.loadTexts: entityStateTc.setOrganization('IETF Entity MIB Working Group')
class EntityAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4))

class EntityOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("testing", 4))

class EntityUsageState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("idle", 2), ("active", 3), ("busy", 4))

class EntityAlarmStatus(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("unknown", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("indeterminate", 6))

class EntityStandbyStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("hotStandby", 2), ("coldStandby", 3), ("providingService", 4))

mibBuilder.exportSymbols("ENTITY-STATE-TC-MIB", entityStateTc=entityStateTc, PYSNMP_MODULE_ID=entityStateTc, EntityStandbyStatus=EntityStandbyStatus, EntityAdminState=EntityAdminState, EntityAlarmStatus=EntityAlarmStatus, EntityOperState=EntityOperState, EntityUsageState=EntityUsageState)
