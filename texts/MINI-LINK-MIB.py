#
# PySNMP MIB module MINI-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/MINI-LINK-MIB
# Produced by pysmi-1.1.8 at Tue Feb  1 21:02:47 2022
# On host fv-az121-510 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Counter32, TimeTicks, enterprises, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, Integer32, NotificationType, MibIdentifier, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Counter32", "TimeTicks", "enterprises", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "Integer32", "NotificationType", "MibIdentifier", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
miniLink = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223))
miniLink.setRevisions(('2016-03-09 12:30', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: miniLink.setRevisionsDescriptions(('Validated.', 'The initial version of this MIB module\n                            with OID for mini link types.',))
if mibBuilder.loadTexts: miniLink.setLastUpdated('201603091230Z')
if mibBuilder.loadTexts: miniLink.setOrganization('Ericsson')
if mibBuilder.loadTexts: miniLink.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: miniLink.setDescription('This is the top MIB for Ericsson MINI-LINK')
ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
mibBuilder.exportSymbols("MINI-LINK-MIB", ericsson=ericsson, miniLink=miniLink, PYSNMP_MODULE_ID=miniLink)
