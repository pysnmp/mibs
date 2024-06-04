#
# PySNMP MIB module BLUECOAT-SG-FAILOVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-FAILOVER-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:18:39 2024
# On host fv-az1789-327 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ModuleIdentity, Integer32, Counter32, ObjectIdentity, MibIdentifier, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, Unsigned32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "Unsigned32", "Counter64", "NotificationType")
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
mibBuilder.exportSymbols("BLUECOAT-SG-FAILOVER-MIB", bluecoatSgFailoverMessage=bluecoatSgFailoverMessage, PYSNMP_MODULE_ID=bluecoatSGFailoverMIB, bluecoatSgFailoverMIBObjects=bluecoatSgFailoverMIBObjects, bluecoatSgFailoverTrap=bluecoatSgFailoverTrap, bluecoatSgFailoverValues=bluecoatSgFailoverValues, bluecoatSGFailoverMIB=bluecoatSGFailoverMIB, bluecoatSgFailoverMIBNotificationsPrefix=bluecoatSgFailoverMIBNotificationsPrefix, FailoverMessageString=FailoverMessageString, bluecoatSgFailoverMIBNotifications=bluecoatSgFailoverMIBNotifications)
