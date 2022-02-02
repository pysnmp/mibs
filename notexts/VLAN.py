#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.8 at Wed Feb  2 18:23:21 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanGroupT, VlanStatusT = mibBuilder.importSymbols("ExaltComm", "VlanGroupT", "VlanStatusT")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, iso, Gauge32, ModuleIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity, TimeTicks, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "Counter64", "NotificationType", "Integer32")
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
mibBuilder.exportSymbols("VLAN", vlanDefaultMgmtId=vlanDefaultMgmtId, vlanInterfacesEntry=vlanInterfacesEntry, vlan=vlan, vlanInterfaces=vlanInterfaces, vlanID=vlanID, vlanDefaultId=vlanDefaultId, vlanStatus=vlanStatus, commitVlanSettings=commitVlanSettings)
