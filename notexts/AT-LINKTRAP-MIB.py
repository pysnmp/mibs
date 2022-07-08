#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:17:07 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifIndex, ifOperStatus, ifDescr, ifAdminStatus = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifOperStatus", "ifDescr", "ifAdminStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, Integer32, Bits, TimeTicks, MibIdentifier, Counter64, ObjectIdentity, IpAddress, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Integer32", "Bits", "TimeTicks", "MibIdentifier", "Counter64", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atLinkTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25))
atLinkTrap.setRevisions(('2014-04-04 00:00',))
if mibBuilder.loadTexts: atLinkTrap.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: atLinkTrap.setOrganization('Allied Telesis, Inc.')
atLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkDown.setStatus('current')
atLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkUp.setStatus('current')
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkDown=atLinkDown, atLinkUp=atLinkUp, PYSNMP_MODULE_ID=atLinkTrap, atLinkTrap=atLinkTrap)
