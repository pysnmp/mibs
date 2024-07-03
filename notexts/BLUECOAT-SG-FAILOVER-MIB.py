#
# PySNMP MIB module BLUECOAT-SG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:00:41 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, TimeTicks, Counter32, MibIdentifier, Gauge32, IpAddress, Integer32, ObjectIdentity, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "TimeTicks", "Counter32", "MibIdentifier", "Gauge32", "IpAddress", "Integer32", "ObjectIdentity", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BLUECOAT-SG-FAILOVER-MIB", bluecoatSgFailoverMIBNotifications=bluecoatSgFailoverMIBNotifications, bluecoatSgFailoverTrap=bluecoatSgFailoverTrap, bluecoatSgFailoverValues=bluecoatSgFailoverValues, bluecoatSGFailoverMIB=bluecoatSGFailoverMIB, bluecoatSgFailoverMIBNotificationsPrefix=bluecoatSgFailoverMIBNotificationsPrefix, bluecoatSgFailoverMessage=bluecoatSgFailoverMessage, PYSNMP_MODULE_ID=bluecoatSGFailoverMIB, bluecoatSgFailoverMIBObjects=bluecoatSgFailoverMIBObjects, FailoverMessageString=FailoverMessageString)
