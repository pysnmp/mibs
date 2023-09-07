#
# PySNMP MIB module MINI-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/MINI-LINK-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:24:33 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Counter32, Bits, ObjectIdentity, Unsigned32, ModuleIdentity, Gauge32, Counter64, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Counter32", "Bits", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "Gauge32", "Counter64", "MibIdentifier", "NotificationType")
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
mibBuilder.exportSymbols("MINI-LINK-MIB", PYSNMP_MODULE_ID=miniLink, miniLink=miniLink, ericsson=ericsson)
