#
# PySNMP MIB module ADTRAN-AOS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-VRRP-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:07:34 2022
# On host fv-az445-955 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
adGenAOSRouter, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSRouter", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter64, ObjectIdentity, NotificationType, TimeTicks, Integer32, Counter32, Unsigned32, iso, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter64", "ObjectIdentity", "NotificationType", "TimeTicks", "Integer32", "Counter32", "Unsigned32", "iso", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity")
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
mibBuilder.exportSymbols("ADTRAN-AOS-VRRP-MIB", adGenAOSVrrpInetAddr=adGenAOSVrrpInetAddr, adGenAOSVrrpTable=adGenAOSVrrpTable, adGenAOSVrrpTrapCntl=adGenAOSVrrpTrapCntl, adGenAOSVrrpEntry=adGenAOSVrrpEntry, adGenAOSVrrpPriority=adGenAOSVrrpPriority, adGenAOSVrrpMib=adGenAOSVrrpMib, adGenAOSVrrpGroups=adGenAOSVrrpGroups, adGenAOSVrrpCompliances=adGenAOSVrrpCompliances, adGenAOSVrrp=adGenAOSVrrp, adGenAOSVrrpVersion=adGenAOSVrrpVersion, adGenAOSVrrpInetAddrType=adGenAOSVrrpInetAddrType, adGenAOSVrrpTrap=adGenAOSVrrpTrap, adGenAOSVrrpId=adGenAOSVrrpId, adGenAOSVrrpMasterTrap=adGenAOSVrrpMasterTrap, adGenAOSVrrpTrapGroup=adGenAOSVrrpTrapGroup, adGenAOSVrrpMasterTrapCntl=adGenAOSVrrpMasterTrapCntl, adGenAOSVrrpTrapCfgGroup=adGenAOSVrrpTrapCfgGroup, adGenAOSVrrpObjectGroup=adGenAOSVrrpObjectGroup, adGenAOSVrrpNotificationGroup=adGenAOSVrrpNotificationGroup, adGenAOSVrrpReadOnlyCompliance=adGenAOSVrrpReadOnlyCompliance, adGenAOSVrrpFullCompliance=adGenAOSVrrpFullCompliance, PYSNMP_MODULE_ID=adGenAOSVrrpMib, adGenAOSVrrpConformance=adGenAOSVrrpConformance, adGenAOSVrrpOperStatus=adGenAOSVrrpOperStatus)
