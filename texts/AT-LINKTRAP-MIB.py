#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.8 at Thu Sep  7 14:19:23 2023
# On host fv-az407-692 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifOperStatus, ifAdminStatus, ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifOperStatus", "ifAdminStatus", "ifDescr", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, Bits, MibIdentifier, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, iso, ObjectIdentity, Counter32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Bits", "MibIdentifier", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "iso", "ObjectIdentity", "Counter32", "IpAddress", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", PYSNMP_MODULE_ID=atLinkTrap, atLinkUp=atLinkUp, atLinkTrap=atLinkTrap, atLinkDown=atLinkDown)
