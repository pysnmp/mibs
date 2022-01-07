#
# PySNMP MIB module ASENTRIA-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/asentria/ASENTRIA-ROOT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:54:27 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter64, enterprises, NotificationType, Bits, Unsigned32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "enterprises", "NotificationType", "Bits", "Unsigned32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Integer32", "ModuleIdentity", "iso")
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
