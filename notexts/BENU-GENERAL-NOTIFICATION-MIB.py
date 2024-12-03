#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:37:32 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter32, IpAddress, ObjectIdentity, Unsigned32, Counter64, MibIdentifier, Gauge32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "Counter64", "MibIdentifier", "Gauge32", "Integer32", "Bits")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bNotifyAgentShutDown=bNotifyAgentShutDown, PYSNMP_MODULE_ID=benuGeneralNotif, benuGeneralNotif=benuGeneralNotif, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, bNotifyAgentRestart=bNotifyAgentRestart)
