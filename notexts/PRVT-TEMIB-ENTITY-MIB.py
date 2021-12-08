#
# PySNMP MIB module PRVT-TEMIB-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-TEMIB-ENTITY-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:20 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Unsigned32, Integer32, TimeTicks, ModuleIdentity, Counter64, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Unsigned32", "Integer32", "TimeTicks", "ModuleIdentity", "Counter64", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "iso", "ObjectIdentity")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
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
mibBuilder.exportSymbols("PRVT-TEMIB-ENTITY-MIB", mplsTunnelHoldTimer=mplsTunnelHoldTimer, PrvtTeMibAdminStatus=PrvtTeMibAdminStatus, PrvtTeMibEntityIndex=PrvtTeMibEntityIndex, prvtMplsTeMibEntityTable=prvtMplsTeMibEntityTable, prvtMplsTeMibEntityIndex=prvtMplsTeMibEntityIndex, prvtTeMibEntityMIBObjects=prvtTeMibEntityMIBObjects, prvtMplsTeMibEntityScalarEntry=prvtMplsTeMibEntityScalarEntry, prvtMplsTeMibEntityScalarTable=prvtMplsTeMibEntityScalarTable, prvtTeMibEntityMIB=prvtTeMibEntityMIB, prvtMplsTeMibEntityEntry=prvtMplsTeMibEntityEntry, prvtMplsTeMibEntityRowStatus=prvtMplsTeMibEntityRowStatus, PYSNMP_MODULE_ID=prvtTeMibEntityMIB, prvtMplsTeMibDynFacilityBypass=prvtMplsTeMibDynFacilityBypass, mplsTunnelConfigured=mplsTunnelConfigured, PrvtTeMibOperStatus=PrvtTeMibOperStatus, mplsTunnelActive=mplsTunnelActive, PrvtTeMibPartnerStatus=PrvtTeMibPartnerStatus)
