#
# PySNMP MIB module PW-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/PW-TC-STD-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:56:28 2021
# On host fv-az74-115 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Counter32, IpAddress, TimeTicks, Unsigned32, Gauge32, Counter64, iso, MibIdentifier, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Counter32", "IpAddress", "TimeTicks", "Unsigned32", "Gauge32", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "Bits", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pwTcStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 188))
pwTcStdMIB.setRevisions(('2009-04-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pwTcStdMIB.setRevisionsDescriptions(('Original Version',))
if mibBuilder.loadTexts: pwTcStdMIB.setLastUpdated('200904210000Z')
if mibBuilder.loadTexts: pwTcStdMIB.setOrganization('Pseudowire Edge-to-Edge Emulation (PWE3) Working\n                 Group')
if mibBuilder.loadTexts: pwTcStdMIB.setContactInfo(' Thomas D. Nadeau\n     Email:  tom.nadeau@bt.com\n\n     David Zelig\n     Email: davidz@oversi.com\n\n     Orly Nicklass\n     Email: orlyn@radvision.com\n\n     The PWE3 Working Group (email distribution pwe3@ietf.org,\n     http://www.ietf.org/html.charters/pwe3-charter.html)\n    ')
if mibBuilder.loadTexts: pwTcStdMIB.setDescription("This MIB module defines TEXTUAL-CONVENTIONS\n      for concepts used in pseudowire edge-to-edge\n      networks.\n\n      Copyright (c) 2009 IETF Trust and the persons identified\n      as authors of the code.  All rights reserved.\n\n      Redistribution and use in source and binary forms, with or\n      without modification, are permitted provided that the following\n      conditions are met:\n\n      - Redistributions of source code must retain the above\n        copyright notice, this list of conditions and the following\n        disclaimer.\n\n      - Redistributions in binary form must reproduce the above\n        copyright notice, this list of conditions and the following\n        disclaimer in the documentation and/or other materials\n        provided with the distribution.\n\n      - Neither the name of Internet Society, IETF or IETF Trust, nor\n        the names of specific contributors, may be used to endorse or\n        promote products derived from this software without specific\n        prior written permission.\n\n      THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND\n      CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES,\n      INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF\n      MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n      DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR\n      CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,\n      SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT\n      NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;\n      LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)\n      HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN\n      CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR\n      OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,\n      EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n\n      This version of this MIB module is part of RFC 5542;\n      see the RFC itself for full legal notices.")
class PwGroupID(TextualConvention, Unsigned32):
    description = 'An administrative identification for grouping a\n         set of service-specific pseudowire services.'
    status = 'current'
    displayHint = 'd'

class PwIDType(TextualConvention, Unsigned32):
    description = 'Pseudowire Identifier.  Used to identify the PW\n         (together with some other fields) in the signaling\n         session.'
    status = 'current'
    displayHint = 'd'

class PwIndexType(TextualConvention, Unsigned32):
    description = 'Pseudowire Index.  A unique value, greater than zero,\n        for each locally defined PW.  Used for indexing\n        several MIB tables associated with the particular PW.\n        It is recommended that values are assigned contiguously\n        starting from 1.  The value for each PW MUST remain\n        constant at least from one re-initialization\n        to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class PwIndexOrZeroType(TextualConvention, Unsigned32):
    description = 'This TEXTUAL-CONVENTION is an extension of the\n         PwIndexType convention.  The latter defines a greater-\n         than-zero value used to identify a pseudowire\n         in the managed system.  This extension permits the\n         additional value of zero.  The zero value is object-specific\n         and MUST therefore be defined as part of the description of\n         any object that uses this syntax.  Examples of the usage of\n         zero might include situations where pseudowire was unknown,\n         or where none or all pseudowires need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PwOperStatusTC(TextualConvention, Integer32):
    description = "Indicates the operational status of the PW.\n\n     - up(1):             Ready to pass packets.\n     - down(2):           PW signaling is not yet finished, or\n                          indications available at the service\n                          level indicate that the PW is not\n                          passing packets.\n     - testing(3):        AdminStatus at the PW level is set to\n                          test.\n\n     - dormant(4):        The PW is not in a condition to pass\n                          packets but is in a 'pending' state,\n                          waiting for some external event.\n     - notPresent(5):     Some component is missing to accomplish\n                          the setup of the PW.  It can be\n                          configuration error, incomplete\n                          configuration, or a missing H/W component.\n     - lowerLayerDown(6): One or more of the lower-layer interfaces\n                          responsible for running the underlying PSN\n                          is not in OperStatus 'up' state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("dormant", 4), ("notPresent", 5), ("lowerLayerDown", 6))

class PwAttachmentIdentifierType(TextualConvention, OctetString):
    description = 'An octet string used in the generalized Forward Error\n       Correction (FEC) element for identifying attachment forwarder\n       and groups.  A NULL identifier is of zero length.\n      '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwGenIdType(TextualConvention, Unsigned32):
    description = 'Represents the Attachment Group Identifier (AGI) Type and\n       Attachment Individual Identifier (AII) Type in generalized FEC\n       signaling and configuration.\n      '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 254)

class PwCwStatusTC(TextualConvention, Integer32):
    reference = "Martini, et al., 'Pseudowire Setup and Maintenance Using\n       the Label Distribution Protocol', [RFC4447]."
    description = 'Indicates the status of the control word (CW) negotiation\n       based on the local configuration and the indications received\n       from the peer node.\n\n       waitingForNextMsg(1) indicates that the node is waiting for\n       another label mapping from the peer.\n\n       sentWrongBitErrorCode(2) indicates that the local node has\n       notified the peer about a mismatch in the C-bit.\n\n       rxWithdrawWithWrongBitErrorCode(3) indicates that a withdraw\n       message has been received with the wrong C-bit error code.\n\n       illegalReceivedBit(4) indicates a C-bit configuration with\n       the peer that is not compatible with the PW type.\n\n       cwPresent(5) indicates that the CW is present for this PW.\n       If signaling is used, the C-bit is set and agreed upon between\n       the nodes.  For manually configured PW, the local\n       configuration requires the use of the CW.\n\n       cwNotPresent(6) indicates that the CW is not present for this\n       PW.  If signaling is used, the C-bit is reset and agreed upon\n       between the nodes.  For manually configured PW, the local\n       configuration requires that the CW not be used.\n\n       notYetKnown(7) indicates that a label mapping has not yet\n       been received from the peer.\n      '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalReceivedBit", 4), ("cwPresent", 5), ("cwNotPresent", 6), ("notYetKnown", 7))

class PwStatus(TextualConvention, Bits):
    description = 'Indicates the status of the PW and the interfaces affecting\n       this PW.  If none of the bits are set, it indicates no faults\n       are reported.\n      '
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("servicePwRxFault", 1), ("servicePwTxFault", 2), ("psnPwRxFault", 3), ("psnPwTxFault", 4))

