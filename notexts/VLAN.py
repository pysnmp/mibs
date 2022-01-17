#
# PySNMP MIB module VLAN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/VLAN
# Produced by pysmi-1.1.8 at Mon Jan 17 14:56:14 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
interface, = mibBuilder.importSymbols("ExaltComProducts", "interface")
VlanGroupT, VlanStatusT = mibBuilder.importSymbols("ExaltComm", "VlanGroupT", "VlanStatusT")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, ModuleIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Integer32, TimeTicks, Bits, Counter32, ObjectIdentity, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Integer32", "TimeTicks", "Bits", "Counter32", "ObjectIdentity", "Gauge32", "iso")
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
mibBuilder.exportSymbols("VLAN", vlan=vlan, commitVlanSettings=commitVlanSettings, vlanDefaultId=vlanDefaultId, vlanID=vlanID, vlanStatus=vlanStatus, vlanInterfacesEntry=vlanInterfacesEntry, vlanDefaultMgmtId=vlanDefaultMgmtId, vlanInterfaces=vlanInterfaces)
