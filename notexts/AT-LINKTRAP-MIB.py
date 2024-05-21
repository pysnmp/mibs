#
# PySNMP MIB module AT-LINKTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LINKTRAP-MIB
# Produced by pysmi-1.1.12 at Tue May 21 06:52:14 2024
# On host fv-az1501-253 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ifAdminStatus, ifOperStatus, ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifAdminStatus", "ifOperStatus", "ifIndex", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, NotificationType, Counter32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, Integer32, IpAddress, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atLinkTrap = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25))
atLinkTrap.setRevisions(('2014-04-04 00:00',))
if mibBuilder.loadTexts: atLinkTrap.setLastUpdated('201404040000Z')
if mibBuilder.loadTexts: atLinkTrap.setOrganization('Allied Telesis, Inc.')
atLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkDown.setStatus('current')
atLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 25, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: atLinkUp.setStatus('current')
mibBuilder.exportSymbols("AT-LINKTRAP-MIB", atLinkUp=atLinkUp, atLinkTrap=atLinkTrap, PYSNMP_MODULE_ID=atLinkTrap, atLinkDown=atLinkDown)
