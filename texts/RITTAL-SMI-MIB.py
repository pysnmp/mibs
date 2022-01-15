#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:16 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32, iso, ObjectIdentity, ModuleIdentity, Integer32, Counter64, Gauge32, Bits, Counter32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32", "iso", "ObjectIdentity", "ModuleIdentity", "Integer32", "Counter64", "Gauge32", "Bits", "Counter32", "NotificationType", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rittal = ModuleIdentity((1, 3, 6, 1, 4, 1, 2606))
rittal.setRevisions(('2011-04-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rittal.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: rittal.setLastUpdated('201104010000Z')
if mibBuilder.loadTexts: rittal.setOrganization('RITTAL GmbH & Co. KG')
if mibBuilder.loadTexts: rittal.setContactInfo('www.rittal.de\n\n                            RITTAL GmbH & Co. KG\n                            Forschung & Entwicklung\n                            Auf dem Stuetzelberg\n                            D-35745 Herborn\n                            Germany, Europe\n\n                            +49(0)2772 5050\n                            info@rittal.de')
if mibBuilder.loadTexts: rittal.setDescription('The Structure of Management Information Base for the Rittal enterprise.')
mibBuilder.exportSymbols("RITTAL-SMI-MIB", PYSNMP_MODULE_ID=rittal, rittal=rittal)
