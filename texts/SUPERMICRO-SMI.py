#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-SMI
# Produced by pysmi-1.1.8 at Thu Apr 27 10:44:26 2023
# On host fv-az590-874 platform Linux version 5.15.0-1036-azure by user runner
# Using Python version 3.10.11 (main, Apr  6 2023, 07:59:08) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, ObjectIdentity, Gauge32, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Bits, Integer32, Counter32, enterprises, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "ObjectIdentity", "Gauge32", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Bits", "Integer32", "Counter32", "enterprises", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
supermicro = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876))
supermicro.setRevisions(('2001-10-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: supermicro.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: supermicro.setLastUpdated('200110260000Z')
if mibBuilder.loadTexts: supermicro.setOrganization('Super Micro Computer Inc.')
if mibBuilder.loadTexts: supermicro.setContactInfo('\tSoftware Lab\n\n\t\tPostal: 980 Rock Avenue\n\t\t\tSan Jose, CA  95131\n\t\t\tUSA\n\n\t\t   Tel: +1 408 503 8000\n\n\t\tE-mail: SoftLab@supermicro.com')
if mibBuilder.loadTexts: supermicro.setDescription('The Structure of Management Information for the\n\t\tSuper Micro enterprise.')
smProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 1))
if mibBuilder.loadTexts: smProducts.setStatus('current')
if mibBuilder.loadTexts: smProducts.setDescription('smProducts is the root OBJECT IDENTIFIER from\n\t\twhich sysObjectID values are assigned.  Actual\n\t\tvalues are defined in SUPERMICRO-PRODUCTS-MIB.')
smHealth = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 2))
if mibBuilder.loadTexts: smHealth.setStatus('current')
if mibBuilder.loadTexts: smHealth.setDescription('smHealth is the main subtree for new mib development.')
smSSMInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 10876, 100))
if mibBuilder.loadTexts: smSSMInfo.setStatus('current')
if mibBuilder.loadTexts: smSSMInfo.setDescription('smSSMInfo is the main subtree for ssm mib development.')
mibBuilder.exportSymbols("SUPERMICRO-SMI", supermicro=supermicro, smSSMInfo=smSSMInfo, smProducts=smProducts, PYSNMP_MODULE_ID=supermicro, smHealth=smHealth)
