#
# PySNMP MIB module BLUECOAT-SG-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-POLICY-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 15:24:31 2023
# On host fv-az407-858 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Counter64, ObjectIdentity, ModuleIdentity, iso, Gauge32, TimeTicks, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Counter64", "ObjectIdentity", "ModuleIdentity", "iso", "Gauge32", "TimeTicks", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
devicePolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 6))
devicePolicyMIB.setRevisions(('2007-11-05 03:00', '2002-08-28 03:00',))
if mibBuilder.loadTexts: devicePolicyMIB.setLastUpdated('200711050300Z')
if mibBuilder.loadTexts: devicePolicyMIB.setOrganization('Blue Coat Systems, Inc.')
devicePolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1))
devicePolicyMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2))
devicePolicyMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0))
class PolicyMessageString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

devicePolicyValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1))
devicePolicyMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1, 1), PolicyMessageString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: devicePolicyMessage.setStatus('current')
devicePolicyTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0, 1)).setObjects(("BLUECOAT-SG-POLICY-MIB", "devicePolicyMessage"))
if mibBuilder.loadTexts: devicePolicyTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-POLICY-MIB", devicePolicyMIBNotificationsPrefix=devicePolicyMIBNotificationsPrefix, devicePolicyValues=devicePolicyValues, devicePolicyMIBNotifications=devicePolicyMIBNotifications, PYSNMP_MODULE_ID=devicePolicyMIB, devicePolicyMessage=devicePolicyMessage, devicePolicyTrap=devicePolicyTrap, devicePolicyMIB=devicePolicyMIB, PolicyMessageString=PolicyMessageString, devicePolicyMIBObjects=devicePolicyMIBObjects)
