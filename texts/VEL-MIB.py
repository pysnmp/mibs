#
# PySNMP MIB module VEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:18:55 2024
# On host fv-az1567-4 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, iso, ModuleIdentity, TimeTicks, Counter32, Counter64, Gauge32, IpAddress, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "ModuleIdentity", "TimeTicks", "Counter32", "Counter64", "Gauge32", "IpAddress", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vel = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993))
vel.setRevisions(('2011-10-05 08:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vel.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: vel.setLastUpdated('201110050800Z')
if mibBuilder.loadTexts: vel.setOrganization('Vigintos Elektronika')
if mibBuilder.loadTexts: vel.setContactInfo('Contact:\n\n                Web: http://www.vigintos.com\n                Email: ve@vigintos.com\n    \n                Address: Ozo 4, Vilnius, LT-08200, Lithuania\n                Tel:\t\t\t +37052477465\n                Fax:       +37052477466')
if mibBuilder.loadTexts: vel.setDescription('This is the root MIB module for VEL with OID of\n\t\t\t\t{iso org dod internet private enterprises 27993}.\n\n\t\t\t\tIANA allocated this enterprise OID (object identifier) for the\n\t\t\t\texclusive use of Vigintos Elektronika (VEL). \n\t\t\t\tOther than internet network equipment\n\t\t\t\tdistributed or licensed by VEL, no other party has any right\n\t\t\t\twhat-so-ever to distribute or license internet network equipment\n\t\t\t\twhich responds to the VEL enterprise OID or its subsidiary\n\t\t\t\tbranches. VEL reserves the right to criminally prosecute and/or\n\t\t\t\tto seek civil damages from anyone fraudently using the VEL\n\t\t\t\tenterprise OID to the full extent of the law.')
mibBuilder.exportSymbols("VEL-MIB", vel=vel, PYSNMP_MODULE_ID=vel)
