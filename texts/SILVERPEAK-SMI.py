#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.8 at Mon Jan  2 13:29:23 2023
# On host fv-az552-501 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, TimeTicks, ModuleIdentity, Counter32, Bits, ObjectIdentity, enterprises, IpAddress, iso, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Counter32", "Bits", "ObjectIdentity", "enterprises", "IpAddress", "iso", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
silverpeakNW = ModuleIdentity((1, 3, 6, 1, 4, 1, 23867))
if mibBuilder.loadTexts: silverpeakNW.setLastUpdated('201101240000Z')
if mibBuilder.loadTexts: silverpeakNW.setOrganization('Silver Peak Systems, Inc.')
if mibBuilder.loadTexts: silverpeakNW.setContactInfo('  URL: http://www.silver-peak.com/contact\n            E-mail: support@silver-peak.com ')
if mibBuilder.loadTexts: silverpeakNW.setDescription('The Structure of Management Information for the\n        Silverpeak Systems enterprise.')
silverpeakProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 1))
if mibBuilder.loadTexts: silverpeakProducts.setStatus('current')
if mibBuilder.loadTexts: silverpeakProducts.setDescription('silverpeakProducts is the root OBJECT IDENTIFIER from\n        which sysObjectID values are assigned. Actual values\n        are defined in SILVERPEAK-PRODUCTS-MIB.')
silverpeakModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 2))
if mibBuilder.loadTexts: silverpeakModules.setStatus('current')
if mibBuilder.loadTexts: silverpeakModules.setDescription('silverpeakModules provides a root object identifier from\n        which MODULE-ENTITY values may be assigned.')
silverpeakMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 3))
if mibBuilder.loadTexts: silverpeakMgmt.setStatus('current')
if mibBuilder.loadTexts: silverpeakMgmt.setDescription('silverpeakMgmt is the main subtree for management mibs.')
silverpeakNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 4))
if mibBuilder.loadTexts: silverpeakNotifications.setStatus('current')
if mibBuilder.loadTexts: silverpeakNotifications.setDescription('silverpeakNotifications is the main subtree for agent notifications.')
silverpeakAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 23867, 5))
if mibBuilder.loadTexts: silverpeakAgentCapability.setStatus('current')
if mibBuilder.loadTexts: silverpeakAgentCapability.setDescription('silverpeakAgentCapability provides a root object identifier\n        from which AGENT-CAPABILITIES values may be assigned.')
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakMgmt=silverpeakMgmt, silverpeakNotifications=silverpeakNotifications, silverpeakProducts=silverpeakProducts, silverpeakAgentCapability=silverpeakAgentCapability, PYSNMP_MODULE_ID=silverpeakNW, silverpeakNW=silverpeakNW, silverpeakModules=silverpeakModules)
