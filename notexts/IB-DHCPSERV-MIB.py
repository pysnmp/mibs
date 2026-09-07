#
# PySNMP MIB module IB-DHCPSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source IB-DHCPSERV-MIB
# Source digest sha256:9563b6e2c0dfd9d92362fdb87063c6bf4883a2017231ab48233a5d439f01ec50
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
IbString, ibDHCPServ = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibDHCPServ")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibDhcpv4ServerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 9999, 1))
ibDhcpv4ServerModule.setRevisions(('2011-07-15 00:00',))
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setLastUpdated('2011-07-15 00:00')
if mibBuilder.loadTexts: ibDhcpv4ServerModule.setOrganization('Infoblox')
ibDhcpv4ServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1))
ibDhcpv4ServerSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1))
ibDhcpv4ServerSystemDescr = MibScalar((1, 3, 6, 1, 4, 1, 9999, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpv4ServerSystemDescr.setStatus('current')
mibBuilder.exportSymbols("IB-DHCPSERV-MIB", PYSNMP_MODULE_ID=ibDhcpv4ServerModule, ibDhcpv4ServerModule=ibDhcpv4ServerModule, ibDhcpv4ServerObjects=ibDhcpv4ServerObjects, ibDhcpv4ServerSystem=ibDhcpv4ServerSystem, ibDhcpv4ServerSystemDescr=ibDhcpv4ServerSystemDescr)
