#
# PySNMP MIB module SILVERPEAK-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/silverpeak/SILVERPEAK-SMI
# Produced by pysmi-1.1.3 at Tue Nov 30 03:07:50 2021
# On host fv-az42-83 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, iso, Gauge32, enterprises, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Unsigned32, TimeTicks, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "iso", "Gauge32", "enterprises", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("SILVERPEAK-SMI", silverpeakProducts=silverpeakProducts, silverpeakNotifications=silverpeakNotifications, silverpeakModules=silverpeakModules, silverpeakNW=silverpeakNW, PYSNMP_MODULE_ID=silverpeakNW, silverpeakMgmt=silverpeakMgmt, silverpeakAgentCapability=silverpeakAgentCapability)
