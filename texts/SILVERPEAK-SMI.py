#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.12 at Tue Jun  4 08:23:52 2024
# On host fv-az530-683 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Counter32, NotificationType, IpAddress, ModuleIdentity, Bits, Integer32, TimeTicks, Gauge32, MibIdentifier, iso, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter32", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "Integer32", "TimeTicks", "Gauge32", "MibIdentifier", "iso", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakAgentCapability=silverpeakAgentCapability, silverpeakProducts=silverpeakProducts, PYSNMP_MODULE_ID=silverpeakNW, silverpeakMgmt=silverpeakMgmt, silverpeakNotifications=silverpeakNotifications, silverpeakModules=silverpeakModules, silverpeakNW=silverpeakNW)
