#
# PySNMP MIB module WISI-TANGRAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-TANGRAM-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:28:46 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, NotificationType, ModuleIdentity, Bits, Gauge32, iso, TimeTicks, IpAddress, Integer32, Counter32, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "NotificationType", "ModuleIdentity", "Bits", "Gauge32", "iso", "TimeTicks", "IpAddress", "Integer32", "Counter32", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tangram, = mibBuilder.importSymbols("WISI-ROOT-MIB", "tangram")
tangramMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 0))
tangramMIB.setRevisions(('2016-09-08 00:00', '2014-04-29 00:00', '2012-12-06 09:00', '2012-10-31 00:00', '2011-12-13 00:00', '2011-04-12 00:00',))
if mibBuilder.loadTexts: tangramMIB.setLastUpdated('201609080000Z')
if mibBuilder.loadTexts: tangramMIB.setOrganization('WISI Communications GmbH & Co. KG')
gtUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1))
gtGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4))
gtGenericNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0))
gtGenericObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1))
gtGenericNotifyUsertrap = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 0, 1))
if mibBuilder.loadTexts: gtGenericNotifyUsertrap.setStatus('current')
gtGenericObjectUsertrap = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 4, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtGenericObjectUsertrap.setStatus('current')
gtStandards = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4))
gtIP = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 1))
gtRF = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 3))
gtDVB = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 4, 4))
gtTS = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 5))
gtProcessing = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 6))
class FloatingPoint(TextualConvention, OctetString):
    status = 'current'
    displayHint = '63a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 63)

mibBuilder.exportSymbols("WISI-TANGRAM-MIB", gtProcessing=gtProcessing, gtGenericNotifications=gtGenericNotifications, gtGeneric=gtGeneric, FloatingPoint=FloatingPoint, PYSNMP_MODULE_ID=tangramMIB, gtIP=gtIP, gtGenericNotifyUsertrap=gtGenericNotifyUsertrap, tangramMIB=tangramMIB, gtGenericObjects=gtGenericObjects, gtDVB=gtDVB, gtTS=gtTS, gtRF=gtRF, gtGenericObjectUsertrap=gtGenericObjectUsertrap, gtUnit=gtUnit, gtStandards=gtStandards)
