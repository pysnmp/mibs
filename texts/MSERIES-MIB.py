#
# PySNMP MIB module MSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-MIB
# Produced by pysmi-1.1.12 at Tue Jun 18 01:44:01 2024
# On host fv-az1446-447 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, iso, Gauge32, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, ObjectIdentity, Counter32, NotificationType, Counter64, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "iso", "Gauge32", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "Counter64", "TimeTicks", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smartoptics = ModuleIdentity((1, 3, 6, 1, 4, 1, 30826))
smartoptics.setRevisions(('2014-02-12 13:27',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smartoptics.setRevisionsDescriptions(('The initial revision.',))
if mibBuilder.loadTexts: smartoptics.setLastUpdated('201402121327Z')
if mibBuilder.loadTexts: smartoptics.setOrganization('SmartOptics')
if mibBuilder.loadTexts: smartoptics.setContactInfo('http://www.smartoptics.com')
if mibBuilder.loadTexts: smartoptics.setDescription('This is the enterprise specific MIB for SmartOptics M-Series.\n\n                                 The root of the OID sub-tree assigned to SmartOptics.')
mseries = ObjectIdentity((1, 3, 6, 1, 4, 1, 30826, 1))
if mibBuilder.loadTexts: mseries.setStatus('current')
if mibBuilder.loadTexts: mseries.setDescription('The M-Series product root.')
mibBuilder.exportSymbols("MSERIES-MIB", PYSNMP_MODULE_ID=smartoptics, smartoptics=smartoptics, mseries=mseries)
