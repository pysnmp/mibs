#
# PySNMP MIB module ASENTRIA-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/asentria/ASENTRIA-ROOT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 19:27:59 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, Counter64, Integer32, MibIdentifier, Counter32, TimeTicks, NotificationType, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Gauge32, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Counter64", "Integer32", "MibIdentifier", "Counter32", "TimeTicks", "NotificationType", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Gauge32", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
asentria = ModuleIdentity((1, 3, 6, 1, 4, 1, 3052))
asentria.setRevisions(('2010-03-09 00:00', '2007-09-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: asentria.setRevisionsDescriptions(('Updated CONTACT-INFO comment.', 'Asentria root MIB module',))
if mibBuilder.loadTexts: asentria.setLastUpdated('201003090000Z')
if mibBuilder.loadTexts: asentria.setOrganization('Asentria Corporation')
if mibBuilder.loadTexts: asentria.setContactInfo('Phone:  206-344-8800\n      Fax:    206-344-2116\n      Email:  support@asentria.com')
if mibBuilder.loadTexts: asentria.setDescription('Asentria root MIB module')
mibBuilder.exportSymbols("ASENTRIA-ROOT-MIB", asentria=asentria, PYSNMP_MODULE_ID=asentria)
