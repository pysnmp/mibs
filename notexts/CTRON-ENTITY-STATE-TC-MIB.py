#
# PySNMP MIB module CTRON-ENTITY-STATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENTITY-STATE-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  9 02:19:06 2024
# On host fv-az1144-128 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ctEntityStateTC, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateTC")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Unsigned32, IpAddress, Counter32, Integer32, mib_2, NotificationType, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Unsigned32", "IpAddress", "Counter32", "Integer32", "mib-2", "NotificationType", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctEntityStateTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 30, 1))
ctEntityStateTc.setRevisions(('2005-01-23 00:00',))
if mibBuilder.loadTexts: ctEntityStateTc.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateTc.setOrganization('IETF Entity MIB Working Group')
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

mibBuilder.exportSymbols("CTRON-ENTITY-STATE-TC-MIB", PYSNMP_MODULE_ID=ctEntityStateTc, EntityOperState=EntityOperState, EntityAdminState=EntityAdminState, EntityAlarmStatus=EntityAlarmStatus, EntityStandbyStatus=EntityStandbyStatus, ctEntityStateTc=ctEntityStateTc, EntityUsageState=EntityUsageState)
