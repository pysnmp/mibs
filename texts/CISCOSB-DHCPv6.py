#
# PySNMP MIB module CISCOSB-DHCPv6 (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-DHCPv6
# Source digest sha256:14b70dcd9e590760f49c1e5a47426901305868343fff4f694fe129bcc5ccedbf
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
InetAddress, InetAddressIPv6, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressIPv6", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, MacAddress, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention", "TruthValue")
rlDhcpv6 = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214))
if mibBuilder.loadTexts: rlDhcpv6.setLastUpdated('2006-04-02 00:00')
if mibBuilder.loadTexts: rlDhcpv6.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlDhcpv6.setContactInfo('Postal: 170 West Tasman Drive\n        San Jose , CA 95134-1706\n        USA\n\n        \n        Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlDhcpv6.setDescription('The private MIB module definition for DHCP v6 features.')
rlDhcpv6Common = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1))
rlDhcpv6Client = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 2))
rlDhcpv6Relay = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 3))
rlDhcpv6DuidEn = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 214, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(7, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setStatus('current')
if mibBuilder.loadTexts: rlDhcpv6DuidEn.setDescription('')
mibBuilder.exportSymbols("CISCOSB-DHCPv6", PYSNMP_MODULE_ID=rlDhcpv6, rlDhcpv6=rlDhcpv6, rlDhcpv6Client=rlDhcpv6Client, rlDhcpv6Common=rlDhcpv6Common, rlDhcpv6DuidEn=rlDhcpv6DuidEn, rlDhcpv6Relay=rlDhcpv6Relay)
