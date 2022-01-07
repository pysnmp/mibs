#
# PySNMP MIB module ADTRAN-AOS-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-FAN-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 17:31:17 2022
# On host fv-az126-670 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32, Integer32, Counter64, IpAddress, Counter32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32", "Integer32", "Counter64", "IpAddress", "Counter32", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSFanMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 8))
adGenAOSFanMib.setRevisions(('2013-10-22 00:00',))
if mibBuilder.loadTexts: adGenAOSFanMib.setLastUpdated('201310220000Z')
if mibBuilder.loadTexts: adGenAOSFanMib.setOrganization('ADTRAN, Inc.')
adGenAOSFan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8))
adGenAOSFanTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0))
adGenAOSFanTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1))
adGenAOSFanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2))
adGenAOSFanTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSFanTrapEnable.setStatus('current')
adGenAOSFanNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSFanNumber.setStatus('current')
adGenAOSFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if mibBuilder.loadTexts: adGenAOSFanFailure.setStatus('current')
adGenAOSFanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17))
adGenAOSFanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1))
adGenAOSFanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2))
adGenAOSFanFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapCfgGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanFullCompliance = adGenAOSFanFullCompliance.setStatus('current')
adGenAOSFanTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapCfgGroup = adGenAOSFanTrapCfgGroup.setStatus('current')
adGenAOSFanTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 2)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapGroup = adGenAOSFanTrapGroup.setStatus('current')
adGenAOSFanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 3)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanNotificationGroup = adGenAOSFanNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-FAN-MIB", adGenAOSFanTrapGroup=adGenAOSFanTrapGroup, adGenAOSFanMib=adGenAOSFanMib, adGenAOSFanInfo=adGenAOSFanInfo, adGenAOSFanFailure=adGenAOSFanFailure, adGenAOSFanFullCompliance=adGenAOSFanFullCompliance, adGenAOSFanNumber=adGenAOSFanNumber, adGenAOSFanCompliances=adGenAOSFanCompliances, adGenAOSFanTrap=adGenAOSFanTrap, adGenAOSFanConformance=adGenAOSFanConformance, adGenAOSFanGroups=adGenAOSFanGroups, adGenAOSFanNotificationGroup=adGenAOSFanNotificationGroup, adGenAOSFanTrapCfgGroup=adGenAOSFanTrapCfgGroup, PYSNMP_MODULE_ID=adGenAOSFanMib, adGenAOSFanTrapEnable=adGenAOSFanTrapEnable, adGenAOSFan=adGenAOSFan, adGenAOSFanTrapControl=adGenAOSFanTrapControl)
