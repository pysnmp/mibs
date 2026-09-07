#
# PySNMP MIB module CISCO-IETF-PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-IETF-PW-TC-MIB
# Source digest sha256:113765d39718fe49d078fb29461e0bf60f61ee50931563befe36af9758a1da66
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cpwTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 20000, 1))
cpwTCMIB.setRevisions(('2006-07-21 12:00', '2003-02-26 12:00', '2002-05-28 12:00', '2002-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cpwTCMIB.setRevisionsDescriptions(('Added following enumerations to cpwVcType TC:\n           e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15), \n           basicCesPsn(16), basicTdmIp(17), tdmCasCesPsn(18),\n           tdmCasTdmIp(19). The above enumerations are based \n           on IANAPwTypeTC TC in draft-ietf-pwe3-pw-mib-08.txt', 'Made Cisco proprietary based on the PW-TC-MIB.my file\n            extracted from draft-ietf-pwe3-pw-tc-mib-00.txt\n           ', 'Adding PwVcType, and enhance some descriptions.', 'Adding PwVcVlanCfg, PwAddressType and  \n                  PwOperStatus.', 'Remove PwVcInstance', 'Initial version.',))
if mibBuilder.loadTexts: cpwTCMIB.setLastUpdated('2006-07-21 12:00')
if mibBuilder.loadTexts: cpwTCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cpwTCMIB.setContactInfo(' \n       Thomas D. Nadeau \n       Postal: Cisco Systems, Inc. \n               250 Apollo Drive \n               Chelmsford, MA 01824 \n       Tel:    +1-978-497-3051 \n       Email:  tnadeau@cisco.com \n\n       MPLS MIB Development Team\n       Postal: Cisco Systems, Inc.\n               250 Apollo Drive\n               Chelmsford, MA 01924\n       Tel:    +1-978-497-3989\n       Email:  ch-mpls-mib-dev@cisco.com\n     ')
if mibBuilder.loadTexts: cpwTCMIB.setDescription('This MIB Module provides Textual Conventions \n          and OBJECT-IDENTITY Objects to be used PW services.')
cpwMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 20000))
class CpwGroupID(TextualConvention, Unsigned32):
    description = 'An administrative identification mechanism for grouping a \n           set of service-specific pseudo-wire services. May only \n           have local significance.'
    status = 'current'

class CpwVcIDType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Identifier. Used to identify the VC  \n           (together with some other fields) in the signaling  \n           session. Zero if the VC is set-up manually.'
    status = 'current'

class CpwVcIndexType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Index. Locally unique index for indexing \n           several MIB tables associated with a particular VC.'
    status = 'current'

class CpwVcVlanCfg(TextualConvention, Integer32):
    description = 'VLAN configuration for Ethernet PW.  \n           Values between 0 to 4095 indicate the actual VLAN field \n           value.  \n           A value of 4096 indicates that the object refer to  \n           untagged frames, i.e. frames without 802.1Q field. \n           A value of 4097 indicates that the object is not  \n           relevant.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class CpwOperStatus(TextualConvention, Integer32):
    description = "Indicate the operational status of the PW VC. \n\n        - up:             Ready to pass packets.  \n        - down:           If PW signaling has not yet finished, or \n                          indications available at the service  \n                          level indicate that the VC is not  \n                          passing packets. \n        - testing:        If AdminStatus at the VC level is set to  \n                          test. \n        - dormant:        The VC is not available because of the \n                          required resources are occupied VC with  \n                          higher priority VCs . \n        - notPresent:     Some component is missing to accomplish  \n                          the set up of the VC. \n        - lowerLayerDown: The underlying PSN or outer tunnel is not \n                          in OperStatus 'up'.  \n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class CpwVcType(TextualConvention, Integer32):
    description = 'Indicate the VC type (i.e. the carried service). \n         Note: the exact set of VC types is yet to be worked  \n         out by the WG. \n        '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5Vcc", 2), ("atmTransparent", 3), ("ethernetVLAN", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cep", 8), ("atmVccCell", 9), ("atmVpcCell", 10), ("ethernetVPLS", 11), ("e1Satop", 12), ("t1Satop", 13), ("e3Satop", 14), ("t3Satop", 15), ("basicCesPsn", 16), ("basicTdmIp", 17), ("tdmCasCesPsn", 18), ("tdmCasTdmIp", 19))

mibBuilder.exportSymbols("CISCO-IETF-PW-TC-MIB", CpwGroupID=CpwGroupID, CpwOperStatus=CpwOperStatus, CpwVcIDType=CpwVcIDType, CpwVcIndexType=CpwVcIndexType, CpwVcType=CpwVcType, CpwVcVlanCfg=CpwVcVlanCfg, PYSNMP_MODULE_ID=cpwTCMIB, cpwMIB=cpwMIB, cpwTCMIB=cpwTCMIB)
