#
# PySNMP MIB module MINI-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/MINI-LINK-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 10:56:38 2024
# On host fv-az1986-135 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, Gauge32, Bits, Unsigned32, Counter32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, ObjectIdentity, TimeTicks, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Gauge32", "Bits", "Unsigned32", "Counter32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
miniLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223))
miniLink.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: miniLink.setRevisionsDescriptions(('Validated.', 'The initial version of this MIB module\n                            with OID for mini link types.',))
if mibBuilder.loadTexts: miniLink.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: miniLink.setOrganization('Ericsson')
if mibBuilder.loadTexts: miniLink.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: miniLink.setDescription('This is the top MIB for Ericsson MINI-LINK')
ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
mibBuilder.exportSymbols("MINI-LINK-MIB", miniLink=miniLink, PYSNMP_MODULE_ID=miniLink, ericsson=ericsson)
