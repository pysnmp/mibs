#
# PySNMP MIB module ASENTRIA-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/asentria/ASENTRIA-ROOT-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 11:37:21 2024
# On host fv-az842-370 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, iso, enterprises, ObjectIdentity, Integer32, TimeTicks, IpAddress, Bits, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "iso", "enterprises", "ObjectIdentity", "Integer32", "TimeTicks", "IpAddress", "Bits", "Gauge32", "Unsigned32")
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
