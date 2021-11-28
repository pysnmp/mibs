#
# PySNMP MIB module PRVT-TEMIB-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-TEMIB-ENTITY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 16:43:29 2021
# On host fv-az126-355 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
mpls, = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "mpls")
PrvtLmgrPartnerStatus, PrvtLmgrIndex = mibBuilder.importSymbols("PRVT-LMGR-MIB", "PrvtLmgrPartnerStatus", "PrvtLmgrIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, TimeTicks, IpAddress, NotificationType, Gauge32, iso, Counter32, MibIdentifier, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "IpAddress", "NotificationType", "Gauge32", "iso", "Counter32", "MibIdentifier", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "Counter64")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
prvtTeMibEntityMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8))
prvtTeMibEntityMib.setRevisions(('2007-12-06 00:00',))
if mibBuilder.loadTexts: prvtTeMibEntityMib.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: prvtTeMibEntityMib.setOrganization('BATM Advanced Communication')
prvtTeMibEntityObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1))
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

class PrvtTeMibPartnerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

prvtMplsTeMibEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setStatus('current')
prvtMplsTeMibEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setStatus('current')
prvtMplsTeMibEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 1), PrvtTeMibEntityIndex())
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setStatus('current')
prvtMplsTeMibEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 2), PrvtTeMibAdminStatus().clone('up')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityAdminStatus.setStatus('current')
prvtMplsTeMibEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 3), PrvtTeMibOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibEntityOperStatus.setStatus('current')
prvtMplsTeMibEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setStatus('current')
prvtMplsTeMibTunnelRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(3000)).setUnits('milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryInterval.setStatus('current')
prvtMplsTeMibTunnelRetryDecayRate = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryDecayRate.setStatus('current')
prvtMplsTeMibTunnelRetryMax = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTunnelRetryMax.setStatus('current')
prvtMplsTeMibTnnlBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibTnnlBufPoolSize.setStatus('current')
prvtMplsTeMibLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 9), PrvtLmgrIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibLsrIndex.setStatus('current')
prvtMplsTeMibLdbStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 10), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLdbStatus.setStatus('current')
prvtMplsTeMibLraStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 11), PrvtLmgrPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLraStatus.setStatus('current')
prvtMplsTeMibLdiStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 12), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibLdiStatus.setStatus('current')
prvtMplsTeMibRsvpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 13), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpEnable.setStatus('current')
prvtMplsTeMibCrldpEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibCrldpEnable.setStatus('current')
prvtMplsTeMibCrldpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 15), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibCrldpIndex.setStatus('current')
prvtMplsTeMibUseRsvpResvConf = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 16), Bits().clone(namedValues=NamedValues(("useResvConfForUNI", 0), ("useResvConfForGMPLS", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibUseRsvpResvConf.setStatus('current')
prvtMplsTeMibAllowGracefulDeletion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibAllowGracefulDeletion.setStatus('current')
prvtMplsTeMibShowTransitTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 18), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibShowTransitTunnels.setStatus('current')
prvtMplsTeMibSupportCHopTable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 19), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibSupportCHopTable.setStatus('current')
prvtMplsTeMibNhrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 20), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibNhrIndex.setStatus('current')
prvtMplsTeMibNhrBufPoolSize = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 21), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibNhrBufPoolSize.setStatus('current')
prvtMplsTeMibNhrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 22), PrvtTeMibPartnerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibNhrStatus.setStatus('current')
prvtMplsTeMibExtPrtSuppAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 23), PrvtTeMibAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibExtPrtSuppAdminStatus.setStatus('current')
prvtMplsTeMibRsvpIpv6AdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 24), PrvtTeMibAdminStatus().clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6AdminStatus.setStatus('current')
prvtMplsTeMibRsvpIpv6OperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 25), PrvtTeMibOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsTeMibRsvpIpv6OperStatus.setStatus('current')
prvtMplsTeMibDynFacilityBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 1, 1, 1, 26), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setStatus('current')
prvtTeMibEntityConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2))
prvtTeMibEntityCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1))
prvtTeMibEntityGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2))
prvtTeMibEntityMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 1, 1)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibMandatoryGroup"), ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibOptionalGroup"), ("PRVT-TEMIB-ENTITY-MIB", "mplsTeMibCrldpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtTeMibEntityMibCompliance = prvtTeMibEntityMibCompliance.setStatus('current')
mplsTeMibMandatoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 2)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibMandatoryGroup = mplsTeMibMandatoryGroup.setStatus('current')
mplsTeMibOptionalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 3)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityAdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityOperStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryInterval"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryDecayRate"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTunnelRetryMax"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibTnnlBufPoolSize"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLsrIndex"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdbStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLraStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpEnable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibUseRsvpResvConf"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibAllowGracefulDeletion"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibShowTransitTunnels"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibSupportCHopTable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrIndex"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrBufPoolSize"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibNhrStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibExtPrtSuppAdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6AdminStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibRsvpIpv6OperStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibDynFacilityBypass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibOptionalGroup = mplsTeMibOptionalGroup.setStatus('current')
mplsTeMibCrldpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 8, 2, 2, 4)).setObjects(("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibLdiStatus"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpEnable"), ("PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibCrldpIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mplsTeMibCrldpGroup = mplsTeMibCrldpGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-TEMIB-ENTITY-MIB", prvtTeMibEntityMib=prvtTeMibEntityMib, prvtMplsTeMibCrldpEnable=prvtMplsTeMibCrldpEnable, PrvtTeMibAdminStatus=PrvtTeMibAdminStatus, prvtMplsTeMibTunnelRetryInterval=prvtMplsTeMibTunnelRetryInterval, mplsTeMibCrldpGroup=mplsTeMibCrldpGroup, PrvtTeMibPartnerStatus=PrvtTeMibPartnerStatus, prvtTeMibEntityConformance=prvtTeMibEntityConformance, prvtMplsTeMibEntityRowStatus=prvtMplsTeMibEntityRowStatus, prvtMplsTeMibLdbStatus=prvtMplsTeMibLdbStatus, prvtMplsTeMibLdiStatus=prvtMplsTeMibLdiStatus, mplsTeMibOptionalGroup=mplsTeMibOptionalGroup, prvtMplsTeMibNhrIndex=prvtMplsTeMibNhrIndex, prvtMplsTeMibTnnlBufPoolSize=prvtMplsTeMibTnnlBufPoolSize, prvtMplsTeMibRsvpEnable=prvtMplsTeMibRsvpEnable, mplsTeMibMandatoryGroup=mplsTeMibMandatoryGroup, prvtMplsTeMibNhrBufPoolSize=prvtMplsTeMibNhrBufPoolSize, prvtTeMibEntityMibCompliance=prvtTeMibEntityMibCompliance, PYSNMP_MODULE_ID=prvtTeMibEntityMib, prvtMplsTeMibLsrIndex=prvtMplsTeMibLsrIndex, prvtMplsTeMibTunnelRetryDecayRate=prvtMplsTeMibTunnelRetryDecayRate, prvtMplsTeMibTunnelRetryMax=prvtMplsTeMibTunnelRetryMax, prvtMplsTeMibEntityEntry=prvtMplsTeMibEntityEntry, PrvtTeMibOperStatus=PrvtTeMibOperStatus, prvtTeMibEntityObjects=prvtTeMibEntityObjects, prvtMplsTeMibShowTransitTunnels=prvtMplsTeMibShowTransitTunnels, prvtMplsTeMibRsvpIpv6AdminStatus=prvtMplsTeMibRsvpIpv6AdminStatus, prvtMplsTeMibLraStatus=prvtMplsTeMibLraStatus, prvtMplsTeMibAllowGracefulDeletion=prvtMplsTeMibAllowGracefulDeletion, prvtMplsTeMibEntityOperStatus=prvtMplsTeMibEntityOperStatus, prvtMplsTeMibEntityTable=prvtMplsTeMibEntityTable, prvtTeMibEntityGroups=prvtTeMibEntityGroups, prvtMplsTeMibRsvpIpv6OperStatus=prvtMplsTeMibRsvpIpv6OperStatus, prvtMplsTeMibCrldpIndex=prvtMplsTeMibCrldpIndex, prvtMplsTeMibUseRsvpResvConf=prvtMplsTeMibUseRsvpResvConf, prvtMplsTeMibDynFacilityBypass=prvtMplsTeMibDynFacilityBypass, PrvtTeMibEntityIndex=PrvtTeMibEntityIndex, prvtMplsTeMibEntityIndex=prvtMplsTeMibEntityIndex, prvtMplsTeMibSupportCHopTable=prvtMplsTeMibSupportCHopTable, prvtMplsTeMibEntityAdminStatus=prvtMplsTeMibEntityAdminStatus, prvtTeMibEntityCompliances=prvtTeMibEntityCompliances, prvtMplsTeMibNhrStatus=prvtMplsTeMibNhrStatus, prvtMplsTeMibExtPrtSuppAdminStatus=prvtMplsTeMibExtPrtSuppAdminStatus)
