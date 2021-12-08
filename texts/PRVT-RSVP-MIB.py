#
# PySNMP MIB module PRVT-RSVP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-RSVP-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:22 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, Bits, Gauge32, Integer32, MibIdentifier, TimeTicks, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "Bits", "Gauge32", "Integer32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "iso")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
prvtRsvpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7))
prvtRsvpMIB.setRevisions(('2011-03-21 00:00', '2009-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtRsvpMIB.setRevisionsDescriptions(('Added prvtRsvpProductFastRerouteCaps.', 'Initial version.',))
if mibBuilder.loadTexts: prvtRsvpMIB.setLastUpdated('201103210000Z')
if mibBuilder.loadTexts: prvtRsvpMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtRsvpMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtRsvpMIB.setDescription('The MIB module for management of the PRVT-RSVP product.')
class PrvtRsvpAdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of an RSVP\n         entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtRsvpOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of an RSVP entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtRsvpIndex(TextualConvention, Unsigned32):
    description = 'The index value identifying an RSVP entity.'
    status = 'current'
    displayHint = 'd'

prvtRsvpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1))
prvtRsvpProductTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1), )
if mibBuilder.loadTexts: prvtRsvpProductTable.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductTable.setDescription('The table of RSVP entities.')
prvtRsvpProductEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1), ).setIndexNames((0, "PRVT-RSVP-MIB", "prvtRsvpProductIndex"))
if mibBuilder.loadTexts: prvtRsvpProductEntry.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductEntry.setDescription('Each entry represents an RSVP entity.')
prvtRsvpProductIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 1), PrvtRsvpIndex())
if mibBuilder.loadTexts: prvtRsvpProductIndex.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductIndex.setDescription('The index of this prvtRsvpProductEntry. This is the\n         HAF entity index passed on the entity create parameters.')
prvtRsvpProductRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductRowStatus.setDescription("Used to create and delete a PRVT-RSVP Product Table entry.\n         When this object is set to 'active', only the\n         prvtRsvpProductAdminStatus object in the row may be modified.")
prvtRsvpProductAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 3), PrvtRsvpAdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductAdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductAdminStatus.setDescription('The desired administrative state of the RSVP entity.')
prvtRsvpProductOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 4), PrvtRsvpOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtRsvpProductOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductOperStatus.setDescription('The current operational state of this instance of PRVT-RSVP.')
prvtRsvpProductProtocolExtensions = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 5), Bits().clone(namedValues=NamedValues(("bypassFastReroute", 0), ("detourFastReroute", 1), ("noResAffOnInIf", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductProtocolExtensions.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductProtocolExtensions.setDescription('Specifies which extensions to the standard RSVP-TE protocol\n         are enabled. For fully standards-compliant behavior, set\n         this parameter to zero (no bits set). To enable specific\n         non-standard protocol extensions, set this parameter to the\n         bitwise OR of whichever of the following behaviors you wish\n         to enable.\n         \n         - bypassFastReroute: Enable support for facility fast reroute\n         protection of LSPs (bypass LSP protection).\n         \n         - detourFastReroute: Enable support for one-to-one fast\n         reroute protection of LSPs (detour LSP protection).\n         \n         - noResAffOnInIf: Disable resource affinity checking on\n         incoming interfaces for LSPs. If this flag is set, RSVP\n         will accept Path messages which use invalid resource\n         affinities for the incoming interface used by the LSP.')
prvtRsvpProductFastRerouteCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 7, 1, 1, 1, 6), Bits().clone(namedValues=NamedValues(("fastReroutePLR", 0), ("fastRerouteMP", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtRsvpProductFastRerouteCaps.setStatus('current')
if mibBuilder.loadTexts: prvtRsvpProductFastRerouteCaps.setDescription('Specifies what fast reroute capabilities are enabled\n         on this node.\n         This field is only valid when the fast reroute extension\n         is enabled (i.e. prvtRsvpProductProtocolExtensions has\n         either of the bypassFastReroute, or detourFastReroute\n         bits set or both).\n         When the fast reroute extension is not enabled, this\n         field should be cleared (no bits set).\n         \n         - PLR: Node provides fast reroute point of local repair\n         capability.\n         \n         - MP: Node provides fast reroute merge point capability.')
mibBuilder.exportSymbols("PRVT-RSVP-MIB", prvtRsvpProductProtocolExtensions=prvtRsvpProductProtocolExtensions, PrvtRsvpIndex=PrvtRsvpIndex, prvtRsvpProductIndex=prvtRsvpProductIndex, PrvtRsvpAdminStatus=PrvtRsvpAdminStatus, prvtRsvpProductTable=prvtRsvpProductTable, prvtRsvpMIB=prvtRsvpMIB, prvtRsvpProductAdminStatus=prvtRsvpProductAdminStatus, prvtRsvpProductEntry=prvtRsvpProductEntry, prvtRsvpProductRowStatus=prvtRsvpProductRowStatus, prvtRsvpProductFastRerouteCaps=prvtRsvpProductFastRerouteCaps, prvtRsvpProductOperStatus=prvtRsvpProductOperStatus, PYSNMP_MODULE_ID=prvtRsvpMIB, prvtRsvpObjects=prvtRsvpObjects, PrvtRsvpOperStatus=PrvtRsvpOperStatus)
