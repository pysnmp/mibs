#
# PySNMP MIB module ENTITY-STATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ENTITY-STATE-TC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:09 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, iso, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Counter32, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32")
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

mibBuilder.exportSymbols("ENTITY-STATE-TC-MIB", EntityStandbyStatus=EntityStandbyStatus, EntityOperState=EntityOperState, EntityAdminState=EntityAdminState, PYSNMP_MODULE_ID=entityStateTc, EntityAlarmStatus=EntityAlarmStatus, entityStateTc=entityStateTc, EntityUsageState=EntityUsageState)
