#
# PySNMP MIB module PRVT-OPR-LED-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OPR-LED-MANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:20:34 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, TimeTicks, NotificationType, Counter64, ObjectIdentity, Counter32, Gauge32, ModuleIdentity, Integer32, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "TimeTicks", "NotificationType", "Counter64", "ObjectIdentity", "Counter32", "Gauge32", "ModuleIdentity", "Integer32", "iso", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtOprLedMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 110))
prvtOprLedMgmtMIB.setRevisions(('2006-07-29 00:00',))
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setLastUpdated('200607290000Z')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setOrganization('BATM Advanced Communication')
class LedValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("green-stable", 1), ("green-blinking", 2), ("amber-stable", 3), ("amber-blinking", 4), ("red-stable", 5), ("red-blinking", 6))

prvtOprLedMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1))
prvtOprLedMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 2))
prvtOprLedMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 3))
prvtOprLedSatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1, 1), LedValues().clone('green-stable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOprLedSatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-OPR-LED-MANAGEMENT-MIB", LedValues=LedValues, PYSNMP_MODULE_ID=prvtOprLedMgmtMIB, prvtOprLedMgmtObjects=prvtOprLedMgmtObjects, prvtOprLedSatus=prvtOprLedSatus, prvtOprLedMgmtNotifications=prvtOprLedMgmtNotifications, prvtOprLedMgmtConformance=prvtOprLedMgmtConformance, prvtOprLedMgmtMIB=prvtOprLedMgmtMIB)
