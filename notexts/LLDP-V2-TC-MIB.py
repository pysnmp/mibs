#
# PySNMP MIB module LLDP-V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/LLDP-V2-TC-MIB
# Produced by pysmi-1.1.12 at Thu May 30 02:12:28 2024
# On host fv-az1567-87 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, org, MibIdentifier, iso, Gauge32, ObjectIdentity, Unsigned32, Bits, IpAddress, Integer32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "org", "MibIdentifier", "iso", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Integer32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
lldpV2TcMIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 12))
lldpV2TcMIB.setRevisions(('2009-06-08 00:00',))
if mibBuilder.loadTexts: lldpV2TcMIB.setLastUpdated('200906080000Z')
if mibBuilder.loadTexts: lldpV2TcMIB.setOrganization('IEEE 802.1 Working Group')
ieee802dot1mibs = MibIdentifier((1, 3, 111, 2, 802, 1, 1))
class LldpV2ChassisIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("chassisComponent", 1), ("interfaceAlias", 2), ("portComponent", 3), ("macAddress", 4), ("networkAddress", 5), ("interfaceName", 6), ("local", 7))

class LldpV2ChassisId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpV2PortIdSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("interfaceAlias", 1), ("portComponent", 2), ("macAddress", 3), ("networkAddress", 4), ("interfaceName", 5), ("agentCircuitId", 6), ("local", 7))

class LldpV2PortId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class LldpV2ManAddrIfSubtype(TextualConvention, Integer32):
    reference = '8.5.9.5'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("ifIndex", 2), ("systemPortNumber", 3))

class LldpV2ManAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 31)

class LldpV2SystemCapabilitiesMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("other", 0), ("repeater", 1), ("bridge", 2), ("wlanAccessPoint", 3), ("router", 4), ("telephone", 5), ("docsisCableDevice", 6), ("stationOnly", 7), ("cVLANComponent", 8), ("sVLANComponent", 9), ("twoPortMACRelay", 10))

class LldpV2DestAddressTableIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4096)

class LldpV2LinkAggStatusMap(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("aggCapable", 0), ("aggEnabled", 1))

class LldpV2PowerPortClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pClassPSE", 1), ("pClassPD", 2))

mibBuilder.exportSymbols("LLDP-V2-TC-MIB", LldpV2ChassisIdSubtype=LldpV2ChassisIdSubtype, LldpV2LinkAggStatusMap=LldpV2LinkAggStatusMap, ieee802dot1mibs=ieee802dot1mibs, LldpV2DestAddressTableIndex=LldpV2DestAddressTableIndex, LldpV2ManAddress=LldpV2ManAddress, LldpV2PortIdSubtype=LldpV2PortIdSubtype, lldpV2TcMIB=lldpV2TcMIB, LldpV2ManAddrIfSubtype=LldpV2ManAddrIfSubtype, PYSNMP_MODULE_ID=lldpV2TcMIB, LldpV2ChassisId=LldpV2ChassisId, LldpV2PowerPortClass=LldpV2PowerPortClass, LldpV2SystemCapabilitiesMap=LldpV2SystemCapabilitiesMap, LldpV2PortId=LldpV2PortId)