class PwFragSize(TextualConvention, Unsigned32):
    description = 'If set to a value other than zero, it indicates the desired\n       fragmentation length in bytes.  If set to zero,\n       fragmentation is not desired for PSN bound packets.\n      '
    status = 'current'
    displayHint = 'd'

class PwFragStatus(TextualConvention, Bits):
    reference = "Malis, A. and M. Townsley, 'Pseudowire Emulation Edge-to-\n        Edge (PWE3) Fragmentation and Reassembly', [RFC4623]."
    description = 'Indicates the status of the fragmentation/reassembly process\n       based on local configuration and peer capability.\n\n       noFrag(0) bit indicates that local configuration is for no\n       fragmentation.\n\n       cfgFragGreaterThanPsnMtu(1) bit indicates that the local node\n       is set to fragment, but the fragmentation size is greater\n       than the MTU available at the PSN between the nodes.\n       Fragmentation is not done in this case.\n\n       cfgFragButRemoteIncapable(2) bit indicates that the local\n       configuration conveys the desire for fragmentation but\n       the peer is not capable of reassembly.\n\n       remoteFragCapable(3) bit indicates that the remote node\n       is capable to accept fragmented PDUs.\n\n       fragEnabled(4) bit indicates that fragmentation will be used\n       on this PW.  Fragmentation can be used if the local node was\n       configured for fragmentation, the peer has the capability\n       to accept fragmented packets, and the CW is in use for this\n       PW.'
    status = 'current'
    namedValues = NamedValues(("noFrag", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragEnabled", 4))

class PwCfgIndexOrzero(TextualConvention, Unsigned32):
    description = 'Index in any of the relevant configuration tables for\n        supplement information regarding configuration of the\n        specific technology.  Value zero implies no additional\n        configuration information is applicable.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("PW-TC-STD-MIB", PwFragStatus=PwFragStatus, PwFragSize=PwFragSize, PwIndexOrZeroType=PwIndexOrZeroType, PwCwStatusTC=PwCwStatusTC, PwGroupID=PwGroupID, pwTcStdMIB=pwTcStdMIB, PwGenIdType=PwGenIdType, PwOperStatusTC=PwOperStatusTC, PwCfgIndexOrzero=PwCfgIndexOrzero, PwIndexType=PwIndexType, PwIDType=PwIDType, PwAttachmentIdentifierType=PwAttachmentIdentifierType, PYSNMP_MODULE_ID=pwTcStdMIB, PwStatus=PwStatus)
