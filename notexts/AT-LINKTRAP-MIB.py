#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.10 at Fri Oct 27 07:35:20 2023
# On host fv-az1236-588 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifAdminStatus, ifIndex, ifOperStatus, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifAdminStatus", "ifIndex", "ifOperStatus", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, Integer32, MibIdentifier, iso, Gauge32, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Integer32", "MibIdentifier", "iso", "Gauge32", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atLinkTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25))
atLinkTrap.setRevisions(('2014-04-04 00:00',))
if mibBuilder.loadTexts: atLinkTrap.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: atLinkTrap.setOrganization('Allied Telesis, Inc.')
atLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkDown.setStatus('current')
atLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkUp.setStatus('current')
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkTrap=atLinkTrap, atLinkUp=atLinkUp, atLinkDown=atLinkDown, PYSNMP_MODULE_ID=atLinkTrap)
