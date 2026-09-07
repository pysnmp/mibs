#
# PySNMP MIB module CISCOWAN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source CISCOWAN-SMI
# Source digest sha256:a858f60a2199a9f90948e30b44170146bcba38b9cc45a5ad99a00648abdca066
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stratacom = ModuleIdentity((1, 3, 6, 1, 4, 1, 351))
stratacom.setRevisions(('2002-05-24 00:00', '2000-01-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stratacom.setRevisionsDescriptions(("Using the 4 digit Year value in LAST-UPDATED and\n             REVISION Clause. Modified description of 'ciscoWan'.", 'Added ciscoWanAgentCapability Object Identifier\n\t         assignment.',))
if mibBuilder.loadTexts: stratacom.setLastUpdated('2002-05-24 00:00')
if mibBuilder.loadTexts: stratacom.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: stratacom.setContactInfo('       Cisco Systems\n\t\t\tCustomer Service\n\n\t\tPostal: 170 W Tasman Drive\n\t\t\tSan Jose, CA  95134\n\t\t\tUSA\n\n\t\t   Tel: +1 800 553-NETS\n\n\t\tE-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: stratacom.setDescription('The Structure of Management Information for the\n\t\t stratacom enterprise.')
ciscoWan = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 150))
if mibBuilder.loadTexts: ciscoWan.setStatus('current')
if mibBuilder.loadTexts: ciscoWan.setDescription("ciscoWan is the main subtree for mibs under 'stratacom'\n        enterprise. This is used by MGX product series.")
ciscoWanAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 351, 160))
if mibBuilder.loadTexts: ciscoWanAgentCapability.setStatus('current')
if mibBuilder.loadTexts: ciscoWanAgentCapability.setDescription('ciscoWanAgentCapability provides a root object identifier\n        from which AGENT-CAPABILITIES values may be assigned.')
mibBuilder.exportSymbols("CISCOWAN-SMI", PYSNMP_MODULE_ID=stratacom, ciscoWan=ciscoWan, ciscoWanAgentCapability=ciscoWanAgentCapability, stratacom=stratacom)
