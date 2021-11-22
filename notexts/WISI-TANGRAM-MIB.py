#
# PySNMP MIB module WISI-TANGRAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-TANGRAM-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:35:21 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, IpAddress, ModuleIdentity, Bits, Counter32, MibIdentifier, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "ModuleIdentity", "Bits", "Counter32", "MibIdentifier", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("WISI-TANGRAM-MIB", gtGenericNotifyUsertrap=gtGenericNotifyUsertrap, FloatingPoint=FloatingPoint, gtGeneric=gtGeneric, gtProcessing=gtProcessing, gtStandards=gtStandards, PYSNMP_MODULE_ID=tangramMIB, gtUnit=gtUnit, gtRF=gtRF, gtDVB=gtDVB, gtGenericNotifications=gtGenericNotifications, gtGenericObjectUsertrap=gtGenericObjectUsertrap, gtIP=gtIP, tangramMIB=tangramMIB, gtGenericObjects=gtGenericObjects, gtTS=gtTS)
