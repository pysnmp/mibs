#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 20:05:38 2021
# On host fv-az42-715 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifAdminStatus, ifOperStatus, ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifAdminStatus", "ifOperStatus", "ifIndex", "ifDescr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, IpAddress, MibIdentifier, ObjectIdentity, Counter64, NotificationType, ModuleIdentity, Counter32, iso, Gauge32, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "NotificationType", "ModuleIdentity", "Counter32", "iso", "Gauge32", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atLinkTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25))
atLinkTrap.setRevisions(('2014-04-04 00:00',))
if mibBuilder.loadTexts: atLinkTrap.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: atLinkTrap.setOrganization('Allied Telesis, Inc.')
atLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkDown.setStatus('current')
atLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkUp.setStatus('current')
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkTrap=atLinkTrap, PYSNMP_MODULE_ID=atLinkTrap, atLinkDown=atLinkDown, atLinkUp=atLinkUp)
