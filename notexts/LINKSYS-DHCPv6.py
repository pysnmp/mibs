#
# PySNMP MIB module LINKSYS-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source LINKSYS-DHCPv6
# Source digest sha256:1fe30023834e3bb70697f8df0b89ed7685dfca4400bf12f7bc5aca55b3f7d96a
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('2006-04-02 00:00')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
mibBuilder.exportSymbols("LINKSYS-DHCPv6", PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6=rlDhcpv6, rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6Relay=rlDhcpv6Relay)
