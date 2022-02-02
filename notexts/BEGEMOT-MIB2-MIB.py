#
# PySNMP MIB module BEGEMOT-MIB2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-MIB2-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 19:34:29 2022
# On host fv-az33-564 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
begemotIp, = mibBuilder.importSymbols("BEGEMOT-IP-MIB", "begemotIp")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, NotificationType, Counter32, Bits, TimeTicks, IpAddress, Unsigned32, iso, Integer32, ObjectIdentity, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "NotificationType", "Counter32", "Bits", "TimeTicks", "IpAddress", "Unsigned32", "iso", "Integer32", "ObjectIdentity", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotMib2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1))
begemotMib2.setRevisions(('2009-08-03 00:00', '2006-02-13 00:00',))
if mibBuilder.loadTexts: begemotMib2.setLastUpdated('200908030000Z')
if mibBuilder.loadTexts: begemotMib2.setOrganization('German Aerospace Center')
begemotIfMaxspeed = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 1), Counter64()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfMaxspeed.setStatus('current')
begemotIfPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotIfPoll.setStatus('current')
begemotIfForcePoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfForcePoll.setStatus('current')
begemotIfDataPoll = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 3, 1, 4), TimeTicks().clone(100)).setUnits('deciseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotIfDataPoll.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-MIB2-MIB", begemotIfMaxspeed=begemotIfMaxspeed, begemotIfPoll=begemotIfPoll, begemotIfForcePoll=begemotIfForcePoll, begemotMib2=begemotMib2, PYSNMP_MODULE_ID=begemotMib2, begemotIfDataPoll=begemotIfDataPoll)
