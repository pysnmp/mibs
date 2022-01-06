#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source https://pysnmp.github.io:443/mibs/asn1/CISCOWAN-SMI
# Produced by pysmi-1.1.8 at Thu Jan  6 19:59:57 2022
# On host fv-az121-779 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, iso, ModuleIdentity, enterprises, Counter64, Gauge32, IpAddress, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "iso", "ModuleIdentity", "enterprises", "Counter64", "Gauge32", "IpAddress", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stratacom.setRevisionsDescriptions(("Using the 4 digit Year value in LAST-UPDATED and\n             REVISION Clause. Modified description of 'ciscoWan'.", 'Added ciscoWanAgentCapability Object Identifier\n\t         assignment.',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('200205240000Z')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: stratacom.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal: 170 W Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel: +1 800 553-NETS\n\n\t\tE-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: stratacom.setDescription('The Structure of Management Information for the\n\t\t stratacom enterprise.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
if mibBuilder.loadTexts: ciscoWan.setDescription("ciscoWan is the main subtree for mibs under 'stratacom'\n        enterprise. This is used by MGX product series.")
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAgentCapability.setDescription('ciscoWanAgentCapability provides a root object identifier\n        from which AGENT-CAPABILITIES values may be assigned.')
mibBuilder.exportSymbols("CISCOWAN-SMI", stratacom=stratacom, ciscoWan=ciscoWan, PYSNMP_MODULE_ID=stratacom, ciscoWanAgentCapability=ciscoWanAgentCapability)
