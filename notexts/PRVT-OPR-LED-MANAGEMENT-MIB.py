#
# PySNMP MIB module PRVT-OPR-LED-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OPR-LED-MANAGEMENT-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 15:50:13 2021
# On host fv-az74-277 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, ObjectIdentity, NotificationType, Bits, Gauge32, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "ObjectIdentity", "NotificationType", "Bits", "Gauge32", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "Integer32", "iso")
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
mibBuilder.exportSymbols("PRVT-OPR-LED-MANAGEMENT-MIB", prvtOprLedSatus=prvtOprLedSatus, prvtOprLedMgmtMIB=prvtOprLedMgmtMIB, PYSNMP_MODULE_ID=prvtOprLedMgmtMIB, LedValues=LedValues, prvtOprLedMgmtConformance=prvtOprLedMgmtConformance, prvtOprLedMgmtNotifications=prvtOprLedMgmtNotifications, prvtOprLedMgmtObjects=prvtOprLedMgmtObjects)
