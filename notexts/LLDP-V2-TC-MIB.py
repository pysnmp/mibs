#
# PySNMP MIB module LLDP-V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/LLDP-V2-TC-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 20:18:54 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, TimeTicks, Counter64, iso, Bits, Counter32, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, org, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "TimeTicks", "Counter64", "iso", "Bits", "Counter32", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "org", "ModuleIdentity")
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

mibBuilder.exportSymbols("LLDP-V2-TC-MIB", LldpV2ManAddress=LldpV2ManAddress, LldpV2ChassisId=LldpV2ChassisId, ieee802dot1mibs=ieee802dot1mibs, LldpV2DestAddressTableIndex=LldpV2DestAddressTableIndex, LldpV2PortIdSubtype=LldpV2PortIdSubtype, LldpV2SystemCapabilitiesMap=LldpV2SystemCapabilitiesMap, LldpV2PortId=LldpV2PortId, LldpV2ChassisIdSubtype=LldpV2ChassisIdSubtype, PYSNMP_MODULE_ID=lldpV2TcMIB, LldpV2ManAddrIfSubtype=LldpV2ManAddrIfSubtype, LldpV2PowerPortClass=LldpV2PowerPortClass, lldpV2TcMIB=lldpV2TcMIB, LldpV2LinkAggStatusMap=LldpV2LinkAggStatusMap)
