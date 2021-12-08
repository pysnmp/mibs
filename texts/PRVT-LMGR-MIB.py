#
# PySNMP MIB module PRVT-LMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-LMGR-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 21:25:21 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
mpls, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "mpls")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, IpAddress, Integer32, TimeTicks, Gauge32, Counter32, ObjectIdentity, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "Counter32", "ObjectIdentity", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "Counter64", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
prvtLmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4))
prvtLmgrMIB.setRevisions(('2006-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtLmgrMIB.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: prvtLmgrMIB.setLastUpdated('200606110000Z')
if mibBuilder.loadTexts: prvtLmgrMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtLmgrMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtLmgrMIB.setDescription('The MIB module for management of the PRVT-LMGR\n         product.')
class PrvtLmgrAdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a Label\n         Manager entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class PrvtLmgrOperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a Label Manager\n         entity. If the operational state is goingDown then\n         a request to activate the Label Manager entity\n         is rejected.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("up", 1), ("down", 2), ("goingUp", 3), ("goingDown", 4), ("actFailed", 5))

class PrvtLmgrPartnerStatus(TextualConvention, Integer32):
    description = 'The state of a Label Manager partner entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("initial", 0), ("activating", 1), ("active", 2), ("deactivating", 3), ("failedOver", 4), ("failed", 5), ("unavailable", 6))

class PrvtLmgrIndex(TextualConvention, Unsigned32):
    description = 'The index value identifying a Label Manager\n         entity.'
    status = 'current'
    displayHint = 'd'

class PrvtLmgrControlModes(TextualConvention, Integer32):
    description = 'The Control Mode of Label Manager.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ordered", 1), ("independent", 2))

prvtLmgrObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1))
prvtLmgrLsrEntityTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2), )
if mibBuilder.loadTexts: prvtLmgrLsrEntityTable.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityTable.setDescription('Each entry represents an instance of the Label Manager.\n         Each instance is identified by LSR index.')
prvtLmgrLsrEntityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrEntityEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityEntry.setDescription('Each entry represents a Label Manager entity.')
prvtlmgrLsrEntityLsrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 1), PrvtLmgrIndex())
if mibBuilder.loadTexts: prvtlmgrLsrEntityLsrIndex.setStatus('current')
if mibBuilder.loadTexts: prvtlmgrLsrEntityLsrIndex.setDescription('LSR index for this prvtLmgrLsrEntityEntry. This is the\n         entity index passed in the Label Manager create\n         parameters.')
prvtLmgrLsrEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityRowStatus.setDescription("Row status for the Label Manager table entry, used to\n         create and destroy table entries. When\n         prvtLmgrLsrEntityRowStatus is 'active' and\n         prvtLmgrLsrEntityAdminStatus is 'up' Label Manager is\n         active and only these two fields and\n         prvtLmgrLsrEntityMinLsiBuffers can be modified.")
prvtLmgrLsrEntityAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 3), PrvtLmgrAdminStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityAdminStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityAdminStatus.setDescription("Administrative status for Label Manager. When\n         prvtLmgrLsrEntityRowStatus is 'active' and\n         prvtLmgrLsrEntityAdminStatus is 'up' Label Manager is\n         active and only these two fields and\n         prvtLmgrLsrEntityMinLsiBuffers can be modified.")
prvtLmgrLsrEntityOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 4), PrvtLmgrOperStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrEntityOperStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityOperStatus.setDescription('The current operational status of the Label Manager\n         entity.')
prvtLmgrLsrEntityLsrId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityLsrId.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityLsrId.setDescription("An ID that uniquely identifies this LSR within the\n         network.\n         \n         The LSR ID is typically derived from one of the LSR's IP\n         addresses. It may be used for path vector based loop\n         detection if the signaling protocol in use implements\n         that.\n         \n         A value of zero indicates that no LSR ID has been\n         configured. In this case, the signaling protocol stack\n         should construct a unique LSR ID from the other\n         information that is available to it (such as IP\n         addresses). For example, PRVT-CR-LDP and PRVT-RSVP derive\n         the LSR ID by taking the 32 low bits of the following\n         _transport_address_ field, left padding with zeros if\n         necessary.\n         \n         The LSR ID is only used to identify this LSR on IPv4\n         networks. See dcLmgrLsrEntityIpv6TranAddr for equivalent\n         function for use in IPv6 networks.")
prvtLmgrLsrEntityTranAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrType.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrType.setDescription('The type of the internetwork layer address used as the\n         transport address. Currently this must be IPv4. See\n         dcLmgrLsrEntityIpv6TranAddr, below, for the equivalent\n         field for use in IPv6 networks.\n         \n         The transport address is used by LDP as the source\n         transport address for LDP Hello messages for the global\n         (per-platform) label space.\n         \n         The transport address is used by RSVP as the source\n         address for messages originating on unnumbered interfaces.\n         \n         This object indicates how the value of\n         mplsLdpEntityTransAddr is to be interpreted.')
prvtLmgrLsrEntityTranAddrLen = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrLen.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddrLen.setDescription('The length of the internetwork layer address used as the\n         transport address for LDP Hello messages in the global\n         label space and for messages originating on unnumbered\n         interfaces in RSVP. Currently this must be an IPv4\n         address.\n         \n         This object indicates how many elements of the\n         mplsLdpEntityTransAddr array are valid. This value must\n         not exceed _LMGR_LSR_ADDR_LEN_.')
prvtLmgrLsrEntityTranAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddr.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrEntityTranAddr.setDescription('The value of the internetwork layer address used as the\n         transport address for LDP Hello messages in the global\n         label space and for messages originating on unnumbered\n         interfaces in RSVP.\n         \n         This must be an IPv4 address. See\n         dcLmgrLsrEntityIpv6TranAddr, below, for the equivalent\n         field for use in IPv6 networks.\n         \n         If the transport address is not set, then _lsr_id_ must be\n         set to zero. In this case, the transport address and LSR\n         ID are taken from an address on the Interface Information\n         Interface.')
prvtLmgrLsrLspXcTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3), )
if mibBuilder.loadTexts: prvtLmgrLsrLspXcTable.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspXcTable.setDescription('Each entry represents an instance of an LSP\n         cross-conect between a single in-segment and a\n         single out-segment.')
prvtLmgrLsrLspXcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1), ).setIndexNames((0, "PRVT-LMGR-MIB", "prvtlmgrLsrEntityLsrIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspXcIndex"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspInSegLabel"), (0, "PRVT-LMGR-MIB", "prvtLmgrLsrLspOutSegIndex"))
if mibBuilder.loadTexts: prvtLmgrLsrLspXcEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspXcEntry.setDescription('Each entry represents an LSP cross connect.')
prvtLmgrLsrLspXcIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspXcIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspXcIndex.setDescription('XC index for this prvtLmgrLsrLspXc. This is the XC index\n         assigned by Label Manager for the LSP.')
prvtLmgrLsrLspInSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 3), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIndex.setDescription('Index for the in segment. This is the index assigned\n         by Label Manager for the in segment.')
prvtLmgrLsrLspInSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIfIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegIfIndex.setDescription('If index for the in segment. This is the If index\n         specified on setting up the in segment.')
prvtLmgrLsrLspInSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 5), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegLabel.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspInSegLabel.setDescription('Top label for the in segment. This is the Label assigned\n         by Label Manager Label Library for the in segment.')
prvtLmgrLsrLspOutSegIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 6), Unsigned32())
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIndex.setDescription('Index for the out segment. This is the index assigned\n         by Label Manager for the out segment.')
prvtLmgrLsrLspOutSegIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIfIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegIfIndex.setDescription('Interface Index for the out segment. This is the\n         interface index specified when setting up the out segment.')
prvtLmgrLsrLspOutSegLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegLabel.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegLabel.setDescription('Top label for the out segment. This is the label\n         specified by the remote LSR for the out segment.')
prvtLmgrLsrLspOutSegNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 3, 4, 1, 3, 1, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegNextHopAddr.setStatus('current')
if mibBuilder.loadTexts: prvtLmgrLsrLspOutSegNextHopAddr.setDescription('Next hop address for the out segment. This is the address\n         specified by the remote LSR for the out segment.')
mibBuilder.exportSymbols("PRVT-LMGR-MIB", prvtLmgrLsrEntityEntry=prvtLmgrLsrEntityEntry, prvtLmgrLsrLspInSegIfIndex=prvtLmgrLsrLspInSegIfIndex, prvtLmgrLsrEntityOperStatus=prvtLmgrLsrEntityOperStatus, prvtLmgrObjects=prvtLmgrObjects, prvtLmgrLsrEntityTranAddrLen=prvtLmgrLsrEntityTranAddrLen, prvtLmgrLsrEntityAdminStatus=prvtLmgrLsrEntityAdminStatus, prvtLmgrLsrEntityRowStatus=prvtLmgrLsrEntityRowStatus, prvtLmgrLsrLspOutSegIfIndex=prvtLmgrLsrLspOutSegIfIndex, PYSNMP_MODULE_ID=prvtLmgrMIB, prvtLmgrLsrLspXcTable=prvtLmgrLsrLspXcTable, prvtLmgrLsrEntityTable=prvtLmgrLsrEntityTable, PrvtLmgrOperStatus=PrvtLmgrOperStatus, prvtLmgrLsrLspOutSegLabel=prvtLmgrLsrLspOutSegLabel, prvtlmgrLsrEntityLsrIndex=prvtlmgrLsrEntityLsrIndex, PrvtLmgrIndex=PrvtLmgrIndex, prvtLmgrLsrLspOutSegIndex=prvtLmgrLsrLspOutSegIndex, prvtLmgrLsrEntityTranAddrType=prvtLmgrLsrEntityTranAddrType, PrvtLmgrPartnerStatus=PrvtLmgrPartnerStatus, prvtLmgrLsrLspInSegLabel=prvtLmgrLsrLspInSegLabel, prvtLmgrLsrEntityLsrId=prvtLmgrLsrEntityLsrId, prvtLmgrLsrLspXcIndex=prvtLmgrLsrLspXcIndex, prvtLmgrLsrEntityTranAddr=prvtLmgrLsrEntityTranAddr, prvtLmgrLsrLspXcEntry=prvtLmgrLsrLspXcEntry, prvtLmgrLsrLspInSegIndex=prvtLmgrLsrLspInSegIndex, PrvtLmgrAdminStatus=PrvtLmgrAdminStatus, prvtLmgrMIB=prvtLmgrMIB, prvtLmgrLsrLspOutSegNextHopAddr=prvtLmgrLsrLspOutSegNextHopAddr, PrvtLmgrControlModes=PrvtLmgrControlModes)
