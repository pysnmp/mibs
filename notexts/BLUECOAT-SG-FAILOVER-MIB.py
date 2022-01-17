#
# PySNMP MIB module BLUECOAT-SG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 22:00:44 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, MibIdentifier, Integer32, Counter32, Counter64, ModuleIdentity, Bits, IpAddress, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibIdentifier", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "Bits", "IpAddress", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGFailoverMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 13))
bluecoatSGFailoverMIB.setRevisions(('2011-12-20 03:00',))
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setLastUpdated('201112200300Z')
if mibBuilder.loadTexts: bluecoatSGFailoverMIB.setOrganization('Blue Coat Systems, Inc.')
bluecoatSgFailoverMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1))
bluecoatSgFailoverMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2))
bluecoatSgFailoverMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0))
class FailoverMessageString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

bluecoatSgFailoverValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1))
bluecoatSgFailoverMessage = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 13, 1, 1, 1), FailoverMessageString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bluecoatSgFailoverMessage.setStatus('current')
bluecoatSgFailoverTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 13, 2, 0, 1)).setObjects(("BLUECOAT-SG-FAILOVER-MIB", "bluecoatSgFailoverMessage"))
if mibBuilder.loadTexts: bluecoatSgFailoverTrap.setStatus('current')
mibBuilder.exportSymbols("BLUECOAT-SG-FAILOVER-MIB", PYSNMP_MODULE_ID=bluecoatSGFailoverMIB, bluecoatSGFailoverMIB=bluecoatSGFailoverMIB, bluecoatSgFailoverMIBNotifications=bluecoatSgFailoverMIBNotifications, bluecoatSgFailoverMessage=bluecoatSgFailoverMessage, bluecoatSgFailoverTrap=bluecoatSgFailoverTrap, bluecoatSgFailoverMIBObjects=bluecoatSgFailoverMIBObjects, FailoverMessageString=FailoverMessageString, bluecoatSgFailoverValues=bluecoatSgFailoverValues, bluecoatSgFailoverMIBNotificationsPrefix=bluecoatSgFailoverMIBNotificationsPrefix)
