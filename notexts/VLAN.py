#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.12 at Thu Apr  4 13:38:01 2024
# On host fv-az984-576 platform Linux version 6.5.0-1017-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanStatusT, VlanGroupT = mibBuilder.importSymbols("ExaltComm", "VlanStatusT", "VlanGroupT")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Bits, TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, IpAddress, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vlan = ObjectIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3))
if mibBuilder.loadTexts: vlan.setStatus('current')
vlanStatus = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1), VlanStatusT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanStatus.setStatus('current')
vlanDefaultMgmtId = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultMgmtId.setStatus('current')
vlanInterfaces = MibTable((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6), )
if mibBuilder.loadTexts: vlanInterfaces.setStatus('current')
vlanInterfacesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1), ).setIndexNames((0, "VLAN", "vlanDefaultId"))
if mibBuilder.loadTexts: vlanInterfacesEntry.setStatus('current')
vlanDefaultId = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultId.setStatus('current')
vlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanID.setStatus('current')
commitVlanSettings = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 200))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: commitVlanSettings.setStatus('current')
mibBuilder.exportSymbols("VLAN", commitVlanSettings=commitVlanSettings, vlanInterfacesEntry=vlanInterfacesEntry, vlan=vlan, vlanDefaultId=vlanDefaultId, vlanDefaultMgmtId=vlanDefaultMgmtId, vlanStatus=vlanStatus, vlanID=vlanID, vlanInterfaces=vlanInterfaces)
