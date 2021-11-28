#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 19:57:21 2021
# On host fv-az83-233 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifDescr, ifOperStatus, ifAdminStatus, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifOperStatus", "ifAdminStatus", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, iso, Counter32, MibIdentifier, ModuleIdentity, TimeTicks, Unsigned32, Bits, Counter64, IpAddress, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "iso", "Counter32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Unsigned32", "Bits", "Counter64", "IpAddress", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkDown=atLinkDown, atLinkUp=atLinkUp, PYSNMP_MODULE_ID=atLinkTrap, atLinkTrap=atLinkTrap)
