#
# PySNMP MIB module PRVT-OPR-LED-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OPR-LED-MANAGEMENT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Counter64, Bits, IpAddress, MibIdentifier, Gauge32, ObjectIdentity, Unsigned32, ModuleIdentity, TimeTicks, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Counter64", "Bits", "IpAddress", "MibIdentifier", "Gauge32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "TimeTicks", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtOprLedMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 110))
prvtOprLedMgmtMIB.setRevisions(('2006-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setRevisionsDescriptions(('Initial revision history',))
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setLastUpdated('200607290000Z')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setContactInfo('BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setDescription('Initial version. This MIB will provied a way to control\nthe status of the state OPR LED for certain switches')
class LedValues(TextualConvention, Integer32):
    description = 'All possible led states'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("green-stable", 1), ("green-blinking", 2), ("amber-stable", 3), ("amber-blinking", 4), ("red-stable", 5), ("red-blinking", 6))

prvtOprLedMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1))
prvtOprLedMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 2))
prvtOprLedMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 3))
prvtOprLedSatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1, 1), LedValues().clone('green-stable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOprLedSatus.setStatus('current')
if mibBuilder.loadTexts: prvtOprLedSatus.setDescription('All possible led states. States red-stable and red-blinking\ncan not be set. States amber-stable and amber-blinking green-blinking can\nbe set only when the current state is green-stable. The object\nhas read-write access and its default value is green-stable')
mibBuilder.exportSymbols("PRVT-OPR-LED-MANAGEMENT-MIB", prvtOprLedMgmtConformance=prvtOprLedMgmtConformance, LedValues=LedValues, prvtOprLedMgmtMIB=prvtOprLedMgmtMIB, prvtOprLedSatus=prvtOprLedSatus, PYSNMP_MODULE_ID=prvtOprLedMgmtMIB, prvtOprLedMgmtNotifications=prvtOprLedMgmtNotifications, prvtOprLedMgmtObjects=prvtOprLedMgmtObjects)
