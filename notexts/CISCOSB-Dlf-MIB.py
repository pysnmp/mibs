#
# PySNMP MIB module CISCOSB-Dlf-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-Dlf-MIB
# Source digest sha256:7603a5a6125fc2121b722795cc297e91abe62bee11b4f91383a4afcb0cd9d839
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDlf = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135))
if mibBuilder.loadTexts: rlDlf.setLastUpdated('2008-09-15 12:34')
if mibBuilder.loadTexts: rlDlf.setOrganization('Cisco Systems, Inc.')
rlDlfPortList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 135, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDlfPortList.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-Dlf-MIB", PYSNMP_MODULE_ID=rlDlf, rlDlf=rlDlf, rlDlfPortList=rlDlfPortList)
