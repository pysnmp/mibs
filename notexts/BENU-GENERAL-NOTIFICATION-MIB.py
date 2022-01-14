#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:35:57 2022
# On host fv-az74-435 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Integer32, iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Gauge32, IpAddress, mib_2, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "IpAddress", "mib-2", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bNotifyAgentRestart=bNotifyAgentRestart, PYSNMP_MODULE_ID=benuGeneralNotif, benuGeneralNotif=benuGeneralNotif, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps, bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, bNotifyAgentShutDown=bNotifyAgentShutDown)
