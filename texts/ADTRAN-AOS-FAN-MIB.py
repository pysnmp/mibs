#
# PySNMP MIB module ADTRAN-AOS-FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-FAN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 19:56:00 2021
# On host fv-az33-735 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, Counter32, NotificationType, Bits, TimeTicks, iso, Integer32, Counter64, MibIdentifier, ModuleIdentity, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "NotificationType", "Bits", "TimeTicks", "iso", "Integer32", "Counter64", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSFanMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 8))
adGenAOSFanMib.setRevisions(('2013-10-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSFanMib.setRevisionsDescriptions(('Created the adGenAosFan MIB. Revision R10.11',))
if mibBuilder.loadTexts: adGenAOSFanMib.setLastUpdated('201310220000Z')
if mibBuilder.loadTexts: adGenAOSFanMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSFanMib.setContactInfo('        Technical Support Dept.\n            \t\tPostal: ADTRAN, Inc.\n                    901 Explorer Blvd.\n                    Huntsville, AL 35806\n\n               Tel: +1 800 726-8663\n               Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSFanMib.setDescription('The MIB module defines fan configuration information and traps for AdtranOS products.')
adGenAOSFan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8))
adGenAOSFanTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0))
adGenAOSFanTrapControl = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1))
adGenAOSFanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2))
adGenAOSFanTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSFanTrapEnable.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanTrapEnable.setDescription('This variable indicates whether the system produces\n            the fan failure trap.')
adGenAOSFanNumber = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSFanNumber.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanNumber.setDescription("A numerical representation of the chassis's fan.")
adGenAOSFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8, 0, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if mibBuilder.loadTexts: adGenAOSFanFailure.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanFailure.setDescription('A fan failure trap signifies that one of the fans inside the chassis has failed.')
adGenAOSFanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17))
adGenAOSFanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1))
adGenAOSFanCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2))
adGenAOSFanFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 2, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapCfgGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapGroup"), ("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanFullCompliance = adGenAOSFanFullCompliance.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanFullCompliance.setDescription('The compliance statement for SNMP entities which implement\n        version 2 of the adGenAosFan MIB. When this MIB is implemented\n        with support for read-write, then such an implementation can claim\n        full compliance.')
adGenAOSFanTrapCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 1)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanTrapEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapCfgGroup = adGenAOSFanTrapCfgGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanTrapCfgGroup.setDescription('This group contains the objects necessary to enable/disable\n            fan failure traps.')
adGenAOSFanTrapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 2)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanTrapGroup = adGenAOSFanTrapGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanTrapGroup.setDescription('The objects necessary to control fan notification messages.')
adGenAOSFanNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 17, 1, 3)).setObjects(("ADTRAN-AOS-FAN-MIB", "adGenAOSFanFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFanNotificationGroup = adGenAOSFanNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFanNotificationGroup.setDescription("Traps which may be used to enhance event driven\n            management of the chassis's fan.")
mibBuilder.exportSymbols("ADTRAN-AOS-FAN-MIB", adGenAOSFanCompliances=adGenAOSFanCompliances, adGenAOSFanTrapCfgGroup=adGenAOSFanTrapCfgGroup, adGenAOSFanNotificationGroup=adGenAOSFanNotificationGroup, adGenAOSFanMib=adGenAOSFanMib, PYSNMP_MODULE_ID=adGenAOSFanMib, adGenAOSFanNumber=adGenAOSFanNumber, adGenAOSFanFailure=adGenAOSFanFailure, adGenAOSFanConformance=adGenAOSFanConformance, adGenAOSFanTrapEnable=adGenAOSFanTrapEnable, adGenAOSFanGroups=adGenAOSFanGroups, adGenAOSFanTrapGroup=adGenAOSFanTrapGroup, adGenAOSFanFullCompliance=adGenAOSFanFullCompliance, adGenAOSFanInfo=adGenAOSFanInfo, adGenAOSFanTrapControl=adGenAOSFanTrapControl, adGenAOSFan=adGenAOSFan, adGenAOSFanTrap=adGenAOSFanTrap)
