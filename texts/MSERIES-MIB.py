#
# PySNMP MIB module MSERIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/smartoptics/MSERIES-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 03:03:53 2021
# On host fv-az42-83 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, enterprises, Unsigned32, Bits, MibIdentifier, iso, ObjectIdentity, TimeTicks, NotificationType, ModuleIdentity, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "enterprises", "Unsigned32", "Bits", "MibIdentifier", "iso", "ObjectIdentity", "TimeTicks", "NotificationType", "ModuleIdentity", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
