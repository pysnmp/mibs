#
# PySNMP MIB module BLUECOAT-SG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.1.8 at Tue Jan 18 14:01:12 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, Gauge32, ModuleIdentity, iso, TimeTicks, Bits, Unsigned32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "ModuleIdentity", "iso", "TimeTicks", "Bits", "Unsigned32", "Integer32", "IpAddress")
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
mibBuilder.exportSymbols("BLUECOAT-SG-FAILOVER-MIB", bluecoatSgFailoverMIBNotifications=bluecoatSgFailoverMIBNotifications, bluecoatSgFailoverTrap=bluecoatSgFailoverTrap, bluecoatSgFailoverValues=bluecoatSgFailoverValues, FailoverMessageString=FailoverMessageString, bluecoatSgFailoverMessage=bluecoatSgFailoverMessage, bluecoatSgFailoverMIBNotificationsPrefix=bluecoatSgFailoverMIBNotificationsPrefix, bluecoatSgFailoverMIBObjects=bluecoatSgFailoverMIBObjects, bluecoatSGFailoverMIB=bluecoatSGFailoverMIB, PYSNMP_MODULE_ID=bluecoatSGFailoverMIB)
