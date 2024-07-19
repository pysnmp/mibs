#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-SMI
# Produced by pysmi-1.1.12 at Fri Jul 19 10:07:30 2024
# On host fv-az1251-884 platform Linux version 6.5.0-1023-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Gauge32, IpAddress, enterprises, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Integer32, iso, Unsigned32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Gauge32", "IpAddress", "enterprises", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Integer32", "iso", "Unsigned32", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SUPERMICRO-SMI", smHealth=smHealth, smSSMInfo=smSSMInfo, supermicro=supermicro, smProducts=smProducts, PYSNMP_MODULE_ID=supermicro)
