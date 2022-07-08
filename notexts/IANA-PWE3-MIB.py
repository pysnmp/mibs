#
# PySNMP MIB module IANA-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-PWE3-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:16:05 2022
# On host fv-az206-808 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, TimeTicks, IpAddress, Unsigned32, mib_2, Counter64, Integer32, ModuleIdentity, Counter32, ObjectIdentity, Bits, iso, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "IpAddress", "Unsigned32", "mib-2", "Counter64", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "iso", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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

mibBuilder.exportSymbols("IANA-PWE3-MIB", IANAPwCapabilities=IANAPwCapabilities, ianaPwe3MIB=ianaPwe3MIB, IANAPwPsnTypeTC=IANAPwPsnTypeTC, PYSNMP_MODULE_ID=ianaPwe3MIB, IANAPwTypeTC=IANAPwTypeTC)
