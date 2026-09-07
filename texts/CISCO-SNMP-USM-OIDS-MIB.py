#
# PySNMP MIB module CISCO-SNMP-USM-OIDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-SNMP-USM-OIDS-MIB
# Source digest sha256:b3d7854867674b2c5d2abf8dc2ad9468876b272535ce9fb3d5f526e4ae566244
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpUsmOidsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 6))
ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setLastUpdated('2006-02-28 00:00')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setDescription("This MIB extends the OID's for SNMP-USM-MIB\n                 specified in RFC 3414.\n\n                The privacy protocol OID's specified herein \n                are intended to be used as values  for \n                usmUserPrivProtocol when managing SNMPv3  \n                users via the snmpUsmMIB.\n\n                This MIB defines the OID's for the following\n                encryption options:\n\n                        * 192 bit key size AES\n                        * 256 bit key size AES\n                        * 168 bit key size 3DES.\n\n                OID for 128 bit key size AES encryption is \n                defined in SNMP-USM-AES-MIB as per the \n                RFC 3826.")
ciscoSnmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1))
cusmAESCfb192PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1))
cusmAESCfb256PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2))
cusm3DES168PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3))
mibBuilder.exportSymbols("CISCO-SNMP-USM-OIDS-MIB", PYSNMP_MODULE_ID=ciscoSnmpUsmOidsMIB, ciscoSnmpPrivProtocols=ciscoSnmpPrivProtocols, ciscoSnmpUsmOidsMIB=ciscoSnmpUsmOidsMIB, cusm3DES168PrivProtocol=cusm3DES168PrivProtocol, cusmAESCfb192PrivProtocol=cusmAESCfb192PrivProtocol, cusmAESCfb256PrivProtocol=cusmAESCfb256PrivProtocol)
