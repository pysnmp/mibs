#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:30:45 2023
# On host fv-az1153-970 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, MibIdentifier, IpAddress, iso, Bits, Counter64, Unsigned32, Counter32, ObjectIdentity, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "MibIdentifier", "IpAddress", "iso", "Bits", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", PYSNMP_MODULE_ID=benuGeneralNotif, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bNotifyAgentRestart=bNotifyAgentRestart, benuGeneralNotif=benuGeneralNotif, bNotifyAgentShutDown=bNotifyAgentShutDown, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps)
