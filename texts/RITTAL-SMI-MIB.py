#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.12 at Tue May 28 12:39:53 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, MibIdentifier, enterprises, IpAddress, Bits, Gauge32, ObjectIdentity, ModuleIdentity, Unsigned32, Counter64, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "MibIdentifier", "enterprises", "IpAddress", "Bits", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter64", "iso", "Integer32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rittal = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606))
rittal.setRevisions(('2011-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rittal.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rittal.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: rittal.setOrganization('RITTAL GmbH & Co. KG')
if mibBuilder.loadTexts: rittal.setContactInfo('www.rittal.de\n\n                            RITTAL GmbH & Co. KG\n                            Forschung & Entwicklung\n                            Auf dem Stuetzelberg\n                            D-35745 Herborn\n                            Germany, Europe\n\n                            +49(0)2772 5050\n                            info@rittal.de')
if mibBuilder.loadTexts: rittal.setDescription('The Structure of Management Information Base for the Rittal enterprise.')
mibBuilder.exportSymbols("RITTAL-SMI-MIB", rittal=rittal, PYSNMP_MODULE_ID=rittal)
