#
# PySNMP MIB module BLUECOAT-SG-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-POLICY-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 11:10:34 2024
# On host fv-az1493-704 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Bits, iso, NotificationType, Unsigned32, Gauge32, MibIdentifier, ModuleIdentity, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Bits", "iso", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier", "ModuleIdentity", "IpAddress", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BLUECOAT-SG-POLICY-MIB", devicePolicyMIBObjects=devicePolicyMIBObjects, devicePolicyMIBNotifications=devicePolicyMIBNotifications, PolicyMessageString=PolicyMessageString, PYSNMP_MODULE_ID=devicePolicyMIB, devicePolicyValues=devicePolicyValues, devicePolicyTrap=devicePolicyTrap, devicePolicyMIBNotificationsPrefix=devicePolicyMIBNotificationsPrefix, devicePolicyMIB=devicePolicyMIB, devicePolicyMessage=devicePolicyMessage)
