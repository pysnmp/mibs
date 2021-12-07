#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.3 at Tue Dec  7 13:58:32 2021
# On host fv-az33-388 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, ModuleIdentity, iso, NotificationType, TimeTicks, enterprises, Counter32, MibIdentifier, Integer32, Gauge32, Unsigned32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "TimeTicks", "enterprises", "Counter32", "MibIdentifier", "Integer32", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
silverpeakNW = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867))
if mibBuilder.loadTexts: silverpeakNW.setLastUpdated('201101240000Z')
if mibBuilder.loadTexts: silverpeakNW.setOrganization('Silver Peak Systems, Inc.')
silverpeakProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 1))
if mibBuilder.loadTexts: silverpeakProducts.setStatus('current')
silverpeakModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 2))
if mibBuilder.loadTexts: silverpeakModules.setStatus('current')
silverpeakMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 3))
if mibBuilder.loadTexts: silverpeakMgmt.setStatus('current')
silverpeakNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 4))
if mibBuilder.loadTexts: silverpeakNotifications.setStatus('current')
silverpeakAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 5))
if mibBuilder.loadTexts: silverpeakAgentCapability.setStatus('current')
mibBuilder.exportSymbols("SILVERPEAK-SMI", PYSNMP_MODULE_ID=silverpeakNW, silverpeakAgentCapability=silverpeakAgentCapability, silverpeakNotifications=silverpeakNotifications, silverpeakMgmt=silverpeakMgmt, silverpeakNW=silverpeakNW, silverpeakModules=silverpeakModules, silverpeakProducts=silverpeakProducts)
