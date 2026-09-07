#
# PySNMP MIB module CISCOTRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOTRAP-MIB
# Source digest sha256:0ee2624530d6cd4961518b9415bb0250e6d7702152e20ffb2cff0e4c42edb797
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
cisco, = mibBuilder.importSymbols("CISCO-SMI", "cisco")
ifDescr, ifIndex, ifType = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex", "ifType")
locIfReason, = mibBuilder.importSymbols("OLD-CISCO-INTERFACES-MIB", "locIfReason")
authAddr, whyReload = mibBuilder.importSymbols("OLD-CISCO-SYSTEM-MIB", "authAddr", "whyReload")
loctcpConnElapsed, loctcpConnInBytes, loctcpConnOutBytes = mibBuilder.importSymbols("OLD-CISCO-TCP-MIB", "loctcpConnElapsed", "loctcpConnInBytes", "loctcpConnOutBytes")
tsLineUser, tslineSesType = mibBuilder.importSymbols("OLD-CISCO-TS-MIB", "tsLineUser", "tslineSesType")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmp, sysUpTime = mibBuilder.importSymbols("SNMPv2-MIB", "snmp", "sysUpTime")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tcpConnState, = mibBuilder.importSymbols("TCP-MIB", "tcpConnState")
coldStart = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
linkDown = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 3)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
linkUp = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 4)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"), ("IF-MIB", "ifType"), ("OLD-CISCO-INTERFACES-MIB", "locIfReason"))
authenticationFailure = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 5)).setObjects(("OLD-CISCO-SYSTEM-MIB", "authAddr"))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 6)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
reload = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,0)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("OLD-CISCO-SYSTEM-MIB", "whyReload"))
tcpConnectionClose = NotificationType((1, 3, 6, 1, 4, 1, 9) + (0,1)).setObjects(("OLD-CISCO-TS-MIB", "tslineSesType"), ("TCP-MIB", "tcpConnState"), ("OLD-CISCO-TCP-MIB", "loctcpConnElapsed"), ("OLD-CISCO-TCP-MIB", "loctcpConnInBytes"), ("OLD-CISCO-TCP-MIB", "loctcpConnOutBytes"), ("OLD-CISCO-TS-MIB", "tsLineUser"))
mibBuilder.exportSymbols("CISCOTRAP-MIB", authenticationFailure=authenticationFailure, coldStart=coldStart, egpNeighborLoss=egpNeighborLoss, linkDown=linkDown, linkUp=linkUp, reload=reload, tcpConnectionClose=tcpConnectionClose)
