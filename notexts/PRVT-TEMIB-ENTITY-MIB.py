#
# PySNMP MIB module PRVT-TEMIB-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-TEMIB-ENTITY-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 14:17:50 2021
# On host fv-az33-388 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, Counter32, Counter64, ModuleIdentity, Bits, ObjectIdentity, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "Counter32", "Counter64", "ModuleIdentity", "Bits", "ObjectIdentity", "iso", "Integer32", "Gauge32")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
prvtTeMibEntityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8))
prvtTeMibEntityMIB.setRevisions(('2007-12-06 00:00',))
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setOrganization('BATM Advanced Communication')
class PrvtTeMibAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtTeMibOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtTeMibEntityIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class PrvtTeMibPartnerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

prvtTeMibEntityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1))
prvtMplsTeMibEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setStatus('current')
prvtMplsTeMibEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setStatus('current')
prvtMplsTeMibEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 1), PrvtTeMibEntityIndex())
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setStatus('current')
prvtMplsTeMibEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setStatus('current')
prvtMplsTeMibDynFacilityBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setStatus('current')
mplsTunnelHoldTimer = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsTunnelHoldTimer.setStatus('current')
prvtMplsTeMibEntityScalarTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarTable.setStatus('current')
prvtMplsTeMibEntityScalarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarEntry.setStatus('current')
mplsTunnelConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelConfigured.setStatus('current')
mplsTunnelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelActive.setStatus('current')
mibBuilder.exportSymbols("PRVT-TEMIB-ENTITY-MIB", prvtMplsTeMibDynFacilityBypass=prvtMplsTeMibDynFacilityBypass, prvtMplsTeMibEntityIndex=prvtMplsTeMibEntityIndex, PrvtTeMibPartnerStatus=PrvtTeMibPartnerStatus, PrvtTeMibAdminStatus=PrvtTeMibAdminStatus, prvtMplsTeMibEntityScalarTable=prvtMplsTeMibEntityScalarTable, prvtMplsTeMibEntityTable=prvtMplsTeMibEntityTable, mplsTunnelConfigured=mplsTunnelConfigured, prvtMplsTeMibEntityScalarEntry=prvtMplsTeMibEntityScalarEntry, PYSNMP_MODULE_ID=prvtTeMibEntityMIB, PrvtTeMibEntityIndex=PrvtTeMibEntityIndex, mplsTunnelHoldTimer=mplsTunnelHoldTimer, prvtTeMibEntityMIBObjects=prvtTeMibEntityMIBObjects, mplsTunnelActive=mplsTunnelActive, PrvtTeMibOperStatus=PrvtTeMibOperStatus, prvtMplsTeMibEntityEntry=prvtMplsTeMibEntityEntry, prvtTeMibEntityMIB=prvtTeMibEntityMIB, prvtMplsTeMibEntityRowStatus=prvtMplsTeMibEntityRowStatus)
