#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.8 at Thu Sep  8 09:11:57 2022
# On host fv-az447-161 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Bits, TimeTicks, NotificationType, mib_2, Gauge32, IpAddress, Unsigned32, Counter32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Bits", "TimeTicks", "NotificationType", "mib-2", "Gauge32", "IpAddress", "Unsigned32", "Counter32", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuGeneralNotif = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 4))
benuGeneralNotif.setRevisions(('2014-12-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuGeneralNotif.setRevisionsDescriptions(('Changed bGeneralNotifyMIBTraps from index 2 to 0',))
if mibBuilder.loadTexts: benuGeneralNotif.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: benuGeneralNotif.setOrganization('Benu Networks')
if mibBuilder.loadTexts: benuGeneralNotif.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: benuGeneralNotif.setDescription('Initial creation\n        MIB module containing general trap definition.\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
bGeneralNotifyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 4, 1))
bGeneralNotifyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0))
bNotifyAgentShutDown = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 1))
if mibBuilder.loadTexts: bNotifyAgentShutDown.setStatus('current')
if mibBuilder.loadTexts: bNotifyAgentShutDown.setDescription('An indication that the agent is in the process of being shut down.')
bNotifyAgentRestart = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 2))
if mibBuilder.loadTexts: bNotifyAgentRestart.setStatus('current')
if mibBuilder.loadTexts: bNotifyAgentRestart.setDescription('An indication that the agent has been restarted.\n         This does not imply anything about whether the configuration has\n         changed or not (unlike the standard coldStart or warmStart traps)')
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, bNotifyAgentRestart=bNotifyAgentRestart, PYSNMP_MODULE_ID=benuGeneralNotif, benuGeneralNotif=benuGeneralNotif, bNotifyAgentShutDown=bNotifyAgentShutDown)
