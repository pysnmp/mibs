#
# PySNMP MIB module CTRON-ENTITY-STATE-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ENTITY-STATE-TC-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:40:19 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctEntityStateTC, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctEntityStateTC")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, TimeTicks, Integer32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, Unsigned32, IpAddress, MibIdentifier, mib_2, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "mib-2", "ModuleIdentity", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctEntityStateTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 2, 30, 1))
ctEntityStateTc.setRevisions(('2005-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctEntityStateTc.setRevisionsDescriptions(('Initial version, published as RFC yyyy.',))
if mibBuilder.loadTexts: ctEntityStateTc.setLastUpdated('200501230000Z')
if mibBuilder.loadTexts: ctEntityStateTc.setOrganization('IETF Entity MIB Working Group')
if mibBuilder.loadTexts: ctEntityStateTc.setContactInfo('General Discussion: entmib@ietf.org\n                   To Subscribe:\n                     http://www.ietf.org/mailman/listinfo/entmib\n\nhttp://www.ietf.org/html.charters/entmib-charter.html\n\n                     Sharon Chisholm\n                     Nortel Networks\n                     PO Box 3511 Station C\n                     Ottawa, Ont.  K1Y 4H7\n                     Canada\n                     schishol@nortelnetworks.com\n\n\n\n                     David T. Perkins\n                     548 Qualbrook Ct\n                     San Jose, CA 95110\n                     USA\n                     Phone: 408 394-8702\n                     dperkins@snmpinfo.com')
if mibBuilder.loadTexts: ctEntityStateTc.setDescription('This MIB defines state textual conventions.\n\n          Copyright (C) The Internet Society 2005.  This version\n          of this MIB module is part of RFC yyyy;  see the RFC\n          itself for full legal notices.')
class EntityAdminState(TextualConvention, Integer32):
    description = " Represents the various possible administrative states.\n\n              A value of 'locked' means the resource is administratively\n              prohibited from use. A value of 'shuttingDown' means that\n              usage is administratively limited to current instances of\n              use. A value of 'unlocked' means the resource is not\n              administratively prohibited from use. A value of\n               'unknown' means that this resource is unable to\n               report administrative state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("locked", 2), ("shuttingDown", 3), ("unlocked", 4))

class EntityOperState(TextualConvention, Integer32):
    description = " Represents the possible values of operational states.\n\n              A value of 'disabled' means the resource is totally\n              inoperable. A value of 'enabled' means the resource\n              is partially or fully operable. A value of 'testing'\n              means the resource is currently being tested\n              and cannot therefore report whether it is operational\n              or not. A value of 'unknown' means that this\n              resource is unable to report operational state. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3), ("testing", 4))

class EntityUsageState(TextualConvention, Integer32):
    description = " Represents the possible values of usage states.\n              A value of 'idle' means the resource is servicing no\n              users. A value of 'active' means the resource is\n              currently in use and it has sufficient spare capacity\n              to provide for additional users. A value of 'busy'\n              means the resource is currently in use, but it\n              currently has no spare capacity to provide for\n              additional users. A value of 'unknown' means\n              that this resource is unable to report usage state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("idle", 2), ("active", 3), ("busy", 4))

class EntityAlarmStatus(TextualConvention, Bits):
    description = "Represents the possible values of alarm status.\n            An Alarm [RFC3877] is a persistent indication\n            of an error or warning condition.\n\n            When no bits of this attribute are set, then no active\n            alarms are known against this entity and it is not under\n            repair.\n\n            When the 'value of underRepair' is set, the resource is\n            currently being repaired, which, depending on the\n            implementation, may make the other values in this bit\n            string not meaningful.\n\n            When the value of 'critical' is set, one or more critical\n            alarms are active against the resource. When the value\n            of 'major' is set, one or more major alarms are active\n            against the resource. When the value of 'minor' is set,\n            one or more minor alarms are active against the resource.\n            When the value of 'warning' is set, one or more warning\n            alarms are active against the resource. When the value\n            of 'indeterminate' is set, one or more alarms whose of\n            perceived severity cannot be determined are active\n            against this resource.\n\n            A value of 'unknown' means that this resource is\n            unable to report alarm state."
    status = 'current'
    namedValues = NamedValues(("unknown", 0), ("underRepair", 1), ("critical", 2), ("major", 3), ("minor", 4), ("warning", 5), ("indeterminate", 6))

class EntityStandbyStatus(TextualConvention, Integer32):
    description = " Represents the possible values of standby status.\n\n              A value of 'hotStandby' means the resource is not\n              providing service, but it will be immediately able to\n              take over the role of the resource to be backed-up,\n              without the need for initialization activity, and will\n              contain the same information as the resource to be\n              backed up. A value of 'coldStandy' means that the\n              resource is to back-up another resource, but will not\n              be immediately able to take over the role of a resource\n              to be backed up, and will require some initialization\n              activity. A value of 'providingService' means the\n              resource is providing service. A value of\n               'unknown' means that this resource is unable to\n               report standby state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("hotStandby", 2), ("coldStandby", 3), ("providingService", 4))

mibBuilder.exportSymbols("CTRON-ENTITY-STATE-TC-MIB", ctEntityStateTc=ctEntityStateTc, PYSNMP_MODULE_ID=ctEntityStateTc, EntityUsageState=EntityUsageState, EntityStandbyStatus=EntityStandbyStatus, EntityAlarmStatus=EntityAlarmStatus, EntityOperState=EntityOperState, EntityAdminState=EntityAdminState)
