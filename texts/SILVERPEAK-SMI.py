#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.11 at Wed Apr  3 14:56:32 2024
# On host fv-az1198-695 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, enterprises, Bits, Counter32, TimeTicks, NotificationType, MibIdentifier, ModuleIdentity, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "enterprises", "Bits", "Counter32", "TimeTicks", "NotificationType", "MibIdentifier", "ModuleIdentity", "Gauge32", "Counter64")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakNotifications=silverpeakNotifications, silverpeakModules=silverpeakModules, PYSNMP_MODULE_ID=silverpeakNW, silverpeakNW=silverpeakNW, silverpeakProducts=silverpeakProducts, silverpeakMgmt=silverpeakMgmt, silverpeakAgentCapability=silverpeakAgentCapability)
