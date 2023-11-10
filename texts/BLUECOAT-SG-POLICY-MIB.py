#
# PySNMP MIB module BLUECOAT-SG-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-POLICY-MIB
# Produced by pysmi-1.1.10 at Fri Nov 10 11:09:09 2023
# On host fv-az1251-57 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, IpAddress, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter64, TimeTicks, NotificationType, Gauge32, iso, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "iso", "Integer32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
devicePolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 6))
devicePolicyMIB.setRevisions(('2007-11-05 03:00', '2002-08-28 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: devicePolicyMIB.setRevisionsDescriptions(('Minor corrections and reformatting. Changed the\n                         trap OID for compatibility with SNMPv1.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: devicePolicyMIB.setLastUpdated('200711050300Z')
if mibBuilder.loadTexts: devicePolicyMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: devicePolicyMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: devicePolicyMIB.setDescription('The policy MIB is used to monitor policy violations.')
devicePolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1))
devicePolicyMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2))
devicePolicyMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0))
class PolicyMessageString(TextualConvention, OctetString):
    description = 'The message that the user would enter while setting\n                         the policy.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

devicePolicyValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1))
devicePolicyMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 6, 1, 1, 1), PolicyMessageString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: devicePolicyMessage.setStatus('current')
if mibBuilder.loadTexts: devicePolicyMessage.setDescription('The custom message the user entered for this policy')
devicePolicyTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 6, 2, 0, 1)).setObjects(("BLUECOAT-SG-POLICY-MIB", "devicePolicyMessage"))
if mibBuilder.loadTexts: devicePolicyTrap.setStatus('current')
if mibBuilder.loadTexts: devicePolicyTrap.setDescription('A notification is generated when triggered by policy')
mibBuilder.exportSymbols("BLUECOAT-SG-POLICY-MIB", devicePolicyMIB=devicePolicyMIB, devicePolicyMessage=devicePolicyMessage, PolicyMessageString=PolicyMessageString, PYSNMP_MODULE_ID=devicePolicyMIB, devicePolicyMIBNotifications=devicePolicyMIBNotifications, devicePolicyValues=devicePolicyValues, devicePolicyMIBNotificationsPrefix=devicePolicyMIBNotificationsPrefix, devicePolicyTrap=devicePolicyTrap, devicePolicyMIBObjects=devicePolicyMIBObjects)
