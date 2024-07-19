#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Fri Jul 19 08:52:13 2024
# On host fv-az1149-759 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, mib_2, iso, Counter64, ModuleIdentity, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "mib-2", "iso", "Counter64", "ModuleIdentity", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bNotifyAgentShutDown=bNotifyAgentShutDown, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, PYSNMP_MODULE_ID=benuGeneralNotif, benuGeneralNotif=benuGeneralNotif, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, bNotifyAgentRestart=bNotifyAgentRestart)
