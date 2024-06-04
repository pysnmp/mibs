#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 08:02:23 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifDescr, ifOperStatus, ifIndex, ifAdminStatus = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifOperStatus", "ifIndex", "ifAdminStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter32, Integer32, iso, Counter64, NotificationType, ModuleIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter32", "Integer32", "iso", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atLinkTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25))
atLinkTrap.setRevisions(('2014-04-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atLinkTrap.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: atLinkTrap.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: atLinkTrap.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: atLinkTrap.setContactInfo('  http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atLinkTrap.setDescription('The AT-LINKTRAP MIB contains objects for link\n                up and down traps.')
atLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkDown.setStatus('current')
if mibBuilder.loadTexts: atLinkDown.setDescription('A trap generated when an interface is linked down.')
atLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkUp.setStatus('current')
if mibBuilder.loadTexts: atLinkUp.setDescription('A trap generated when an interface is linked up.')
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkTrap=atLinkTrap, atLinkDown=atLinkDown, PYSNMP_MODULE_ID=atLinkTrap, atLinkUp=atLinkUp)
