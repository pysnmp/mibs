#
# PySNMP MIB module ADTRAN-AOS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-VRRP-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 13:25:34 2024
# On host fv-az693-695 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
adGenAOSRouter, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSRouter", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Unsigned32, IpAddress, TimeTicks, Counter32, Integer32, NotificationType, Bits, Counter64, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "TimeTicks", "Counter32", "Integer32", "NotificationType", "Bits", "Counter64", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSVrrpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 2, 3))
adGenAOSVrrpMib.setRevisions(('2014-07-29 00:00', '2014-04-17 00:00',))
if mibBuilder.loadTexts: adGenAOSVrrpMib.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: adGenAOSVrrpMib.setOrganization('ADTRAN, Inc.')
adGenAOSVrrp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3))
adGenAOSVrrpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0))
adGenAOSVrrpTrapCntl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1))
adGenAOSVrrpTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2), )
if mibBuilder.loadTexts: adGenAOSVrrpTable.setStatus('current')
adGenAOSVrrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpVersion"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpId"), (0, "ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddrType"))
if mibBuilder.loadTexts: adGenAOSVrrpEntry.setStatus('current')
adGenAOSVrrpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("v2", 2), ("v3", 3))))
if mibBuilder.loadTexts: adGenAOSVrrpVersion.setStatus('current')
adGenAOSVrrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: adGenAOSVrrpId.setStatus('current')
adGenAOSVrrpInetAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 3), InetAddressType())
if mibBuilder.loadTexts: adGenAOSVrrpInetAddrType.setStatus('current')
adGenAOSVrrpInetAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpInetAddr.setStatus('current')
adGenAOSVrrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("initialize", 1), ("backup", 2), ("master", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpOperStatus.setStatus('current')
adGenAOSVrrpPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSVrrpPriority.setStatus('current')
adGenAOSVrrpMasterTrapCntl = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrapCntl.setStatus('current')
adGenAOSVrrpMasterTrap = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 2, 3, 0, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus"))
if mibBuilder.loadTexts: adGenAOSVrrpMasterTrap.setStatus('current')
adGenAOSVrrpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20))
adGenAOSVrrpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1))
adGenAOSVrrpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2))
adGenAOSVrrpFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpObjectGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpTrapCfgGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpTrapGroup"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpFullCompliance = adGenAOSVrrpFullCompliance.setStatus('current')
adGenAOSVrrpReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 2, 2)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpReadOnlyCompliance = adGenAOSVrrpReadOnlyCompliance.setStatus('current')
adGenAOSVrrpObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 1)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpInetAddr"), ("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpPriority"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpObjectGroup = adGenAOSVrrpObjectGroup.setStatus('current')
adGenAOSVrrpTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 2)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrapCntl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpTrapCfgGroup = adGenAOSVrrpTrapCfgGroup.setStatus('current')
adGenAOSVrrpTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 3)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpTrapGroup = adGenAOSVrrpTrapGroup.setStatus('current')
adGenAOSVrrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 20, 1, 4)).setObjects(("ADTRAN-AOS-VRRP-MIB", "adGenAOSVrrpMasterTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSVrrpNotificationGroup = adGenAOSVrrpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-VRRP-MIB", adGenAOSVrrpFullCompliance=adGenAOSVrrpFullCompliance, adGenAOSVrrpEntry=adGenAOSVrrpEntry, adGenAOSVrrpPriority=adGenAOSVrrpPriority, adGenAOSVrrpId=adGenAOSVrrpId, adGenAOSVrrpReadOnlyCompliance=adGenAOSVrrpReadOnlyCompliance, adGenAOSVrrpMib=adGenAOSVrrpMib, adGenAOSVrrpTrapCntl=adGenAOSVrrpTrapCntl, adGenAOSVrrp=adGenAOSVrrp, adGenAOSVrrpObjectGroup=adGenAOSVrrpObjectGroup, adGenAOSVrrpInetAddr=adGenAOSVrrpInetAddr, PYSNMP_MODULE_ID=adGenAOSVrrpMib, adGenAOSVrrpCompliances=adGenAOSVrrpCompliances, adGenAOSVrrpTrap=adGenAOSVrrpTrap, adGenAOSVrrpVersion=adGenAOSVrrpVersion, adGenAOSVrrpTrapGroup=adGenAOSVrrpTrapGroup, adGenAOSVrrpInetAddrType=adGenAOSVrrpInetAddrType, adGenAOSVrrpConformance=adGenAOSVrrpConformance, adGenAOSVrrpOperStatus=adGenAOSVrrpOperStatus, adGenAOSVrrpGroups=adGenAOSVrrpGroups, adGenAOSVrrpMasterTrapCntl=adGenAOSVrrpMasterTrapCntl, adGenAOSVrrpMasterTrap=adGenAOSVrrpMasterTrap, adGenAOSVrrpNotificationGroup=adGenAOSVrrpNotificationGroup, adGenAOSVrrpTable=adGenAOSVrrpTable, adGenAOSVrrpTrapCfgGroup=adGenAOSVrrpTrapCfgGroup)
