#
# PySNMP MIB module BENU-GENERAL-NOTIFICATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-GENERAL-NOTIFICATION-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:04:12 2022
# On host fv-az126-754 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ObjectIdentity, Counter32, IpAddress, ModuleIdentity, TimeTicks, Integer32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Bits, mib_2, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "ModuleIdentity", "TimeTicks", "Integer32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Bits", "mib-2", "NotificationType")
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
mibBuilder.exportSymbols("BENU-GENERAL-NOTIFICATION-MIB", bGeneralNotifyMIBObjects=bGeneralNotifyMIBObjects, benuGeneralNotif=benuGeneralNotif, PYSNMP_MODULE_ID=benuGeneralNotif, bNotifyAgentShutDown=bNotifyAgentShutDown, bNotifyAgentRestart=bNotifyAgentRestart, bGeneralNotifyMIBTraps=bGeneralNotifyMIBTraps)
