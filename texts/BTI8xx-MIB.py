#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 10:30:53 2023
# On host fv-az1153-970 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, NotificationType, Counter64, ObjectIdentity, Gauge32, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, Unsigned32, enterprises, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "NotificationType", "Counter64", "ObjectIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "Unsigned32", "enterprises", "IpAddress", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bti8xx = ModuleIdentity((1, 3, 6, 1, 4, 1, 30005, 1, 7))
bti8xx.setRevisions(('2013-12-26 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bti8xx.setRevisionsDescriptions(('Initial version of MIB.',))
if mibBuilder.loadTexts: bti8xx.setLastUpdated('201312261200Z')
if mibBuilder.loadTexts: bti8xx.setOrganization('Actus Networks Inc.')
if mibBuilder.loadTexts: bti8xx.setContactInfo('Technical Support\n\t\t ')
if mibBuilder.loadTexts: bti8xx.setDescription('This is a top-level MIB for BTI800 whose purpose is to lay out\n                  the top-level objects in the OID hierarchy from which\n                  BTI MIB OIDs descend.')
btiSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 30005))
btiProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 30005, 1))
mibBuilder.exportSymbols("BTI8xx-MIB", btiProducts=btiProducts, bti8xx=bti8xx, PYSNMP_MODULE_ID=bti8xx, btiSystems=btiSystems)
