#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.8 at Tue Jan 11 21:45:29 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, NotificationType, Integer32, IpAddress, Counter32, Gauge32, MibIdentifier, Counter64, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "IpAddress", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "enterprises", "TimeTicks")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakAgentCapability=silverpeakAgentCapability, silverpeakNW=silverpeakNW, silverpeakModules=silverpeakModules, silverpeakProducts=silverpeakProducts, silverpeakMgmt=silverpeakMgmt, PYSNMP_MODULE_ID=silverpeakNW, silverpeakNotifications=silverpeakNotifications)
