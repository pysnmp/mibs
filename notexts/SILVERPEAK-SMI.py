#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.3 at Mon Nov 22 12:37:10 2021
# On host fv-az83-627 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, enterprises, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Gauge32, IpAddress, Unsigned32, NotificationType, Counter32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "enterprises", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakMgmt=silverpeakMgmt, silverpeakAgentCapability=silverpeakAgentCapability, silverpeakModules=silverpeakModules, silverpeakNotifications=silverpeakNotifications, PYSNMP_MODULE_ID=silverpeakNW, silverpeakProducts=silverpeakProducts, silverpeakNW=silverpeakNW)
