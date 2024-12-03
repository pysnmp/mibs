#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 10:03:47 2024
# On host fv-az575-513 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, iso, Integer32, Bits, TimeTicks, Counter32, Unsigned32, IpAddress, mib_2, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "Bits", "TimeTicks", "Counter32", "Unsigned32", "IpAddress", "mib-2", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuGeneralNotif = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 4))
benuGeneralNotif.setRevisions(('2014-12-15 00:00',))
if mibBuilder.loadTexts: benuGeneralNotif.setLastUpdated('201412150000Z')
if mibBuilder.loadTexts: benuGeneralNotif.setOrganization('Benu Networks')
bGeneralNotifyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 4, 1))
bGeneralNotifyMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0))
bNotifyAgentShutDown = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 1))
if mibBuilder.loadTexts: bNotifyAgentShutDown.setStatus('current')
bNotifyAgentRestart = NotificationType((1, 3, 6, 1, 4, 1, 39406, 1, 4, 0, 2))
if mibBuilder.loadTexts: bNotifyAgentRestart.setStatus('current')
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", benuGeneralNotif=benuGeneralNotif, bNotifyAgentShutDown=bNotifyAgentShutDown, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, PYSNMP_MODULE_ID=benuGeneralNotif, bNotifyAgentRestart=bNotifyAgentRestart)
