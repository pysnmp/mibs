#
# PySNMP MIB module MSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:54:01 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, ObjectIdentity, NotificationType, Unsigned32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, iso, Gauge32, ModuleIdentity, Counter64, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ObjectIdentity", "NotificationType", "Unsigned32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "iso", "Gauge32", "ModuleIdentity", "Counter64", "enterprises")
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
mibBuilder.exportSymbols("MSERIES-MIB", PYSNMP_MODULE_ID=smartoptics, mseries=mseries, smartoptics=smartoptics)
