#
# PySNMP MIB module BLUECOAT-SG-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-POLICY-MIB
# Produced by pysmi-1.1.8 at Tue Sep 12 07:21:42 2023
# On host fv-az749-158 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, ModuleIdentity, TimeTicks, iso, Counter32, Gauge32, IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "ModuleIdentity", "TimeTicks", "iso", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
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
mibBuilder.exportSymbols("BLUECOAT-SG-POLICY-MIB", PolicyMessageString=PolicyMessageString, PYSNMP_MODULE_ID=devicePolicyMIB, devicePolicyMIBObjects=devicePolicyMIBObjects, devicePolicyMIBNotifications=devicePolicyMIBNotifications, devicePolicyValues=devicePolicyValues, devicePolicyMIB=devicePolicyMIB, devicePolicyMIBNotificationsPrefix=devicePolicyMIBNotificationsPrefix, devicePolicyMessage=devicePolicyMessage, devicePolicyTrap=devicePolicyTrap)
