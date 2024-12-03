#
# PySNMP MIB module BTI8xx-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bti/BTI8xx-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:39:59 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, ModuleIdentity, Counter64, iso, Gauge32, Integer32, MibIdentifier, IpAddress, Bits, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "ModuleIdentity", "Counter64", "iso", "Gauge32", "Integer32", "MibIdentifier", "IpAddress", "Bits", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BTI8xx-MIB", PYSNMP_MODULE_ID=bti8xx, btiSystems=btiSystems, btiProducts=btiProducts, bti8xx=bti8xx)
