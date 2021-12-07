#
# PySNMP MIB module PRVT-TEMIB-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-TEMIB-ENTITY-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 14:20:37 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Bits, TimeTicks, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, NotificationType, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "NotificationType", "iso", "IpAddress")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
prvtTeMibEntityMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8))
prvtTeMibEntityMIB.setRevisions(('2007-12-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtTeMibEntityMIB.setRevisionsDescriptions(('Initial.',))
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setLastUpdated('200712060000Z')
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtTeMibEntityMIB.setDescription('The MIB module for management of TE-MIB entities.')
class PrvtTeMibAdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a TE-MIB entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtTeMibOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a TE-MIB entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtTeMibEntityIndex(TextualConvention, Unsigned32):
    description = 'The index value identifying a TE-MIB entity.'
    status = 'current'
    displayHint = 'd'

class PrvtTeMibPartnerStatus(TextualConvention, Integer32):
    description = 'The state of a TE-MIB entity partner.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

prvtTeMibEntityMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1))
prvtMplsTeMibEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityTable.setDescription('The table of TE-MIB entities.')
prvtMplsTeMibEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityEntry.setDescription('Each entry represents a TE-MIB entity.')
prvtMplsTeMibEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 1), PrvtTeMibEntityIndex())
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityIndex.setDescription('The index of this TE-MIB entity table entry. This is the\n         HAF entity index passed on the entity create parameters.')
prvtMplsTeMibEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityRowStatus.setDescription("The row status for the TE-MIB entity table entry, used to create\n         and destroy TE-MIB entities.\n         When prvtMplsTeMibEntityRowStatus is 'active' and\n         prvtMplsTeMibEntityAdminStatus is 'up' the TE-MIB entity is active\n         and only these two fields can be modified.")
prvtMplsTeMibDynFacilityBypass = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibDynFacilityBypass.setDescription('This object gives the user ability to globally enable/disable \n         automatically creation of bypass tunnels for all LSPs. Bypass \n         tunnels will be created on FRR tunnel request automatically.\n         The default value is true. The creation of Dynamic bypass tunnels \n         is enabled')
mplsTunnelHoldTimer = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 120))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mplsTunnelHoldTimer.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelHoldTimer.setDescription('Defines a period in seconds needed to wait before rebuilding backup \n         or primary tunnels if a frr condition occurs\n         Currently no more than 10 seconds are allowed')
prvtMplsTeMibEntityScalarTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3), )
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarTable.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarTable.setDescription('The mplsTeMibEntityScalarTable contains all MPLS Tunnel\n         scalars.')
prvtMplsTeMibEntityScalarEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1), ).setIndexNames((0, "PRVT-TEMIB-ENTITY-MIB", "prvtMplsTeMibEntityIndex"))
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarEntry.setStatus('current')
if mibBuilder.loadTexts: prvtMplsTeMibEntityScalarEntry.setDescription('The mplsTeMibEntityScalarTable contains all MPLS Tunnel\n         scalars.')
mplsTunnelConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelConfigured.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelConfigured.setDescription('The number of tunnels configured on this device. A\n         tunnel is considered configured if the\n         mplsTunnelRowStatus is active(1).')
mplsTunnelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 8, 1, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mplsTunnelActive.setStatus('current')
if mibBuilder.loadTexts: mplsTunnelActive.setDescription('The number of tunnels active on this device. A\n         tunnel is considered active if the\n         mplsTunnelOperStatus is up(1).')
mibBuilder.exportSymbols("PRVT-TEMIB-ENTITY-MIB", PYSNMP_MODULE_ID=prvtTeMibEntityMIB, PrvtTeMibOperStatus=PrvtTeMibOperStatus, PrvtTeMibPartnerStatus=PrvtTeMibPartnerStatus, prvtMplsTeMibEntityIndex=prvtMplsTeMibEntityIndex, PrvtTeMibEntityIndex=PrvtTeMibEntityIndex, prvtTeMibEntityMIBObjects=prvtTeMibEntityMIBObjects, prvtTeMibEntityMIB=prvtTeMibEntityMIB, prvtMplsTeMibEntityRowStatus=prvtMplsTeMibEntityRowStatus, prvtMplsTeMibEntityTable=prvtMplsTeMibEntityTable, mplsTunnelHoldTimer=mplsTunnelHoldTimer, prvtMplsTeMibEntityEntry=prvtMplsTeMibEntityEntry, PrvtTeMibAdminStatus=PrvtTeMibAdminStatus, prvtMplsTeMibEntityScalarEntry=prvtMplsTeMibEntityScalarEntry, mplsTunnelConfigured=mplsTunnelConfigured, prvtMplsTeMibDynFacilityBypass=prvtMplsTeMibDynFacilityBypass, mplsTunnelActive=mplsTunnelActive, prvtMplsTeMibEntityScalarTable=prvtMplsTeMibEntityScalarTable)
