#
# PySNMP MIB module IANA-GMPLS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-GMPLS-TC-MIB
# Produced by pysmi-1.1.12 at Mon Sep  9 08:59:33 2024
# On host fv-az1567-109 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, ObjectIdentity, IpAddress, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, mib_2, ModuleIdentity, TimeTicks, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "ObjectIdentity", "IpAddress", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "mib-2", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaGmpls = ModuleIdentity((1, 3, 6, 1, 2, 1, 152))
ianaGmpls.setRevisions(('2007-02-27 00:00',))
if mibBuilder.loadTexts: ianaGmpls.setLastUpdated('200702270000Z')
if mibBuilder.loadTexts: ianaGmpls.setOrganization('IANA')
class IANAGmplsLSPEncodingTypeTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1. 2. Generalized MPLS Signalling Extensions for G.709 Optical Transport Networks Control, RFC 4328, section 3.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 7, 8, 9, 11, 12, 13))
    namedValues = NamedValues(("tunnelLspNotGmpls", 0), ("tunnelLspPacket", 1), ("tunnelLspEthernet", 2), ("tunnelLspAnsiEtsiPdh", 3), ("tunnelLspSdhSonet", 5), ("tunnelLspDigitalWrapper", 7), ("tunnelLspLambda", 8), ("tunnelLspFiber", 9), ("tunnelLspFiberChannel", 11), ("tunnelDigitalPath", 12), ("tunnelOpticalChannel", 13))

class IANAGmplsSwitchingTypeTC(TextualConvention, Integer32):
    reference = '1. Routing Extensions in Support of Generalized Multi-Protocol Label Switching, RFC 4202, section 2.4. 2. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 51, 100, 150, 200))
    namedValues = NamedValues(("unknown", 0), ("psc1", 1), ("psc2", 2), ("psc3", 3), ("psc4", 4), ("l2sc", 51), ("tdm", 100), ("lsc", 150), ("fsc", 200))

class IANAGmplsGeneralizedPidTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.1.1. 2. Generalized MPLS Signalling Extensions for G.709 Optical Transport Networks Control, RFC 4328, section 3.1.3.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58))
    namedValues = NamedValues(("unknown", 0), ("asynchE4", 5), ("asynchDS3T3", 6), ("asynchE3", 7), ("bitsynchE3", 8), ("bytesynchE3", 9), ("asynchDS2T2", 10), ("bitsynchDS2T2", 11), ("reservedByRFC3471first", 12), ("asynchE1", 13), ("bytesynchE1", 14), ("bytesynch31ByDS0", 15), ("asynchDS1T1", 16), ("bitsynchDS1T1", 17), ("bytesynchDS1T1", 18), ("vc1vc12", 19), ("reservedByRFC3471second", 20), ("reservedByRFC3471third", 21), ("ds1SFAsynch", 22), ("ds1ESFAsynch", 23), ("ds3M23Asynch", 24), ("ds3CBitParityAsynch", 25), ("vtLovc", 26), ("stsSpeHovc", 27), ("posNoScramble16BitCrc", 28), ("posNoScramble32BitCrc", 29), ("posScramble16BitCrc", 30), ("posScramble32BitCrc", 31), ("atm", 32), ("ethernet", 33), ("sdhSonet", 34), ("digitalwrapper", 36), ("lambda", 37), ("ansiEtsiPdh", 38), ("lapsSdh", 40), ("fddi", 41), ("dqdb", 42), ("fiberChannel3", 43), ("hdlc", 44), ("ethernetV2DixOnly", 45), ("ethernet802dot3Only", 46), ("g709ODUj", 47), ("g709OTUk", 48), ("g709CBRorCBRa", 49), ("g709CBRb", 50), ("g709BSOT", 51), ("g709BSNT", 52), ("gfpIPorPPP", 53), ("gfpEthernetMAC", 54), ("gfpEthernetPHY", 55), ("g709ESCON", 56), ("g709FICON", 57), ("g709FiberChannel", 58))

class IANAGmplsAdminStatusInformationTC(TextualConvention, Bits):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 8. 2. Generalized MPLS Signaling - RSVP-TE Extensions, RFC 3473, section 7. 3. GMPLS - Communication of Alarm Information, RFC 4783, section 3.2.1.'
    status = 'current'
    namedValues = NamedValues(("reflect", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("reserved10", 10), ("reserved11", 11), ("reserved12", 12), ("reserved13", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("testing", 29), ("administrativelyDown", 30), ("deleteInProgress", 31))

mibBuilder.exportSymbols("IANA-GMPLS-TC-MIB", IANAGmplsSwitchingTypeTC=IANAGmplsSwitchingTypeTC, ianaGmpls=ianaGmpls, IANAGmplsAdminStatusInformationTC=IANAGmplsAdminStatusInformationTC, IANAGmplsGeneralizedPidTC=IANAGmplsGeneralizedPidTC, PYSNMP_MODULE_ID=ianaGmpls, IANAGmplsLSPEncodingTypeTC=IANAGmplsLSPEncodingTypeTC)
