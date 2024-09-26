#
# PySNMP MIB module RITTAL-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/rittal/RITTAL-SMI
# Produced by pysmi-1.1.12 at Thu Sep 26 02:18:25 2024
# On host fv-az1144-917 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, TimeTicks, Counter32, ModuleIdentity, MibIdentifier, NotificationType, Gauge32, Unsigned32, iso, ObjectIdentity, enterprises, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Gauge32", "Unsigned32", "iso", "ObjectIdentity", "enterprises", "Integer32", "Counter64")
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
