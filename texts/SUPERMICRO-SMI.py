#
# PySNMP MIB module SUPERMICRO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/supermicro/SUPERMICRO-SMI
# Produced by pysmi-1.1.8 at Sun Jan 16 15:37:36 2022
# On host fv-az36-128 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, Bits, Integer32, MibIdentifier, enterprises, Unsigned32, ObjectIdentity, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "Bits", "Integer32", "MibIdentifier", "enterprises", "Unsigned32", "ObjectIdentity", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "NotificationType", "ModuleIdentity")
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
mibBuilder.exportSymbols("SUPERMICRO-SMI", supermicro=supermicro, smSSMInfo=smSSMInfo, smProducts=smProducts, smHealth=smHealth, PYSNMP_MODULE_ID=supermicro)
