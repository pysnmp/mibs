#
# PySNMP MIB module BLUECOAT-SG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 22:04:21 2022
# On host fv-az126-754 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Counter64, Integer32, Gauge32, Counter32, iso, TimeTicks, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Counter64", "Integer32", "Gauge32", "Counter32", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGFailoverMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 13))
bluecoatSGFailoverMIB.setRevisions(('2011-12-20 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setRevisionsDescriptions(('Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setLastUpdated('201112200300Z')
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setDescription('The failover MIB is used to monitor\n                         changes in the failover state of the SG appliance.')
bluecoatSgFailoverMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1))
bluecoatSgFailoverMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2))
bluecoatSgFailoverMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0))
class FailoverMessageString(TextualConvention, OctetString):
    description = 'The message describing a change in failover state\n                          of the SG system.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

bluecoatSgFailoverValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1))
bluecoatSgFailoverMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1, 1), FailoverMessageString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bluecoatSgFailoverMessage.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgFailoverMessage.setDescription('The custom message generated for this change in\n                         failover state.')
bluecoatSgFailoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0, 1)).setObjects(("BLUECOAT-SG-FAILOVER-MIB", "bluecoatSgFailoverMessage"))
if mibBuilder.loadTexts: bluecoatSgFailoverTrap.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgFailoverTrap.setDescription('A notification is generated when the failover state\n                         of the SG system changes.')
mibBuilder.exportSymbols("BLUECOAT-SG-FAILOVER-MIB", PYSNMP_MODULE_ID=bluecoatSGFailoverMIB, bluecoatSgFailoverMessage=bluecoatSgFailoverMessage, FailoverMessageString=FailoverMessageString, bluecoatSgFailoverTrap=bluecoatSgFailoverTrap, bluecoatSgFailoverMIBNotificationsPrefix=bluecoatSgFailoverMIBNotificationsPrefix, bluecoatSgFailoverMIBObjects=bluecoatSgFailoverMIBObjects, bluecoatSgFailoverValues=bluecoatSgFailoverValues, bluecoatSgFailoverMIBNotifications=bluecoatSgFailoverMIBNotifications, bluecoatSGFailoverMIB=bluecoatSGFailoverMIB)
