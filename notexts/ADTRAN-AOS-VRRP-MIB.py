#
# PySNMP MIB module ADTRAN-AOS-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-VRRP-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:53:28 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
adGenAOSRouter, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSRouter", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, Gauge32, Integer32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, ObjectIdentity, iso, Bits, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "Gauge32", "Integer32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "ObjectIdentity", "iso", "Bits", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-AOS-VRRP-MIB", adGenAOSVrrpTrap=adGenAOSVrrpTrap, adGenAOSVrrpReadOnlyCompliance=adGenAOSVrrpReadOnlyCompliance, PYSNMP_MODULE_ID=adGenAOSVrrpMib, adGenAOSVrrpMasterTrap=adGenAOSVrrpMasterTrap, adGenAOSVrrpTrapCfgGroup=adGenAOSVrrpTrapCfgGroup, adGenAOSVrrpVersion=adGenAOSVrrpVersion, adGenAOSVrrpFullCompliance=adGenAOSVrrpFullCompliance, adGenAOSVrrpPriority=adGenAOSVrrpPriority, adGenAOSVrrpTrapCntl=adGenAOSVrrpTrapCntl, adGenAOSVrrpMib=adGenAOSVrrpMib, adGenAOSVrrpCompliances=adGenAOSVrrpCompliances, adGenAOSVrrpTrapGroup=adGenAOSVrrpTrapGroup, adGenAOSVrrpTable=adGenAOSVrrpTable, adGenAOSVrrp=adGenAOSVrrp, adGenAOSVrrpGroups=adGenAOSVrrpGroups, adGenAOSVrrpInetAddr=adGenAOSVrrpInetAddr, adGenAOSVrrpOperStatus=adGenAOSVrrpOperStatus, adGenAOSVrrpEntry=adGenAOSVrrpEntry, adGenAOSVrrpMasterTrapCntl=adGenAOSVrrpMasterTrapCntl, adGenAOSVrrpId=adGenAOSVrrpId, adGenAOSVrrpInetAddrType=adGenAOSVrrpInetAddrType, adGenAOSVrrpNotificationGroup=adGenAOSVrrpNotificationGroup, adGenAOSVrrpObjectGroup=adGenAOSVrrpObjectGroup, adGenAOSVrrpConformance=adGenAOSVrrpConformance)
