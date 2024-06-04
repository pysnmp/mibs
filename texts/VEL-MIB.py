#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 13:08:39 2024
# On host fv-az1108-994 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, Counter64, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Integer32, Gauge32, ModuleIdentity, Unsigned32, enterprises, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter64", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Integer32", "Gauge32", "ModuleIdentity", "Unsigned32", "enterprises", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vel.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
if mibBuilder.loadTexts: vel.setContactInfo('Contact:\n\n                Web: http://www.vigintos.com\n                Email: ve@vigintos.com\n    \n                Address: Ozo 4, Vilnius, LT-08200, Lithuania\n                Tel:\t\t\t +37052477465\n                Fax:       +37052477466')
if mibBuilder.loadTexts: vel.setDescription('This is the root MIB module for VEL with OID of\n\t\t\t\t{iso org dod internet private enterprises 27993}.\n\n\t\t\t\tIANA allocated this enterprise OID (object identifier) for the\n\t\t\t\texclusive use of Vigintos Elektronika (VEL). \n\t\t\t\tOther than internet network equipment\n\t\t\t\tdistributed or licensed by VEL, no other party has any right\n\t\t\t\twhat-so-ever to distribute or license internet network equipment\n\t\t\t\twhich responds to the VEL enterprise OID or its subsidiary\n\t\t\t\tbranches. VEL reserves the right to criminally prosecute and/or\n\t\t\t\tto seek civil damages from anyone fraudently using the VEL\n\t\t\t\tenterprise OID to the full extent of the law.')
mibBuilder.exportSymbols("VEL-MIB", PYSNMP_MODULE_ID=vel, vel=vel)
