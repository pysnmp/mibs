#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:21:21 2022
# On host fv-az130-744 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter32, IpAddress, Bits, MibIdentifier, NotificationType, Gauge32, Counter64, iso, Integer32, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter32", "IpAddress", "Bits", "MibIdentifier", "NotificationType", "Gauge32", "Counter64", "iso", "Integer32", "ModuleIdentity", "ObjectIdentity")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bNotifyAgentRestart=bNotifyAgentRestart, benuGeneralNotif=benuGeneralNotif, PYSNMP_MODULE_ID=benuGeneralNotif, bNotifyAgentShutDown=bNotifyAgentShutDown)
