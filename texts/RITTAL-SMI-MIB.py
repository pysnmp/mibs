#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.8 at Thu Feb  9 14:05:56 2023
# On host fv-az565-495 platform Linux version 5.15.0-1031-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, Counter64, TimeTicks, Integer32, MibIdentifier, Bits, Unsigned32, Gauge32, iso, IpAddress, ModuleIdentity, Counter32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Counter64", "TimeTicks", "Integer32", "MibIdentifier", "Bits", "Unsigned32", "Gauge32", "iso", "IpAddress", "ModuleIdentity", "Counter32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
