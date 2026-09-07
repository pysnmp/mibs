#
# PySNMP MIB module CISCO-TM (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-TM
# Source digest sha256:74f1ee4c4647e0bb2bf98441dc6cdad231de900373ad05b8795cedff8ab00448
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDomains, = mibBuilder.importSymbols("CISCO-SMI", "ciscoDomains")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTransportMappings = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1))
ciscoTransportMappings.setRevisions(('2001-08-23 16:00', '2000-06-21 16:00',))
if mibBuilder.loadTexts: ciscoTransportMappings.setLastUpdated('2001-08-23 16:00')
if mibBuilder.loadTexts: ciscoTransportMappings.setOrganization('Cisco Systems, Inc.')
snmpUDPVPNDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 1))
if mibBuilder.loadTexts: snmpUDPVPNDomain.setStatus('current')
class SnmpUDPVPNAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 38)

snmpAAL5Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 2))
if mibBuilder.loadTexts: snmpAAL5Domain.setStatus('current')
class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d/4d/4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

snmpCNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 3))
if mibBuilder.loadTexts: snmpCNSDomain.setStatus('current')
class SnmpCNSIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '19a.255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 274)

mibBuilder.exportSymbols("CISCO-TM", PYSNMP_MODULE_ID=ciscoTransportMappings, SnmpAAL5VCIdentifier=SnmpAAL5VCIdentifier, SnmpCNSIdentifier=SnmpCNSIdentifier, SnmpUDPVPNAddress=SnmpUDPVPNAddress, ciscoTransportMappings=ciscoTransportMappings, snmpAAL5Domain=snmpAAL5Domain, snmpCNSDomain=snmpCNSDomain, snmpUDPVPNDomain=snmpUDPVPNDomain)
