#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.8 at Mon Jan  9 11:10:08 2023
# On host fv-az402-229 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ModuleIdentity, Bits, NotificationType, Integer32, Counter32, TimeTicks, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Bits", "NotificationType", "Integer32", "Counter32", "TimeTicks", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakModules=silverpeakModules, silverpeakAgentCapability=silverpeakAgentCapability, PYSNMP_MODULE_ID=silverpeakNW, silverpeakNotifications=silverpeakNotifications, silverpeakMgmt=silverpeakMgmt, silverpeakProducts=silverpeakProducts, silverpeakNW=silverpeakNW)
