#
# PySNMP MIB module IANA-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-PWE3-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:03:22 2024
# On host fv-az883-299 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, Counter64, IpAddress, NotificationType, MibIdentifier, Integer32, Gauge32, Unsigned32, iso, mib_2, Counter32, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "Counter64", "IpAddress", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "Unsigned32", "iso", "mib-2", "Counter32", "TimeTicks", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaPwe3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 174))
ianaPwe3MIB.setRevisions(('2009-06-11 00:00',))
if mibBuilder.loadTexts: ianaPwe3MIB.setLastUpdated('200906110000Z')
if mibBuilder.loadTexts: ianaPwe3MIB.setOrganization('IANA')
class IANAPwTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 32767))
    namedValues = NamedValues(("other", 0), ("frameRelayDlciMartiniMode", 1), ("atmAal5SduVcc", 2), ("atmTransparent", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmCellNto1Vcc", 9), ("atmCellNto1Vpc", 10), ("ipLayer2Transport", 11), ("atmCell1to1Vcc", 12), ("atmCell1to1Vpc", 13), ("atmAal5PduVcc", 14), ("frameRelayPortMode", 15), ("cep", 16), ("e1Satop", 17), ("t1Satop", 18), ("e3Satop", 19), ("t3Satop", 20), ("basicCesPsn", 21), ("basicTdmIp", 22), ("tdmCasCesPsn", 23), ("tdmCasTdmIp", 24), ("frDlci", 25), ("wildcard", 32767))

class IANAPwPsnTypeTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mpls", 1), ("l2tp", 2), ("udpOverIp", 3), ("mplsOverIp", 4), ("mplsOverGre", 5), ("other", 6))

class IANAPwCapabilities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0), ("pwVCCV", 1))

mibBuilder.exportSymbols("IANA-PWE3-MIB", IANAPwCapabilities=IANAPwCapabilities, IANAPwPsnTypeTC=IANAPwPsnTypeTC, IANAPwTypeTC=IANAPwTypeTC, ianaPwe3MIB=ianaPwe3MIB, PYSNMP_MODULE_ID=ianaPwe3MIB)
